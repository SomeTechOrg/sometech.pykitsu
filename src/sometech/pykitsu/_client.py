"""The Kitsu clients.

Building a client is cheap: API groups (``client.shots``, ``client.tasks``…)
and their pydantic models are imported the first time you use them.
"""

from __future__ import annotations

import logging
import os
from collections.abc import Mapping
from types import TracebackType
from typing import Any

import httpx
from typing_extensions import Self

from ._auth import _AuthMixin
from ._groups import GROUP_NAMES, _AsyncGroups, _Groups
from ._transport import AsyncTransport, SyncTransport
from .errors import KitsuAPIError

logger = logging.getLogger("pykitsu")

# Statuses meaning "this token is not valid any more" (flask-jwt answers 422 for a malformed one).
_INVALID_TOKEN_STATUSES = (401, 422)

__all__ = ["AsyncPyKitsu", "PyKitsu"]


def _env(host: str | None, token: str | None) -> dict[str, Any]:
    host = host or os.environ.get("KITSU_HOST")
    if not host:
        raise ValueError("no Kitsu host: pass host= or set KITSU_HOST")
    return {
        "host": host,
        "token": token or os.environ.get("KITSU_TOKEN") or None,
    }


class PyKitsu(_Groups, _AuthMixin[SyncTransport]):
    """Synchronous Kitsu client.

    Example::

        from pykitsu import PyKitsu

        with PyKitsu("https://kitsu.example.com") as k:
            k.login("me@example.com", password)  # the password is not kept
            for project in k.projects.get_open_projects():
                print(project.name)

    Args:
        host: Kitsu URL. ``/api`` is added when missing.
        token: Access token (a bot token, or one from a previous login).
        refresh_token: Refresh token. When set, an expired access token is
            refreshed once and the request retried.
        timeout: Seconds, or an ``httpx.Timeout``. Defaults to 30 s (300 s read).
        verify: TLS verification, as in httpx.
        headers: Extra headers sent with every request.
        validate_responses: Parse responses into models (default). With
            ``False`` methods return the decoded JSON as-is.
        http_client: Use your own ``httpx.Client`` (proxies, retries…).
        token_folder: Folder where the tokens are saved (``kitsu_token.json``)
            after each login and refresh, and removed at logout. A later client
            built with the same folder can call :meth:`reconnect`.

    Auth events: see :meth:`add_login_callback` and :meth:`add_logout_callback`.
    """

    def __init__(
        self,
        host: str,
        *,
        token: str | None = None,
        refresh_token: str | None = None,
        timeout: float | httpx.Timeout | None = None,
        verify: bool | str = True,
        headers: Mapping[str, str] | None = None,
        validate_responses: bool = True,
        http_client: httpx.Client | None = None,
        token_folder: str | os.PathLike[str] | None = None,
    ) -> None:
        self._transport = SyncTransport(
            host,
            token=token,
            refresh_token=refresh_token,
            timeout=timeout,
            verify=verify,
            headers=headers,
            validate_responses=validate_responses,
            http_client=http_client,
        )
        self._groups: dict[str, Any] = {}
        self._init_auth(token_folder)
        self._transport.on_login = self._on_login

    @classmethod
    def from_env(
        cls,
        host: str | None = None,
        *,
        token: str | None = None,
        **kwargs: Any,
    ) -> Self:
        """Build a client from ``KITSU_HOST`` and, if set, ``KITSU_TOKEN``."""
        return cls(**_env(host, token), **kwargs)

    # -- auth
    @property
    def host(self) -> str:
        """API root URL, ending with ``/api``."""
        return self._transport.base_url

    @property
    def token(self) -> str | None:
        """Current access token."""
        return self._transport.token

    @token.setter
    def token(self, value: str | None) -> None:
        self._transport.token = value

    @property
    def refresh_token(self) -> str | None:
        return self._transport.refresh_token

    def login(self, email: str, password: str, *, totp: str | None = None, **extra: Any) -> dict[str, Any]:
        """Log in and keep the tokens for the next requests. Returns the login response.

        The password is only sent in this request: the client never stores it.
        Saves the tokens in the token folder (if any) and calls the login callbacks.
        """
        return self._transport.login(email, password, totp=totp, **extra)

    def reconnect(self) -> dict[str, Any] | None:
        """Authenticate with the tokens saved in the token folder. Returns the user.

        The saved token is checked against the server (and refreshed if it
        expired and a refresh token was saved). On success the login callbacks
        are called.

        Raises:
            KitsuError: no token folder, or no saved token for this host
                (see :meth:`can_reconnect`).
            AuthenticationError: the saved token was rejected; the saved file
                is removed, so :meth:`can_reconnect` becomes ``False``.
        """
        self._use_saved_tokens()
        try:
            data = self._transport.request("GET", "/auth/authenticated")
        except KitsuAPIError as exc:
            if exc.status_code in _INVALID_TOKEN_STATUSES:
                self._drop_saved_session()
            raise
        self._on_login(data)
        return self.current_user

    def logout(self) -> None:
        """Revoke the tokens on the server, forget them and remove the saved file.

        Local logout always happens, even when the server cannot be reached.
        The logout callbacks are called when a session was open.
        """
        if self._transport.token:
            try:
                self._transport.request("GET", "/auth/logout")
            except (KitsuAPIError, httpx.HTTPError) as exc:
                logger.warning("pykitsu: server logout failed, logging out locally: %s", exc)
        if self._forget_session():
            self._fire(self._logout_callbacks)

    def _on_login(self, data: Any) -> None:
        self._set_user_from(data)
        self._fire(self._login_callbacks)

    def _fire(self, callbacks: list[Any]) -> None:
        for pending in self._run_callbacks(callbacks):
            logger.warning("pykitsu: async callback ignored by the sync PyKitsu client: %r", pending)
            close = getattr(pending, "close", None)
            if callable(close):
                close()

    # -- escape hatch
    def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        raw: bool = False,
    ) -> Any:
        """Call any route, e.g. ``k.request("GET", "/data/projects/open")``. Returns decoded JSON."""
        return self._transport.request(method, path, params=params, json=json, raw=raw)

    @property
    def http(self) -> httpx.Client:
        """The underlying ``httpx.Client``."""
        return self._transport.http

    # -- lifecycle
    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        self.close()

    def __dir__(self) -> list[str]:
        return sorted(set(super().__dir__()) | set(GROUP_NAMES))

    def __repr__(self) -> str:
        return f"PyKitsu({self.host!r})"


