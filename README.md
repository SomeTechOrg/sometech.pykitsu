# pykitsu

A Modern Python Client for Kitsu Production Tracker [Kitsu](https://www.cg-wire.com/kitsu) API. It is generated from the official OpenAPI spec (`spec/openapi.json`, v1.1.1 → 811 routes in 25 groups),
supports sync and async calls, and returns pydantic v2 models.

**Python 3.9+.** This covers DCCs on the VFX Reference Platform CY2022, such as Maya 2023,
Houdini 19.5 and Nuke 14. On 3.9 the dependency resolver installs pydantic 2.13.x, because pydantic
2.14 dropped 3.9 support. Python 3.9 itself has been end-of-life since October 2025, so plan to
drop it when your DCCs allow. The code generator (`codegen/generate.py`) needs Python 3.11+.

**Lazy loading.** Importing `pykitsu` and creating a client does not load the API groups or
their models, and does not import pydantic. A group loads the first time you use it:

| step                              | cost (indicative) |
|-----------------------------------|-------------------|
| `import pykitsu` + `PyKitsu(...)` | ~100 ms (httpx)   |
| first `k.shots`                   | ~150 ms (pydantic + core models + shots) |
| every other group                 | only when used    |

## Usage

```python
from pathlib import Path
from pykitsu import PyKitsu, NotFoundError

with PyKitsu("https://kitsu.example.com") as k:
    k.login("me@example.com", password)   # or PyKitsu.from_env() with KITSU_HOST + KITSU_TOKEN
    for project in k.projects.get_open_projects():
        for shot in k.shots.get_shots_of_project(project.id):
            print(shot.name, shot.nb_frames, shot["data"])   # attributes or gazu-style keys

    shot = k.shots.create_shot(project.id, name="SH010", nb_frames=24)
    k.previews.upload_file_of_preview(preview_id, file=Path("v001.mp4"))
    k.previews.get_movie_of_preview(preview_id, dest="/tmp/v001.mp4")  # -> Path; without dest -> bytes
```

Async:

```python
from pykitsu import AsyncPyKitsu

async with AsyncPyKitsu("https://kitsu.example.com") as k:
    await k.login("me@example.com", password)
    shots = await k.shots.get_shots_of_project(project_id)
```

* **Auth**: call `k.login(email, password)` or `k.reconnect()`, or pass `token=` (a bot token,
  for example). The client never stores the password: `login()` sends it once and keeps only the
  access and refresh tokens. When a refresh token is present, an expired access token is refreshed
  once and the request is retried. A request sent without a token fails with an
  `AuthenticationError` that tells you to log in.
* **Auth events and saved sessions** (for GUI apps):

  ```python
  k = PyKitsu("https://kitsu.example.com", token_folder="~/.config/mytool")
  k.add_login_callback(lambda c: print("logged in as", c.current_user["full_name"]))
  k.add_logout_callback(lambda c: print("logged out"))

  if k.can_reconnect():        # a token was saved for this host in the folder
      k.reconnect()            # checks it with the server (refreshes it if expired)
  else:
      k.login(email, password) # saves the tokens in <token_folder>/kitsu_token.json
  ...
  k.logout()                   # removes the saved file
  ```

  * **When the callbacks run**:
    * Login callbacks run after `login()` and after `reconnect()`.
    * Logout callbacks run after `logout()`, but only if a session was open.
  * **Threads and errors**: callbacks receive the client and run in the thread that made the
    request, so forward them to your UI thread, for example with a Qt signal. If a callback raises
    an exception, it is logged and the remaining callbacks still run.
  * **Async**: `AsyncPyKitsu` also accepts `async def` callbacks.
  * **Removing callbacks**: use `remove_login_callback` and `remove_logout_callback`.
  * **Refreshed tokens**: these are saved too. The file is readable by its owner only (0600), and
    it stores the host it belongs to.
  * **Failed reconnect**: `reconnect()` raises `AuthenticationError` and deletes the file
    when the server rejects the saved token. For any other failure, such as a network error or a
    5xx, the file is kept.
* **Host**: `https://kitsu.example.com` and `https://kitsu.example.com/api` both work.
* **Errors**: `KitsuAPIError` has the subclasses `BadRequestError`, `AuthenticationError`,
  `PermissionDeniedError`, `NotFoundError`, `ConflictError` and `ServerError`. Each one carries
  `.status_code`, `.body` and `.response`.
* **Lenient models**: unknown keys are kept, in `model_extra` or through `obj["key"]`. If a field
  does not match the spec's type, it keeps its raw value instead of failing the whole response.
  To get plain JSON back, use `validate_responses=False`.
* **Escape hatches**:
  * `extra_body={...}` on every method that has a body
  * `k.request("GET", "/any/route")`
  * `k.http`, the underlying httpx client
* **Discoverability**: every method's docstring ends with its route (``GET /data/...``).
  `dir(k)` lists the groups.

## Groups

`assets`, `authentication`, `breakdown`, `chat`, `comments`, `concepts`, `crud`, `departments`,
`edits`, `entities`, `events`, `export`, `files`, `imports`, `index`, `news`, `persons`,
`playlists`, `previews`, `project_templates`, `projects`, `search`, `shots`, `tasks`, `user`.

Method names come from the spec summaries. For example, "Get the shots of a project" becomes
`get_shots_of_project`. The `crud` group holds the generic row routes (`get_task_rows`,
`create_person`…).

## Regenerating

```bash
uv run python codegen/generate.py            # from spec/openapi.json
uv run python codegen/generate.py --fetch    # download the latest spec first
uv run ruff check src && uv run pyright && uv run pytest
uv run --isolated --python 3.9 pytest        # oldest supported Python (temporary env)
```

Generated model and return types use `Optional[...]` and `Union[...]` instead of `X | Y`,
because pydantic evaluates them at runtime and `X | Y` only works from Python 3.10.

Do not edit these files by hand, because the generator overwrites them:
`src/pykitsu/groups/**`, `src/pykitsu/models/_core.py`, `src/pykitsu/models/__init__.py`,
`src/pykitsu/_groups.py` and `src/pykitsu/_spec_version.py`.
Put fixes in `spec/overrides.toml` instead: method renames, forced return models and group moves.
