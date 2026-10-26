# Playlist


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of playlist | [optional] 
**shots** | **str** | JSON field describing shot and preview listed in | [optional] 
**project_id** | **UUID** | Project ID | [optional] 
**episode_id** | **UUID** | Episode ID | [optional] 
**for_client** | **bool** |  | [optional] [default to False]
**for_entity** | **str** |  | [optional] [default to 'shot']
**is_for_all** | **bool** |  | [optional] [default to False]
**task_type_id** | **UUID** | Task type ID | [optional] 

## Example

```python
from sometech.pykitsu._client.models.playlist import Playlist

# TODO update the JSON string below
json = "{}"
# create an instance of Playlist from a JSON string
playlist_instance = Playlist.from_json(json)
# print the JSON string representation of the object
print(Playlist.to_json())

# convert the object into a dict
playlist_dict = playlist_instance.to_dict()
# create an instance of Playlist from a dict
playlist_from_dict = Playlist.from_dict(playlist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


