"""Authentication events and token persistence shared by both clients."""

from __future__ import annotations

import contextlib
import inspect
import json
import logging
import os
import tempfile
import time
from collections.abc import Callable
from pathlib import Path
from typing import TYPE_CHECKING, Any, Generic, TypeVar

from typing_extensions import Self

from .errors import KitsuError

if TYPE_CHECKING:
    from ._transport import _BaseTransport

__all__ = ["TOKEN_FILENAME", "TokenStore"]

logger = logging.getLogger("pykitsu")

TOKEN_FILENAME = "kitsu_token.json"


class TokenStore:
    """The JSON file in ``folder`` that holds the tokens of one Kitsu host.

    The file contains the host, the access and refresh tokens and the date of
    the save. It is written atomically and readable by the owner only.
    """

    def __init__(self, folder: str | os.PathLike[str]) -> None:
        self.folder = Path(folder).expanduser()
        self.path = self.folder / TOKEN_FILENAME

    def load(self, host: str) -> dict[str, Any] | None:
        """Saved tokens for ``host``, or ``None`` (no file, bad file, other host)."""
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return None
        if not isinstance(data, dict) or data.get("host") != host or not data.get("access_token"):
            return None
        return data  # pyright: ignore[reportUnknownVariableType]

    def save(self, host: str, access_token: str, refresh_token: str | None) -> None:
        self.folder.mkdir(parents=True, exist_ok=True)
        payload = {
            "host": host,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "saved_at": time.time(),
        }
        fd, tmp = tempfile.mkstemp(dir=self.folder, prefix=".kitsu_token.", suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, indent=1)
            os.chmod(tmp, 0o600)
            os.replace(tmp, self.path)
        except BaseException:
            with contextlib.suppress(OSError):
                os.unlink(tmp)
            raise

    def clear(self) -> None:
        with contextlib.suppress(OSError):
            self.path.unlink()


_T = TypeVar("_T", bound="_BaseTransport")


class _AuthMixin(Generic[_T]):
    """Login/logout callbacks, current user and saved-token handling."""

    _transport: _T

    def _init_auth(self, token_folder: str | os.PathLike[str] | None) -> None:
        self._token_store = TokenStore(token_folder) if token_folder is not None else None
        self._login_callbacks: list[Callable[[Any], object]] = []
        self._logout_callbacks: list[Callable[[Any], object]] = []
        self._user: dict[str, Any] | None = None
        self._transport.on_tokens_changed = self._save_tokens

    # -- callbacks
    def add_login_callback(self, callback: Callable[[Self], object]) -> Callable[[Self], object]:
        """Call ``callback(client)`` each time the client authenticates.

        That is after :meth:`login` and after :meth:`reconnect`.
        ``client.current_user`` holds the logged-in person at that moment. On
        :class:`AsyncPyKitsu` the callback may be a coroutine function.

        Callbacks run in the thread that made the request; in a GUI, forward
        to the UI thread (e.g. with a Qt signal). An exception raised by a
        callback is logged and does not stop the others.

        Returns ``callback``, so it can be used as a decorator.
        """
        self._login_callbacks.append(callback)
        return callback

    def remove_login_callback(self, callback: Callable[[Self], object]) -> None:
        """Remove a callback added with :meth:`add_login_callback` (no error if absent)."""
        with contextlib.suppress(ValueError):
            self._login_callbacks.remove(callback)

    def add_logout_callback(self, callback: Callable[[Self], object]) -> Callable[[Self], object]:
        """Call ``callback(client)`` each time :meth:`logout` ends an authenticated session.

        Same rules as :meth:`add_login_callback`. Returns ``callback``.
        """
        self._logout_callbacks.append(callback)
        return callback

    def remove_logout_callback(self, callback: Callable[[Self], object]) -> None:
        """Remove a callback added with :meth:`add_logout_callback` (no error if absent)."""
        with contextlib.suppress(ValueError):
            self._logout_callbacks.remove(callback)

    def _run_callbacks(self, callbacks: list[Callable[[Any], object]]) -> list[Any]:
        """Call each callback, return the awaitables they gave (async callbacks)."""
        pending: list[Any] = []
        for cb in list(callbacks):
            try:
                result = cb(self)
            except Exception:
                logger.exception("pykitsu: error in auth callback %r", cb)
                continue
            if inspect.isawaitable(result):
                pending.append(result)
        return pending

    # -- state
    @property
    def current_user(self) -> dict[str, Any] | None:
        """The logged-in person (from the login or reconnect response), or ``None``."""
        return self._user

    @property
    def token_folder(self) -> Path | None:
        """Folder where the tokens are saved, or ``None``."""
        return self._token_store.folder if self._token_store else None

    @property
    def token_file(self) -> Path | None:
        """JSON file holding the saved tokens, or ``None`` without a token folder."""
        return self._token_store.path if self._token_store else None

    def can_reconnect(self) -> bool:
        """``True`` when the token folder has saved tokens for this host.

        It only reads the file: the token may still be expired or revoked,
        which :meth:`reconnect` finds out.
        """
        return self._token_store is not None and self._token_store.load(self._transport.base_url) is not None

    # -- internals
    def _save_tokens(self) -> None:
        t = self._transport
        if self._token_store is None or not t.token:
            return
        try:
            self._token_store.save(t.base_url, t.token, t.refresh_token)
        except OSError:
            logger.exception("pykitsu: cannot save the tokens in %s", self._token_store.path)

    def _set_user_from(self, data: Any) -> None:
        user = data.get("user") if isinstance(data, dict) else None
        self._user = user if isinstance(user, dict) else None  # pyright: ignore[reportUnknownMemberType]

    def _use_saved_tokens(self) -> None:
        if self._token_store is None:
            raise KitsuError("cannot reconnect: the client has no token_folder")
        saved = self._token_store.load(self._transport.base_url)
        if saved is None:
            raise KitsuError(
                f"cannot reconnect: no saved token for {self._transport.base_url} in {self._token_store.folder}"
            )
        self._transport.token = saved["access_token"]
        self._transport.refresh_token = saved.get("refresh_token") or None

    def _drop_saved_session(self) -> None:
        """The saved tokens were rejected: forget them and the saved file."""
        self._transport.token = self._transport.refresh_token = None
        if self._token_store is not None:
            self._token_store.clear()

    def _forget_session(self) -> bool:
        """Drop tokens, user and saved file. Return whether a session existed."""
        had_session = self._transport.token is not None or self._user is not None
        self._transport.forget()
        self._user = None
        if self._token_store is not None:
            self._token_store.clear()
        return had_session
