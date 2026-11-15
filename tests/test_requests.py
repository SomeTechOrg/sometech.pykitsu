"""Request encoding and response decoding, sync and async, against a mocked server."""

import json
from collections.abc import AsyncIterator, Iterator
from pathlib import Path

import httpx
import pytest
import respx

from pykitsu import (
    AsyncPyKitsu,
    AuthenticationError,
    NotFoundError,
    PyKitsu,
    ResponseValidationError,
)
from pykitsu.models import Project, Shot

API = "https://kitsu.test/api"
PID = "a24a6ea4-ce75-4665-a070-57453082c250"
SHOT = {
    "id": "b24a6ea4-ce75-4665-a070-57453082c250",
    "name": "SH010",
    "project_id": PID,
    "created_at": "2024-03-01T10:00:00",
    "data": {"frame_in": 1001},
    "unknown_new_field": 42,
}


@pytest.fixture
def mock() -> Iterator[respx.MockRouter]:
    with respx.mock(base_url=API, assert_all_called=True) as router:
        yield router


@pytest.fixture
def k() -> Iterator[PyKitsu]:
    with PyKitsu("kitsu.test", token="tok") as client:
        yield client


@pytest.fixture
async def ak() -> AsyncIterator[AsyncPyKitsu]:
    async with AsyncPyKitsu("https://kitsu.test/api/", token="tok") as client:
        yield client


def test_host_normalization() -> None:
    assert PyKitsu("kitsu.test").host == API
    assert PyKitsu("http://kitsu.test/api/").host == "http://kitsu.test/api"


def test_list_of_models(mock: respx.MockRouter, k: PyKitsu) -> None:
    route = mock.get(f"/data/projects/{PID}/shots").respond(json=[SHOT])
    shots = k.shots.get_shots_of_project(PID)
    assert route.calls.last.request.headers["Authorization"] == "Bearer tok"
    [shot] = shots
    assert isinstance(shot, Shot)
    assert shot.name == "SH010"
    assert shot.created_at is not None and shot.created_at.year == 2024
    # extra keys are kept, gazu-style item access works
    assert shot["unknown_new_field"] == 42
    assert shot.get("missing", "x") == "x"
    assert shot.to_dict()["unknown_new_field"] == 42


def test_query_params(mock: respx.MockRouter, k: PyKitsu) -> None:
    route = mock.get("/data/projects/open").respond(json=[{"id": PID, "name": "Big Movie"}])
    [project] = k.projects.get_open_projects(name="Big Movie")
    assert isinstance(project, Project)
    assert route.calls.last.request.url.params["name"] == "Big Movie"


def test_bool_and_none_query(mock: respx.MockRouter, k: PyKitsu) -> None:
    route = mock.post("/pictures/preview-files/p1").respond(201, json={"id": "p1"})
    k.previews.upload_file_of_preview("p1", file=b"data", normalize=False, no_job=None)
    params = route.calls.last.request.url.params
    assert params["normalize"] == "false"
    assert "no_job" not in params


def test_json_body(mock: respx.MockRouter, k: PyKitsu) -> None:
    route = mock.post(f"/data/projects/{PID}/shots").respond(201, json=SHOT)
    shot = k.shots.create_shot(PID, name="SH010", nb_frames=24, extra_body={"code": "x"})
    body = json.loads(route.calls.last.request.content)
    assert body == {"name": "SH010", "nb_frames": 24, "code": "x"}  # None values are omitted
    assert shot.name == "SH010"


def test_multipart_upload_from_path(mock: respx.MockRouter, k: PyKitsu, tmp_path: Path) -> None:
    movie = tmp_path / "v001.mp4"
    movie.write_bytes(b"\x00movie")
    route = mock.post("/pictures/preview-files/p1").respond(201, json={"id": "p1", "extension": "mp4"})
    res = k.previews.upload_file_of_preview("p1", file=movie)
    req = route.calls.last.request
    assert req.headers["content-type"].startswith("multipart/form-data")
    assert b'filename="v001.mp4"' in req.content and b"\x00movie" in req.content
    assert res.extension == "mp4"


def test_json_or_multipart(mock: respx.MockRouter, k: PyKitsu) -> None:
    route = mock.post("/actions/tasks/t1/comment").respond(201, json={"id": "c1"})
    k.comments.comment_task("t1", task_status_id="s1", comment="hi")
    assert route.calls.last.request.headers["content-type"] == "application/json"
    k.comments.comment_task("t1", task_status_id="s1", comment="hi", checklist=[{"text": "a"}], files=[b"x"])
    req = route.calls.last.request
    assert req.headers["content-type"].startswith("multipart/form-data")
    assert b'[{"text": "a"}]' in req.content


def test_binary_download(mock: respx.MockRouter, k: PyKitsu, tmp_path: Path) -> None:
    mock.get("/movies/originals/preview-files/p1.mp4").respond(
        content=b"MOVIE", headers={"content-type": "video/mp4"}
    )
    data: bytes = k.previews.get_movie_of_preview("p1")
    assert data == b"MOVIE"
    path: Path = k.previews.get_movie_of_preview("p1", dest=tmp_path / "out" / "m.mp4")
    assert path.read_bytes() == b"MOVIE"


