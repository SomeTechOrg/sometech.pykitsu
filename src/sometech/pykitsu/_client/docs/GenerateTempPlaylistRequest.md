# GenerateTempPlaylistRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_ids** | **List[UUID]** | List of task unique identifiers | 

## Example

```python
from sometech.pykitsu._client.models.generate_temp_playlist_request import GenerateTempPlaylistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateTempPlaylistRequest from a JSON string
generate_temp_playlist_request_instance = GenerateTempPlaylistRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateTempPlaylistRequest.to_json())

# convert the object into a dict
generate_temp_playlist_request_dict = generate_temp_playlist_request_instance.to_dict()
# create an instance of GenerateTempPlaylistRequest from a dict
generate_temp_playlist_request_from_dict = GenerateTempPlaylistRequest.from_dict(generate_temp_playlist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


