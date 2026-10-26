# UpdatePlaylistRequestShotsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **UUID** |  | [optional] 
**preview_file_id** | **UUID** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_playlist_request_shots_inner import UpdatePlaylistRequestShotsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePlaylistRequestShotsInner from a JSON string
update_playlist_request_shots_inner_instance = UpdatePlaylistRequestShotsInner.from_json(json)
# print the JSON string representation of the object
print(UpdatePlaylistRequestShotsInner.to_json())

# convert the object into a dict
update_playlist_request_shots_inner_dict = update_playlist_request_shots_inner_instance.to_dict()
# create an instance of UpdatePlaylistRequestShotsInner from a dict
update_playlist_request_shots_inner_from_dict = UpdatePlaylistRequestShotsInner.from_dict(update_playlist_request_shots_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


