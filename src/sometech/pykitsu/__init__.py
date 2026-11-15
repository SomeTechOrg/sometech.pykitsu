"""Typed client for the Kitsu production tracker API.

Importing this package does not import any API group or model: they load on
first use (``client.shots``, ``from pykitsu.models import Shot``).
"""

from ._client import AsyncPyKitsu, PyKitsu
from ._spec_version import SPEC_VERSION
from ._transport import FileInput
from .errors import (
    AuthenticationError,
    BadRequestError,
    ConflictError,
    KitsuAPIError,
    KitsuError,
    NotFoundError,
    PermissionDeniedError,
    ResponseValidationError,
    ServerError,
)

__version__ = "0.1.0"

__all__ = [
    "SPEC_VERSION",
    "AsyncPyKitsu",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "FileInput",
    "KitsuAPIError",
    "KitsuError",
    "NotFoundError",
    "PermissionDeniedError",
    "PyKitsu",
    "ResponseValidationError",
    "ServerError",
]
