"""HTTP layer shared by the generated groups.

Request building and response decoding are shared; only the sending differs
between :class:`SyncTransport` and :class:`AsyncTransport`.
"""

from __future__ import annotations

import functools
import inspect
import json as _json
import mimetypes
import os
from collections.abc import Callable, Iterator, Mapping
from contextlib import ExitStack, contextmanager
from datetime import date, datetime
from enum import Enum
from pathlib import Path
from typing import IO, Any, Union
from urllib.parse import quote

import httpx

from .errors import ResponseValidationError, error_for

__all__ = ["AsyncTransport", "FileInput", "SyncTransport", "normalize_host"]

FileInput = Union[str, os.PathLike[str], bytes, IO[bytes]]
"""A file to upload: a path, raw bytes or an open binary file."""

_AUTH_PATHS = ("/auth/login", "/auth/refresh-token", "/auth/logout")
_DEFAULT_TIMEOUT = httpx.Timeout(30.0, read=300.0)


def normalize_host(host: str) -> str:
    """``https://kitsu.example.com`` → ``https://kitsu.example.com/api``."""
    host = host.strip().rstrip("/")
    if not host.startswith(("http://", "https://")):
        host = "https://" + host
    if not host.endswith("/api"):
        host += "/api"
    return host


# --------------------------------------------------------------------------- encoding


def to_jsonable(value: Any) -> Any:
    """Convert models, dates and containers to JSON-compatible values."""
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    model_dump = getattr(value, "model_dump", None)
    if callable(model_dump):
        return model_dump(mode="json", by_alias=True, exclude_none=True)
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, Enum):
        return to_jsonable(value.value)
    if isinstance(value, Mapping):
        return {str(k): to_jsonable(v) for k, v in value.items()}  # pyright: ignore[reportUnknownVariableType]
    if isinstance(value, (list, tuple, set, frozenset)):
        return [to_jsonable(v) for v in value]  # pyright: ignore[reportUnknownVariableType]
    if isinstance(value, os.PathLike):
        return os.fspath(value)  # pyright: ignore[reportUnknownArgumentType]
    return value


def _query_value(value: Any) -> Any:
    if isinstance(value, (list, tuple)):
        return [_query_value(v) for v in value]  # pyright: ignore[reportUnknownVariableType]
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    return value


def _form_value(value: Any) -> str:
    value = to_jsonable(value)
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (dict, list)):
        return _json.dumps(value)
    return str(value)


def _merge_body(body: Mapping[str, Any] | None, extra: Mapping[str, Any] | None) -> dict[str, Any]:
    out = {k: v for k, v in (body or {}).items() if v is not None}
    if extra:
        out.update(extra)
    return out


@contextmanager
def _open_files(files: Mapping[str, Any] | None) -> Iterator[list[tuple[str, Any]]]:
    """Yield httpx ``files`` tuples, closing the files we opened."""
    out: list[tuple[str, Any]] = []
    with ExitStack() as stack:
        for field, value in (files or {}).items():
            if value is None:
                continue
            values: list[Any] = list(value) if isinstance(value, (list, tuple)) else [value]  # pyright: ignore[reportUnknownArgumentType]
            for v in values:
                if isinstance(v, (str, os.PathLike)):
                    path = Path(v)  # pyright: ignore[reportUnknownArgumentType]
                    fh = stack.enter_context(path.open("rb"))
                    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
                    out.append((field, (path.name, fh, mime)))
                elif isinstance(v, (bytes, bytearray)):
                    out.append((field, (field, bytes(v), "application/octet-stream")))  # pyright: ignore[reportUnknownArgumentType]
                else:
                    name = os.path.basename(str(getattr(v, "name", field)))
                    mime = mimetypes.guess_type(name)[0] or "application/octet-stream"
                    out.append((field, (name, v, mime)))
        yield out


@functools.lru_cache(maxsize=1024)
def _adapter(tp: Any) -> Any:
    from pydantic import TypeAdapter

    return TypeAdapter(tp)


# --------------------------------------------------------------------------- transports


