# UpdatePreviewBackgroundFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_preview_background_file_request import UpdatePreviewBackgroundFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePreviewBackgroundFileRequest from a JSON string
update_preview_background_file_request_instance = UpdatePreviewBackgroundFileRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePreviewBackgroundFileRequest.to_json())

# convert the object into a dict
update_preview_background_file_request_dict = update_preview_background_file_request_instance.to_dict()
# create an instance of UpdatePreviewBackgroundFileRequest from a dict
update_preview_background_file_request_from_dict = UpdatePreviewBackgroundFileRequest.from_dict(update_preview_background_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


