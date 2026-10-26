from __future__ import annotations

import json
from contextlib import asynccontextmanager
from pathlib import Path

from rich import print

from . import _client
from ._client.models.person import Person


class PyKitsu:
    userinfo: Person|None
    projects : _client.ProjectsApi
    assets : _client.AssetsApi
    exports : _client.ExportApi

    def __init__(self, host:str, access_token_cache_file: Path | str|None):
        if access_token_cache_file is not None:
            access_token_cache_file = Path(access_token_cache_file)
        self._access_token_cache_file = access_token_cache_file
        self._host = host
        self.userinfo = None


    def _save_access_token(self, access_token:str):
        if self._access_token_cache_file is None:
            return
        self._access_token_cache_file.parent.mkdir(parents=True, exist_ok=True)
        with self._access_token_cache_file.open("w") as fp:
            json.dump(access_token, fp)
        print("access_token saved", self._access_token_cache_file)

    def _read_access_token(self)->str|None:
        if self._access_token_cache_file is None or not self._access_token_cache_file.exists():
            return None
        with self._access_token_cache_file.open() as fp:
            return json.load(fp)

    async def _on_connect(self, client:_client.ApiClient, userinfo:Person):
        print('Caching User info...')
        self.userinfo = userinfo
        self.projects = _client.ProjectsApi(client)
        self.assets = _client.AssetsApi(client)
        self.exports = _client.ExportApi(client)

    async def _on_disconnect(self, client:_client.ApiClient):
        await client.close()
        self.userinfo = None
        # self.projects = None
        # self.assets = None
        # self.exports = None

    @asynccontextmanager
    async def connected_bot(self, api_key:str):
        configuration = _client.Configuration(host=self._host)
        configuration.api_key['JWTAuthorization'] = api_key
        configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

        async with _client.ApiClient(configuration) as client:
            print('Authenticating...')
            info = await _client.AuthenticationApi(client).check_authentication_status_with_http_info()
            data = json.loads(info.raw_data)
            userinfo = Person.from_dict(data['user'])
            if userinfo is None:
                raise ValueError('Could not read userinfo on after authentication!')

            try:
                await self._on_connect(client, userinfo)
                yield self
            finally:
                await self._on_disconnect(client)

    @asynccontextmanager
    async def connected_user(self, email:str|None=None, password:str|None=None, use_access_cache:bool=True):
        if use_access_cache:
            access_token = self._read_access_token()
            if access_token is not None:
                async with self.connected_bot(api_key=access_token):
                    if self.userinfo is not None:
                        # connection success
                        yield self
                        return

        if email is None or  password is None:
            raise ValueError('Could not connect: Could not used token cache but email/password not provided.')

        configuration = _client.Configuration(host=self._host)
        configuration.username = email
        configuration.password = password

        async with _client.ApiClient(configuration) as client:
            print('Signin user in...')
            response = await _client.AuthenticationApi(client).login_user_with_http_info(
                _client.LoginUserRequest(
                    email=configuration.username,
                    password=configuration.password,  # pyright: ignore[reportArgumentType]
                ),
            )
            data = json.loads(response.raw_data)
            self._save_access_token(data["access_token"])

            userinfo = Person.from_dict(data['user'])
            if userinfo is None:
                raise ValueError('Could not read userinfo on after user login!')

            try:
                await self._on_connect(client, userinfo)
                yield self
            finally:
                await self._on_disconnect(client)


async def usage():
    host = 'https://lola.kitsu.andarta-pictures.com/api'
    email='d.coureau@andarta-pictures.com'
    password='fnDhrt5LeV2Sd2Y'
    api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc5MzAxMjUxNiwianRpIjoiZDJkZjI2OGItYzBjZC00OWIxLTlhZjMtOTA0MjliNTllZTZkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImMzOTIyODUwLTFjYzItNDgyYi1hODI5LTRhNjFmN2U3NDVkZSIsIm5iZiI6MTc5MzAxMjUxNiwiaWRlbnRpdHlfdHlwZSI6ImJvdCJ9.cYhzzXH-ylbcu_DjXtTg3zPtuIO0q-yRZJFeBSoCedQ'

    kitsu = PyKitsu(host=host, access_token_cache_file='/tmp/test_pykitsu/atcp.json')

    if 1:
        async with kitsu.connected_user(email=email, password=password):
            print( kitsu.userinfo)

            print('Fetching projects...')
            projects = await kitsu.projects.get_all_projects()
            # print(f'{projects=}')
            for project in projects[:5]:
                print(project.id, project.name, project.project_status_id)

            print('Fetching timesheets...')
            import time
            t = time.time()
            csv = await kitsu.exports.export_time_spents_csv()
            print(csv)
            print( time.time()-t)

    if 0:
        async with kitsu.connected_bot(api_key=api_key):
            print( kitsu.userinfo)

            print('Fetching projects...')
            projects = await kitsu.projects.get_all_projects()
            # print(f'{projects=}')
            for project in projects[:5]:
                print(project.id, project.name, project.project_status_id)

            print('Fetching timesheets...')
            import time
            t = time.time()
            csv = await kitsu.exports.export_time_spents_csv()
            print(csv)
            print( time.time()-t)

if __name__ == '__main__':
    import asyncio
    asyncio.run(usage())
