# GetPlaylistGetDataPlaylistsInstanceId200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**episode_id** | **UUID** |  | [optional] 
**task_type_id** | **UUID** |  | [optional] 
**shots** | **List[object]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_playlist_get_data_playlists_instance_id200_response import GetPlaylistGetDataPlaylistsInstanceId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlaylistGetDataPlaylistsInstanceId200Response from a JSON string
get_playlist_get_data_playlists_instance_id200_response_instance = GetPlaylistGetDataPlaylistsInstanceId200Response.from_json(json)
# print the JSON string representation of the object
print(GetPlaylistGetDataPlaylistsInstanceId200Response.to_json())

# convert the object into a dict
get_playlist_get_data_playlists_instance_id200_response_dict = get_playlist_get_data_playlists_instance_id200_response_instance.to_dict()
# create an instance of GetPlaylistGetDataPlaylistsInstanceId200Response from a dict
get_playlist_get_data_playlists_instance_id200_response_from_dict = GetPlaylistGetDataPlaylistsInstanceId200Response.from_dict(get_playlist_get_data_playlists_instance_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


