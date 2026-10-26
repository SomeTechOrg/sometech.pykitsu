# sometech.pykitsu
Modern (async and typed) python client for Kitsu Production Tracker

The client is 90% generated from Kitsu openapi using `openapi-generator-cli`

Due to... creative ways in the api specs... the api model are not fully mapped.\
But `openapi-generator-cli` has a way to deal with this and next versions will have better typed return values.\
In the meantime you still get completion for arguements and objects attributes.

## Authentication

```python
from sometech.pykitsu import PyKitsu

#
# Sign in with a user and password:
# 
kitsu = PyKitsu(host=host)
async with kitsu.connected_user(email=my_email, password=my_password):
    print(kitsu.userinfo)

#
# Sign in with the saved user:
# 

# 1) Specify the file where the token will be saved
cache_file=r'C:\path\to\private\folder\kitsu_access.json'
kitsu = PyKitsu(host=host, access_token_cache_file=cache_file)

# 2) Connect with email and password at least once:
async with kitsu.connected_user(email=my_email, password=my_password):
    print(kitsu.userinfo)

# 3) Now you can connect without email and password:
async with kitsu.connected_user():
    print(kitsu.userinfo)

# 4) To change user, be sure to set `use_access_cache=False`
async with kitsu.connected_user(
    email=your_email, 
    password=your_password, 
    use_access_cache=False
):
    print(kitsu.userinfo)

# 
# Sign in with an api key:
# 
kitsu = PyKitsu(host=host)
async with kitsu.connected_bot(api_key=my_api_key):
    print(kitsu.userinfo)

```

## Usage
```python

from sometech.pykitsu import PyKitsu

kitsu = PyKitsu(host=host)

async with kitsu.connected_XXX(...): # choose your connection style...

    # Once connected, you have the current user info here:
    print(kitsu.userinfo)

    # And each "api group" is accessible in a dedicated namespace:

    print('Fetching projects...')
    projects = await kitsu.projects.get_all_projects()
    for project in projects:
        print(
            'Project:',
            project.id, 
            project.name, 
            project.project_status_id
        )

    print('Fetching timesheets...')
    csv = await kitsu.exports.export_time_spents_csv()

```


## Generate sometech.pykitsu._client

- Download kitsu open api json from either:
  - your kitsu: `https://yourkitsu.yourhost.com/api/openapi.json` 
  - official kitsu: `https://kitsu-api.cg-wire.com/openapi.json`
- cd to `sometech.kitsu/apigen/` and save it there as `api.json`
- Fix the api specs:
  - `uv run python fixer_v3.py api.json api.fixed.json`
- Fix the api models:
  - `uv run python link_models.py api.fixed.json api.linked.json`
- Ensure the `config.yaml` file contains what you want, like:
  - projectName: pykitsu
  - packageName: sometech.pykitsu._client
  - packageVersion: 1.0.36 !!<- put your version here
  - generateSourceCodeOnly: true
  - library: httpx2
- Generate the package:
  - `uv run openapi-generator-cli generate -i api.linked.json -g python -o ./generated -c config.yaml`
- Copy the (generated) folder `./generated/sometech/pykitsu/_client` as `../src/sometech/pykitsu/_client`
- Run the tests
