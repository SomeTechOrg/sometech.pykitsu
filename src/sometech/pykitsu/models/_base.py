"""Base class of every generated model."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, ValidationError, ValidatorFunctionWrapHandler, field_validator


class KitsuModel(BaseModel):
    """Lenient pydantic model.

    * Keys the spec does not know are kept (see ``model_extra``).
    * A field whose value does not match its declared type keeps the raw value
      instead of failing the whole response: the spec documents the API, it does
      not enforce it, and a typo there should not break your tools.
    """

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
        protected_namespaces=(),
        arbitrary_types_allowed=True,
    )

    @field_validator("*", mode="wrap")
    @classmethod
    def _lenient(cls, value: Any, handler: ValidatorFunctionWrapHandler) -> Any:
        try:
            return handler(value)
        except ValidationError:
            return value

    def __getitem__(self, key: str) -> Any:
        """``shot["name"]`` works like with gazu dicts (fields and extra keys)."""
        name = _alias_to_field(type(self)).get(key, key)
        if name in type(self).model_fields:
            return getattr(self, name)
        extra = self.model_extra or {}
        if key in extra:
            return extra[key]
        raise KeyError(key)

    def get(self, key: str, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def to_dict(self) -> dict[str, Any]:
        """Plain JSON-compatible dict with the API key names."""
        return self.model_dump(mode="json", by_alias=True, exclude_none=True)


_ALIASES: dict[type[BaseModel], dict[str, str]] = {}


def _alias_to_field(cls: type[BaseModel]) -> dict[str, str]:
    table = _ALIASES.get(cls)
    if table is None:
        table = {f.alias or name: name for name, f in cls.model_fields.items()}
        _ALIASES[cls] = table
    return table
