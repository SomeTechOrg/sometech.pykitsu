"""Login/logout callbacks, token folder and reconnect."""

import json
import logging
import stat
from collections.abc import Iterator
from pathlib import Path

import httpx
import pytest
import respx

from pykitsu import AsyncPyKitsu, AuthenticationError, KitsuError, PyKitsu

API = "https://kitsu.test/api"
USER = {"id": "u1", "full_name": "Jane Doe"}
LOGIN = {"login": True, "user": USER, "access_token": "a1", "refresh_token": "r1"}


@pytest.fixture
def mock() -> Iterator[respx.MockRouter]:
    with respx.mock(base_url=API, assert_all_called=False) as router:
        router.post("/auth/login").respond(json=LOGIN)
        router.get("/auth/logout").respond(json={"logout": True})
        router.get("/auth/authenticated", name="authenticated").respond(
            json={"authenticated": True, "user": USER}
        )
        yield router


def saved(folder: Path) -> dict[str, object]:
    return json.loads((folder / "kitsu_token.json").read_text())


def test_login_and_logout_callbacks(mock: respx.MockRouter) -> None:
    events: list[tuple[str, object]] = []
    k = PyKitsu("kitsu.test")
    k.add_login_callback(lambda c: events.append(("login", c.current_user)))
    k.add_logout_callback(lambda c: events.append(("logout", c.current_user)))

    k.login("jane@x.com", "pw")
    assert events == [("login", USER)]
    assert k.current_user == USER

    k.logout()
    assert events[-1] == ("logout", None)
    assert k.token is None and k.current_user is None

    k.logout()  # nothing open: no second event
    assert len(events) == 2


def test_remove_callback_and_decorator(mock: respx.MockRouter) -> None:
    k = PyKitsu("kitsu.test")
    calls: list[str] = []

    @k.add_login_callback
    def on_login(client: PyKitsu) -> None:
        calls.append("x")

    k.remove_login_callback(on_login)
    k.remove_login_callback(on_login)  # absent: no error
    k.login("jane@x.com", "pw")
    assert calls == []


def test_failing_callback_does_not_break_login(
    mock: respx.MockRouter, caplog: pytest.LogCaptureFixture
) -> None:
    k = PyKitsu("kitsu.test")
    calls: list[str] = []

    def boom(_: PyKitsu) -> None:
        raise RuntimeError("ui bug")

    k.add_login_callback(boom)
    k.add_login_callback(lambda _: calls.append("ok"))
    with caplog.at_level(logging.ERROR, logger="pykitsu"):
        k.login("jane@x.com", "pw")
    assert calls == ["ok"] and k.token == "a1"
    assert "ui bug" in caplog.text


def test_logout_is_local_when_server_fails(mock: respx.MockRouter, tmp_path: Path) -> None:
    mock.get("/auth/logout").mock(side_effect=httpx.ConnectError("offline"))
    k = PyKitsu("kitsu.test", token_folder=tmp_path)
    k.login("jane@x.com", "pw")
    out: list[str] = []
    k.add_logout_callback(lambda _: out.append("bye"))
    k.logout()
    assert out == ["bye"] and k.token is None and not k.can_reconnect()


def test_requests_after_logout_are_unauthenticated(mock: respx.MockRouter) -> None:
    k = PyKitsu("kitsu.test")
    k.login("jane@x.com", "pw")
    k.logout()
    route = mock.get("/data/projects/open").respond(401)
    with pytest.raises(AuthenticationError):
        k.projects.get_open_projects()
    assert "Authorization" not in route.calls.last.request.headers


# --------------------------------------------------------------------------- token folder


def test_can_reconnect_without_folder_or_token(tmp_path: Path) -> None:
    assert PyKitsu("kitsu.test").can_reconnect() is False
    assert PyKitsu("kitsu.test", token_folder=tmp_path / "missing").can_reconnect() is False
    assert PyKitsu("kitsu.test", token_folder=tmp_path).can_reconnect() is False  # empty folder
    with pytest.raises(KitsuError):
        PyKitsu("kitsu.test").reconnect()
    with pytest.raises(KitsuError):
        PyKitsu("kitsu.test", token_folder=tmp_path).reconnect()


