# CreateOrRetrieveGuestForSharedPlaylistRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] [default to 'Guest']
**last_name** | **str** |  | [optional] 
**guest_id** | **UUID** | If set, return this guest if it still exists | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_or_retrieve_guest_for_shared_playlist_request import CreateOrRetrieveGuestForSharedPlaylistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrRetrieveGuestForSharedPlaylistRequest from a JSON string
create_or_retrieve_guest_for_shared_playlist_request_instance = CreateOrRetrieveGuestForSharedPlaylistRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrRetrieveGuestForSharedPlaylistRequest.to_json())

# convert the object into a dict
create_or_retrieve_guest_for_shared_playlist_request_dict = create_or_retrieve_guest_for_shared_playlist_request_instance.to_dict()
# create an instance of CreateOrRetrieveGuestForSharedPlaylistRequest from a dict
create_or_retrieve_guest_for_shared_playlist_request_from_dict = CreateOrRetrieveGuestForSharedPlaylistRequest.from_dict(create_or_retrieve_guest_for_shared_playlist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


