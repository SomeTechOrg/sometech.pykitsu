"""Exceptions raised by pykitsu."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import httpx

__all__ = [
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "KitsuAPIError",
    "KitsuError",
    "NotFoundError",
    "PermissionDeniedError",
    "ResponseValidationError",
    "ServerError",
]


class KitsuError(Exception):
    """Base class of every pykitsu error."""


class KitsuAPIError(KitsuError):
    """The Kitsu API answered with an error status."""

    def __init__(self, message: str, *, response: httpx.Response, body: Any = None) -> None:
        super().__init__(message)
        self.message = message
        self.response = response
        self.status_code = response.status_code
        self.body = body

    def __str__(self) -> str:
        req = self.response.request
        return f"{self.status_code} {req.method} {req.url}: {self.message}"


class BadRequestError(KitsuAPIError):
    """400: the request is not valid."""


class AuthenticationError(KitsuAPIError):
    """401: missing, invalid or expired token."""


class PermissionDeniedError(KitsuAPIError):
    """403: the user cannot do this action."""


class NotFoundError(KitsuAPIError):
    """404: the resource does not exist."""


class ConflictError(KitsuAPIError):
    """409: the resource already exists or is in a conflicting state."""


class ServerError(KitsuAPIError):
    """5xx: the Kitsu server failed."""


class ResponseValidationError(KitsuError):
    """The response does not have the shape the spec announces.

    ``raw`` holds the decoded JSON so that you can still use it.
    """

    def __init__(self, message: str, *, raw: Any) -> None:
        super().__init__(message)
        self.raw = raw


_BY_STATUS: dict[int, type[KitsuAPIError]] = {
    400: BadRequestError,
    401: AuthenticationError,
    403: PermissionDeniedError,
    404: NotFoundError,
    409: ConflictError,
}


def error_for(response: httpx.Response) -> KitsuAPIError:
    try:
        body: Any = response.json()
    except ValueError:
        body = response.text
    message = ""
    if isinstance(body, dict):
        message = str(body.get("message") or body.get("error") or body.get("msg") or "")
    if not message:
        message = (body if isinstance(body, str) else "") or response.reason_phrase
    if response.status_code == 401 and "authorization" not in response.request.headers:
        message = f"{message} (not logged in: call login() or reconnect(), or pass token=)"
    cls = _BY_STATUS.get(response.status_code)
    if cls is None:
        cls = ServerError if response.status_code >= 500 else KitsuAPIError
    return cls(message[:1000], response=response, body=body)
