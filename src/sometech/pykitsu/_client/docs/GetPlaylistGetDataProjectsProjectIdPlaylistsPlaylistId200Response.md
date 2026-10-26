# GetPlaylistGetDataProjectsProjectIdPlaylistsPlaylistId200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Playlist unique identifier | [optional] 
**name** | **str** | Playlist name | [optional] 
**project_id** | **UUID** | Project unique identifier | [optional] 
**shots** | **List[object]** | List of shots with preview file revisions | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_playlist_get_data_projects_project_id_playlists_playlist_id200_response import GetPlaylistGetDataProjectsProjectIdPlaylistsPlaylistId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlaylistGetDataProjectsProjectIdPlaylistsPlaylistId200Response from a JSON string
get_playlist_get_data_projects_project_id_playlists_playlist_id200_response_instance = GetPlaylistGetDataProjectsProjectIdPlaylistsPlaylistId200Response.from_json(json)
# print the JSON string representation of the object
print(GetPlaylistGetDataProjectsProjectIdPlaylistsPlaylistId200Response.to_json())

# convert the object into a dict
get_playlist_get_data_projects_project_id_playlists_playlist_id200_response_dict = get_playlist_get_data_projects_project_id_playlists_playlist_id200_response_instance.to_dict()
# create an instance of GetPlaylistGetDataProjectsProjectIdPlaylistsPlaylistId200Response from a dict
get_playlist_get_data_projects_project_id_playlists_playlist_id200_response_from_dict = GetPlaylistGetDataProjectsProjectIdPlaylistsPlaylistId200Response.from_dict(get_playlist_get_data_projects_project_id_playlists_playlist_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


