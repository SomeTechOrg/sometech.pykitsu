# GetProjectPlaylists200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Playlist unique identifier | [optional] 
**name** | **str** | Playlist name | [optional] 
**project_id** | **UUID** | Project unique identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_project_playlists200_response_inner import GetProjectPlaylists200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectPlaylists200ResponseInner from a JSON string
get_project_playlists200_response_inner_instance = GetProjectPlaylists200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectPlaylists200ResponseInner.to_json())

# convert the object into a dict
get_project_playlists200_response_inner_dict = get_project_playlists200_response_inner_instance.to_dict()
# create an instance of GetProjectPlaylists200ResponseInner from a dict
get_project_playlists200_response_inner_from_dict = GetProjectPlaylists200ResponseInner.from_dict(get_project_playlists200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


