# NotifyClientsPlaylistReadyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**studio_id** | **UUID** | Studio unique identifier to notify | [optional] 
**department_id** | **UUID** | Department unique identifier to notify | [optional] 

## Example

```python
from sometech.pykitsu._client.models.notify_clients_playlist_ready_request import NotifyClientsPlaylistReadyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotifyClientsPlaylistReadyRequest from a JSON string
notify_clients_playlist_ready_request_instance = NotifyClientsPlaylistReadyRequest.from_json(json)
# print the JSON string representation of the object
print(NotifyClientsPlaylistReadyRequest.to_json())

# convert the object into a dict
notify_clients_playlist_ready_request_dict = notify_clients_playlist_ready_request_instance.to_dict()
# create an instance of NotifyClientsPlaylistReadyRequest from a dict
notify_clients_playlist_ready_request_from_dict = NotifyClientsPlaylistReadyRequest.from_dict(notify_clients_playlist_ready_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


