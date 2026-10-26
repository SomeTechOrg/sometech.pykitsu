# AddEntityToPlaylistRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **UUID** | Entity unique identifier to add to playlist | 
**preview_file_id** | **UUID** | Optional preview file identifier associated to the entity | [optional] 

## Example

```python
from sometech.pykitsu._client.models.add_entity_to_playlist_request import AddEntityToPlaylistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddEntityToPlaylistRequest from a JSON string
add_entity_to_playlist_request_instance = AddEntityToPlaylistRequest.from_json(json)
# print the JSON string representation of the object
print(AddEntityToPlaylistRequest.to_json())

# convert the object into a dict
add_entity_to_playlist_request_dict = add_entity_to_playlist_request_instance.to_dict()
# create an instance of AddEntityToPlaylistRequest from a dict
add_entity_to_playlist_request_from_dict = AddEntityToPlaylistRequest.from_dict(add_entity_to_playlist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