def test_error_mapping(mock: respx.MockRouter, k: PyKitsu) -> None:
    mock.get("/data/shots/nope").respond(404, json={"message": "Shot not found"})
    with pytest.raises(NotFoundError) as exc:
        k.shots.get_shot("nope")
    assert exc.value.status_code == 404
    assert "Shot not found" in str(exc.value)


def test_lenient_field_and_strict_shape(mock: respx.MockRouter, k: PyKitsu) -> None:
    mock.get(f"/data/projects/{PID}/shots").mock(
        side_effect=[
            httpx.Response(200, json=[{**SHOT, "nb_frames": "not-a-number"}]),
            httpx.Response(200, json={"not": "a list"}),
        ]
    )
    [shot] = k.shots.get_shots_of_project(PID)
    assert shot.name == "SH010"  # the bad field does not break the response
    with pytest.raises(ResponseValidationError) as exc:
        k.shots.get_shots_of_project(PID)
    assert exc.value.raw == {"not": "a list"}


def test_validate_responses_off(mock: respx.MockRouter) -> None:
    mock.get(f"/data/projects/{PID}/shots").respond(json=[SHOT])
    with PyKitsu("kitsu.test", token="t", validate_responses=False) as k:
        assert k.shots.get_shots_of_project(PID) == [SHOT]


def test_login_and_refresh(mock: respx.MockRouter) -> None:
    login = mock.post("/auth/login").respond(json={"access_token": "a1", "refresh_token": "r1"})
    refresh = mock.get("/auth/refresh-token").respond(json={"access_token": "a2"})
    shots = mock.get(f"/data/projects/{PID}/shots").mock(
        side_effect=[httpx.Response(401, json={"msg": "expired"}), httpx.Response(200, json=[SHOT])]
    )
    with PyKitsu("kitsu.test") as k:
        k.login("me@x.com", "pw")
        assert len(k.shots.get_shots_of_project(PID)) == 1
        assert k.token == "a2"
    assert json.loads(login.calls.last.request.content) == {"email": "me@x.com", "password": "pw"}
    assert refresh.calls.last.request.headers["Authorization"] == "Bearer r1"
    assert shots.calls.last.request.headers["Authorization"] == "Bearer a2"


def test_not_logged_in(mock: respx.MockRouter) -> None:
    route = mock.get(f"/data/projects/{PID}/shots").respond(401, json={"msg": "Missing Authorization Header"})
    with PyKitsu("kitsu.test") as k, pytest.raises(AuthenticationError, match=r"call login\(\)"):
        k.shots.get_shots_of_project(PID)
    assert "Authorization" not in route.calls.last.request.headers


def test_password_is_not_stored(mock: respx.MockRouter) -> None:
    mock.post("/auth/login").respond(json={"access_token": "a1", "refresh_token": "r1"})
    with PyKitsu("kitsu.test") as k:
        k.login("me@x.com", "s3cret-pw")
        state = repr(vars(k)) + repr(vars(k._transport))  # pyright: ignore[reportPrivateUsage]
    assert "s3cret-pw" not in state


def test_401_without_refresh_token(mock: respx.MockRouter, k: PyKitsu) -> None:
    mock.get(f"/data/projects/{PID}/shots").respond(401, json={"msg": "bad token"})
    with pytest.raises(AuthenticationError):
        k.shots.get_shots_of_project(PID)


def test_raw_request(mock: respx.MockRouter, k: PyKitsu) -> None:
    mock.get("/data/projects/open").respond(json=[{"id": PID}])
    assert k.request("GET", "/data/projects/open") == [{"id": PID}]


# --------------------------------------------------------------------------- async


async def test_async_list_of_models(mock: respx.MockRouter, ak: AsyncPyKitsu) -> None:
    mock.get(f"/data/projects/{PID}/shots").respond(json=[SHOT])
    [shot] = await ak.shots.get_shots_of_project(PID)
    assert isinstance(shot, Shot) and shot.name == "SH010"


async def test_async_upload_and_download(mock: respx.MockRouter, ak: AsyncPyKitsu, tmp_path: Path) -> None:
    src = tmp_path / "v.png"
    src.write_bytes(b"PNG")
    up = mock.post("/pictures/preview-files/p1").respond(201, json={"id": "p1"})
    await ak.previews.upload_file_of_preview("p1", file=src)
    assert b"PNG" in up.calls.last.request.content
    mock.get("/movies/originals/preview-files/p1.mp4").respond(
        content=b"MOVIE", headers={"content-type": "video/mp4"}
    )
    path = await ak.previews.get_movie_of_preview("p1", dest=tmp_path / "m.mp4")
    assert path.read_bytes() == b"MOVIE"


async def test_async_refresh_and_errors(mock: respx.MockRouter) -> None:
    mock.get("/auth/refresh-token").respond(json={"access_token": "a2"})
    mock.get(f"/data/projects/{PID}/shots").mock(
        side_effect=[httpx.Response(401), httpx.Response(200, json=[SHOT])]
    )
    mock.get("/data/shots/nope").respond(404, json={"message": "nope"})
    async with AsyncPyKitsu("kitsu.test", token="a1", refresh_token="r1") as k:
        assert len(await k.shots.get_shots_of_project(PID)) == 1
        assert k.token == "a2"
        with pytest.raises(NotFoundError):
            await k.shots.get_shot("nope")
