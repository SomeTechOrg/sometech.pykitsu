"""Every generated group imports, and sync/async APIs match."""

import inspect

import pytest

from pykitsu import AsyncPyKitsu, PyKitsu
from pykitsu._groups import GROUP_NAMES


def public_methods(obj: object) -> dict[str, inspect.Signature]:
    return {
        name: inspect.signature(getattr(obj, name))
        for name in dir(obj)
        if not name.startswith("_") and callable(getattr(obj, name))
    }


@pytest.mark.parametrize("group", GROUP_NAMES)
def test_group_imports_and_matches_async(group: str) -> None:
    sync = getattr(PyKitsu("http://kitsu.test"), group)
    asyn = getattr(AsyncPyKitsu("http://kitsu.test"), group)
    s, a = public_methods(sync), public_methods(asyn)
    assert s, f"{group} has no method"
    assert s.keys() == a.keys()
    for name in s:
        assert inspect.iscoroutinefunction(getattr(asyn, name)), name
        assert str(s[name]) == str(a[name]), name


def test_total_operation_count() -> None:
    k = PyKitsu("http://kitsu.test")
    assert sum(len(public_methods(getattr(k, g))) for g in GROUP_NAMES) == 811
