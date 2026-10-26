# CreatePlaylistRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**project_id** | **UUID** |  | 
**episode_id** | **UUID** |  | [optional] 
**task_type_id** | **UUID** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_playlist_request import CreatePlaylistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlaylistRequest from a JSON string
create_playlist_request_instance = CreatePlaylistRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePlaylistRequest.to_json())

# convert the object into a dict
create_playlist_request_dict = create_playlist_request_instance.to_dict()
# create an instance of CreatePlaylistRequest from a dict
create_playlist_request_from_dict = CreatePlaylistRequest.from_dict(create_playlist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


