# AddPreviewBackgroundFileToProductionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_background_file_id** | **UUID** | Preview background file unique identifier | 

## Example

```python
from sometech.pykitsu._client.models.add_preview_background_file_to_production_request import AddPreviewBackgroundFileToProductionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddPreviewBackgroundFileToProductionRequest from a JSON string
add_preview_background_file_to_production_request_instance = AddPreviewBackgroundFileToProductionRequest.from_json(json)
# print the JSON string representation of the object
print(AddPreviewBackgroundFileToProductionRequest.to_json())

# convert the object into a dict
add_preview_background_file_to_production_request_dict = add_preview_background_file_to_production_request_instance.to_dict()
# create an instance of AddPreviewBackgroundFileToProductionRequest from a dict
add_preview_background_file_to_production_request_from_dict = AddPreviewBackgroundFileToProductionRequest.from_dict(add_preview_background_file_to_production_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


