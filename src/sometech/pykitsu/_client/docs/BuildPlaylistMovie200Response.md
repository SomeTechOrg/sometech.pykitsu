# BuildPlaylistMovie200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Build job unique identifier | [optional] 
**status** | **str** | Build job status | [optional] 
**created_at** | **datetime** | Build job creation timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.build_playlist_movie200_response import BuildPlaylistMovie200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BuildPlaylistMovie200Response from a JSON string
build_playlist_movie200_response_instance = BuildPlaylistMovie200Response.from_json(json)
# print the JSON string representation of the object
print(BuildPlaylistMovie200Response.to_json())

# convert the object into a dict
build_playlist_movie200_response_dict = build_playlist_movie200_response_instance.to_dict()
# create an instance of BuildPlaylistMovie200Response from a dict
build_playlist_movie200_response_from_dict = BuildPlaylistMovie200Response.from_dict(build_playlist_movie200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