class AsyncPyKitsu(_AsyncGroups, _AuthMixin[AsyncTransport]):
    """Asynchronous Kitsu client. Same arguments as :class:`PyKitsu`.

    Example::

        async with AsyncPyKitsu.from_env() as k:
            shots = await k.shots.get_shots_of_project(project_id)
    """

    def __init__(
        self,
        host: str,
        *,
        token: str | None = None,
        refresh_token: str | None = None,
        timeout: float | httpx.Timeout | None = None,
        verify: bool | str = True,
        headers: Mapping[str, str] | None = None,
        validate_responses: bool = True,
        http_client: httpx.AsyncClient | None = None,
        token_folder: str | os.PathLike[str] | None = None,
    ) -> None:
        self._transport = AsyncTransport(
            host,
            token=token,
            refresh_token=refresh_token,
            timeout=timeout,
            verify=verify,
            headers=headers,
            validate_responses=validate_responses,
            http_client=http_client,
        )
        self._groups: dict[str, Any] = {}
        self._init_auth(token_folder)
        self._transport.on_login = self._on_login

    @classmethod
    def from_env(
        cls,
        host: str | None = None,
        *,
        token: str | None = None,
        **kwargs: Any,
    ) -> Self:
        """Build a client from ``KITSU_HOST`` and, if set, ``KITSU_TOKEN``."""
        return cls(**_env(host, token), **kwargs)

    @property
    def host(self) -> str:
        return self._transport.base_url

    @property
    def token(self) -> str | None:
        return self._transport.token

    @token.setter
    def token(self, value: str | None) -> None:
        self._transport.token = value

    @property
    def refresh_token(self) -> str | None:
        return self._transport.refresh_token

    async def login(
        self, email: str, password: str, *, totp: str | None = None, **extra: Any
    ) -> dict[str, Any]:
        """Log in and keep the tokens for the next requests. Returns the login response.

        The password is only sent in this request: the client never stores it.
        Saves the tokens in the token folder (if any) and calls the login callbacks.
        """
        return await self._transport.login(email, password, totp=totp, **extra)

    async def reconnect(self) -> dict[str, Any] | None:
        """Authenticate with the tokens saved in the token folder. See :meth:`PyKitsu.reconnect`."""
        self._use_saved_tokens()
        try:
            data = await self._transport.request("GET", "/auth/authenticated")
        except KitsuAPIError as exc:
            if exc.status_code in _INVALID_TOKEN_STATUSES:
                self._drop_saved_session()
            raise
        await self._on_login(data)
        return self.current_user

    async def logout(self) -> None:
        """Revoke the tokens on the server, forget them and remove the saved file. See :meth:`PyKitsu.logout`."""
        if self._transport.token:
            try:
                await self._transport.request("GET", "/auth/logout")
            except (KitsuAPIError, httpx.HTTPError) as exc:
                logger.warning("pykitsu: server logout failed, logging out locally: %s", exc)
        if self._forget_session():
            await self._fire(self._logout_callbacks)

    async def _on_login(self, data: Any) -> None:
        self._set_user_from(data)
        await self._fire(self._login_callbacks)

    async def _fire(self, callbacks: list[Any]) -> None:
        for pending in self._run_callbacks(callbacks):
            try:
                await pending
            except Exception:
                logger.exception("pykitsu: error in auth callback")

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        raw: bool = False,
    ) -> Any:
        """Call any route. Returns decoded JSON."""
        return await self._transport.request(method, path, params=params, json=json, raw=raw)

    @property
    def http(self) -> httpx.AsyncClient:
        return self._transport.http

    async def close(self) -> None:
        await self._transport.close()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        await self.close()

    def __dir__(self) -> list[str]:
        return sorted(set(super().__dir__()) | set(GROUP_NAMES))

    def __repr__(self) -> str:
        return f"AsyncPyKitsu({self.host!r})"