def test_login_saves_token_and_reconnect_uses_it(mock: respx.MockRouter, tmp_path: Path) -> None:
    folder = tmp_path / "auth"
    with PyKitsu("kitsu.test", token_folder=folder) as k:
        k.login("jane@x.com", "pw")
    data = saved(folder)
    assert data["host"] == API and data["access_token"] == "a1" and data["refresh_token"] == "r1"
    assert stat.S_IMODE((folder / "kitsu_token.json").stat().st_mode) == 0o600

    # later, in another process / session
    k2 = PyKitsu("kitsu.test", token_folder=folder)
    assert k2.can_reconnect()
    events: list[object] = []
    k2.add_login_callback(lambda c: events.append(c.current_user))
    assert k2.reconnect() == USER
    assert events == [USER] and k2.token == "a1"
    assert mock["authenticated"].calls.last.request.headers["Authorization"] == "Bearer a1"
    # logout removes the saved token
    k2.logout()
    assert not (folder / "kitsu_token.json").exists() and not k2.can_reconnect()


def test_saved_token_is_per_host(mock: respx.MockRouter, tmp_path: Path) -> None:
    PyKitsu("kitsu.test", token_folder=tmp_path).login("jane@x.com", "pw")
    assert PyKitsu("other.test", token_folder=tmp_path).can_reconnect() is False


def test_reconnect_refreshes_expired_token(mock: respx.MockRouter, tmp_path: Path) -> None:
    PyKitsu("kitsu.test", token_folder=tmp_path).login("jane@x.com", "pw")
    mock.get("/auth/authenticated").mock(
        side_effect=[httpx.Response(401), httpx.Response(200, json={"authenticated": True, "user": USER})]
    )
    mock.get("/auth/refresh-token").respond(json={"access_token": "a2"})
    k = PyKitsu("kitsu.test", token_folder=tmp_path)
    assert k.reconnect() == USER
    assert saved(tmp_path)["access_token"] == "a2"  # the refreshed token is saved


def test_reconnect_with_rejected_token_clears_it(mock: respx.MockRouter, tmp_path: Path) -> None:
    PyKitsu("kitsu.test", token_folder=tmp_path).login("jane@x.com", "pw")
    mock.get("/auth/authenticated").respond(401)
    mock.get("/auth/refresh-token").respond(401, json={"msg": "Token has expired"})
    k = PyKitsu("kitsu.test", token_folder=tmp_path)
    events: list[object] = []
    k.add_login_callback(events.append)
    k.add_logout_callback(events.append)
    with pytest.raises(AuthenticationError):
        k.reconnect()
    assert events == [] and k.token is None and not k.can_reconnect()


def test_reconnect_keeps_file_on_server_error(mock: respx.MockRouter, tmp_path: Path) -> None:
    PyKitsu("kitsu.test", token_folder=tmp_path).login("jane@x.com", "pw")
    mock.get("/auth/authenticated").respond(503)
    k = PyKitsu("kitsu.test", token_folder=tmp_path)
    with pytest.raises(KitsuError):
        k.reconnect()
    assert k.can_reconnect()  # the token may still be valid: try again later


def test_corrupt_token_file(tmp_path: Path) -> None:
    (tmp_path / "kitsu_token.json").write_text("{not json")
    assert PyKitsu("kitsu.test", token_folder=tmp_path).can_reconnect() is False


# --------------------------------------------------------------------------- async


async def test_async_events_and_reconnect(mock: respx.MockRouter, tmp_path: Path) -> None:
    events: list[str] = []

    async def on_login(c: AsyncPyKitsu) -> None:
        events.append(f"async-login:{(c.current_user or {}).get('id')}")

    async with AsyncPyKitsu("kitsu.test", token_folder=tmp_path) as k:
        k.add_login_callback(on_login)
        k.add_logout_callback(lambda c: events.append("logout"))
        await k.login("jane@x.com", "pw")
        assert k.can_reconnect()

    async with AsyncPyKitsu("kitsu.test", token_folder=tmp_path) as k2:
        k2.add_login_callback(on_login)
        k2.add_logout_callback(lambda c: events.append("logout"))
        assert await k2.reconnect() == USER
        await k2.logout()
        assert not k2.can_reconnect()
    assert events == ["async-login:u1", "async-login:u1", "logout"]
