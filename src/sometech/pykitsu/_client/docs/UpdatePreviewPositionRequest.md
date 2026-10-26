# UpdatePreviewPositionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | New position for the preview | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_preview_position_request import UpdatePreviewPositionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePreviewPositionRequest from a JSON string
update_preview_position_request_instance = UpdatePreviewPositionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePreviewPositionRequest.to_json())

# convert the object into a dict
update_preview_position_request_dict = update_preview_position_request_instance.to_dict()
# create an instance of UpdatePreviewPositionRequest from a dict
update_preview_position_request_from_dict = UpdatePreviewPositionRequest.from_dict(update_preview_position_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