class _BaseTransport:
    def __init__(
        self,
        base_url: str,
        *,
        token: str | None,
        refresh_token: str | None,
        validate_responses: bool,
    ) -> None:
        self.base_url = normalize_host(base_url)
        self.token = token
        self.refresh_token = refresh_token
        self.validate_responses = validate_responses
        # Hooks set by the client: tokens were stored (login/refresh), a login succeeded.
        self.on_tokens_changed: Callable[[], None] | None = None
        self.on_login: Callable[[Any], Any] | None = None

    # -- request building
    def _url(self, path: str, path_params: Mapping[str, Any] | None) -> str:
        if path_params:
            path = path.format(**{k: quote(str(v), safe="") for k, v in path_params.items()})
        return path

    def _headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def _build(
        self,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, Any] | None,
        params: Mapping[str, Any] | None,
        json: Any,
        body: Mapping[str, Any] | None,
        extra_body: Mapping[str, Any] | None,
        files: list[tuple[str, Any]],
        body_mode: str | None,
    ) -> dict[str, Any]:
        kwargs: dict[str, Any] = {
            "method": method,
            "url": self._url(path, path_params),
            "headers": self._headers(),
        }
        if params:
            q = {k: _query_value(v) for k, v in params.items() if v is not None}
            if q:
                kwargs["params"] = q
        if json is not None:
            kwargs["json"] = to_jsonable(json)
        if body_mode is not None:
            payload = _merge_body(body, extra_body)
            use_multipart = body_mode == "multipart" or (body_mode == "json_or_multipart" and files)
            if use_multipart:
                kwargs["data"] = {k: _form_value(v) for k, v in payload.items()}
                kwargs["files"] = files
            elif body_mode == "form":
                kwargs["data"] = {k: _form_value(v) for k, v in payload.items()}
            else:
                kwargs["json"] = to_jsonable(payload)
        return kwargs

    # -- response decoding
    def _decode(self, response: httpx.Response, response_type: Any) -> Any:
        if not response.content or response.status_code == 204:
            return None
        ctype = response.headers.get("content-type", "")
        if "json" not in ctype:
            try:
                data: Any = response.json()
            except ValueError:
                return response.text
        else:
            data = response.json()
        if response_type is None or not self.validate_responses:
            return data
        from pydantic import ValidationError

        try:
            return _adapter(response_type).validate_python(data)
        except ValidationError as exc:
            raise ResponseValidationError(
                f"{response.request.method} {response.request.url}: response does not match "
                f"{getattr(response_type, '__name__', response_type)}: {exc}",
                raw=data,
            ) from exc

    def _should_refresh(self, response: httpx.Response, path: str, retried: bool) -> bool:
        return (
            response.status_code == 401
            and not retried
            and self.refresh_token is not None
            and not path.startswith(_AUTH_PATHS)
        )

    def _store_login(self, data: Any) -> Any:
        if isinstance(data, dict):
            before = (self.token, self.refresh_token)
            self.token = data.get("access_token") or self.token  # pyright: ignore[reportUnknownMemberType]
            self.refresh_token = data.get("refresh_token") or self.refresh_token  # pyright: ignore[reportUnknownMemberType]
            if (self.token, self.refresh_token) != before and self.on_tokens_changed is not None:
                self.on_tokens_changed()
        return data  # pyright: ignore[reportUnknownVariableType]

    def forget(self) -> None:
        """Drop the tokens."""
        self.token = self.refresh_token = None

    @staticmethod
    def _login_body(email: str, password: str, extra: Mapping[str, Any]) -> dict[str, Any]:
        return {"email": email, "password": password, **{k: v for k, v in extra.items() if v is not None}}


