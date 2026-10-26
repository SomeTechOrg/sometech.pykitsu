# UpdatePlaylistRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**shots** | [**List[UpdatePlaylistRequestShotsInner]**](UpdatePlaylistRequestShotsInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_playlist_request import UpdatePlaylistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePlaylistRequest from a JSON string
update_playlist_request_instance = UpdatePlaylistRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePlaylistRequest.to_json())

# convert the object into a dict
update_playlist_request_dict = update_playlist_request_instance.to_dict()
# create an instance of UpdatePlaylistRequest from a dict
update_playlist_request_from_dict = UpdatePlaylistRequest.from_dict(update_playlist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


