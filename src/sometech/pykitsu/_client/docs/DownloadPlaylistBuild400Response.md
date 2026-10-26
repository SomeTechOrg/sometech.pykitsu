# DownloadPlaylistBuild400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **bool** | Error flag | [optional] 
**message** | **str** | Error message | [optional] 

## Example

```python
from sometech.pykitsu._client.models.download_playlist_build400_response import DownloadPlaylistBuild400Response

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadPlaylistBuild400Response from a JSON string
download_playlist_build400_response_instance = DownloadPlaylistBuild400Response.from_json(json)
# print the JSON string representation of the object
print(DownloadPlaylistBuild400Response.to_json())

# convert the object into a dict
download_playlist_build400_response_dict = download_playlist_build400_response_instance.to_dict()
# create an instance of DownloadPlaylistBuild400Response from a dict
download_playlist_build400_response_from_dict = DownloadPlaylistBuild400Response.from_dict(download_playlist_build400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