class SyncTransport(_BaseTransport):
    def __init__(
        self,
        base_url: str,
        *,
        token: str | None = None,
        refresh_token: str | None = None,
        timeout: float | httpx.Timeout | None = None,
        verify: bool | str = True,
        headers: Mapping[str, str] | None = None,
        validate_responses: bool = True,
        http_client: httpx.Client | None = None,
    ) -> None:
        super().__init__(
            base_url,
            token=token,
            refresh_token=refresh_token,
            validate_responses=validate_responses,
        )
        self.http = http_client or httpx.Client(
            base_url=self.base_url,
            timeout=timeout if timeout is not None else _DEFAULT_TIMEOUT,
            verify=verify,
            headers=dict(headers or {}),
            follow_redirects=True,
        )
        if http_client is not None:
            self.http.base_url = httpx.URL(self.base_url)

    def close(self) -> None:
        self.http.close()

    def login(self, email: str, password: str, **extra: Any) -> Any:
        r = self.http.post("/auth/login", json=self._login_body(email, password, extra))
        if r.is_error:
            raise error_for(r)
        data = self._store_login(r.json())
        if self.on_login is not None:
            self.on_login(data)
        return data

    def refresh(self) -> None:
        r = self.http.get("/auth/refresh-token", headers={"Authorization": f"Bearer {self.refresh_token}"})
        if r.is_error:
            raise error_for(r)
        self._store_login(r.json())

    def request(
        self,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        body: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        files: Mapping[str, Any] | None = None,
        body_mode: str | None = None,
        response_type: Any = None,
        binary: bool = False,
        dest: str | os.PathLike[str] | None = None,
        raw: bool = False,
    ) -> Any:
        retried = False
        while True:
            with _open_files(files) as opened:
                kwargs = self._build(
                    method,
                    path,
                    path_params=path_params,
                    params=params,
                    json=json,
                    body=body,
                    extra_body=extra_body,
                    files=opened,
                    body_mode=body_mode,
                )
                if binary and dest is not None:
                    with self.http.stream(**kwargs) as r:
                        if self._should_refresh(r, path, retried):
                            retried = True
                            self.refresh()
                            continue
                        if r.is_error:
                            r.read()
                            raise error_for(r)
                        target = Path(dest)
                        target.parent.mkdir(parents=True, exist_ok=True)
                        with target.open("wb") as fh:
                            for chunk in r.iter_bytes():
                                fh.write(chunk)
                        return target
                r = self.http.request(**kwargs)
            if self._should_refresh(r, path, retried):
                retried = True
                self.refresh()
                continue
            if raw:
                return r
            if r.is_error:
                raise error_for(r)
            if binary:
                return r.content
            return self._decode(r, response_type)


class AsyncTransport(_BaseTransport):
    def __init__(
        self,
        base_url: str,
        *,
        token: str | None = None,
        refresh_token: str | None = None,
        timeout: float | httpx.Timeout | None = None,
        verify: bool | str = True,
        headers: Mapping[str, str] | None = None,
        validate_responses: bool = True,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        super().__init__(
            base_url,
            token=token,
            refresh_token=refresh_token,
            validate_responses=validate_responses,
        )
        self.http = http_client or httpx.AsyncClient(
            base_url=self.base_url,
            timeout=timeout if timeout is not None else _DEFAULT_TIMEOUT,
            verify=verify,
            headers=dict(headers or {}),
            follow_redirects=True,
        )
        if http_client is not None:
            self.http.base_url = httpx.URL(self.base_url)

    async def close(self) -> None:
        await self.http.aclose()

    async def login(self, email: str, password: str, **extra: Any) -> Any:
        r = await self.http.post("/auth/login", json=self._login_body(email, password, extra))
        if r.is_error:
            raise error_for(r)
        data = self._store_login(r.json())
        if self.on_login is not None:
            result = self.on_login(data)
            if inspect.isawaitable(result):
                await result
        return data

    async def refresh(self) -> None:
        r = await self.http.get(
            "/auth/refresh-token", headers={"Authorization": f"Bearer {self.refresh_token}"}
        )
        if r.is_error:
            raise error_for(r)
        self._store_login(r.json())

    async def request(
        self,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, Any] | None = None,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        body: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        files: Mapping[str, Any] | None = None,
        body_mode: str | None = None,
        response_type: Any = None,
        binary: bool = False,
        dest: str | os.PathLike[str] | None = None,
        raw: bool = False,
    ) -> Any:
        retried = False
        while True:
            # File reads stay synchronous: uploads are rare and httpx needs sync files here.
            with _open_files(files) as opened:
                kwargs = self._build(
                    method,
                    path,
                    path_params=path_params,
                    params=params,
                    json=json,
                    body=body,
                    extra_body=extra_body,
                    files=opened,
                    body_mode=body_mode,
                )
                if opened:
                    # httpx's async client cannot stream sync file objects: read them now.
                    kwargs["files"] = [
                        (f, (n, c.read() if hasattr(c, "read") else c, m)) for f, (n, c, m) in opened
                    ]
                if binary and dest is not None:
                    async with self.http.stream(**kwargs) as r:
                        if self._should_refresh(r, path, retried):
                            retried = True
                            await self.refresh()
                            continue
                        if r.is_error:
                            await r.aread()
                            raise error_for(r)
                        target = Path(dest)
                        target.parent.mkdir(parents=True, exist_ok=True)
                        with target.open("wb") as fh:
                            async for chunk in r.aiter_bytes():
                                fh.write(chunk)
                        return target
                r = await self.http.request(**kwargs)
            if self._should_refresh(r, path, retried):
                retried = True
                await self.refresh()
                continue
            if raw:
                return r
            if r.is_error:
                raise error_for(r)
            if binary:
                return r.content
            return self._decode(r, response_type)
