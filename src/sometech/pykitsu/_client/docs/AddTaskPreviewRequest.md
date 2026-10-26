# AddTaskPreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **int** | Revision number for the preview | [optional] 

## Example

```python
from sometech.pykitsu._client.models.add_task_preview_request import AddTaskPreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTaskPreviewRequest from a JSON string
add_task_preview_request_instance = AddTaskPreviewRequest.from_json(json)
# print the JSON string representation of the object
print(AddTaskPreviewRequest.to_json())

# convert the object into a dict
add_task_preview_request_dict = add_task_preview_request_instance.to_dict()
# create an instance of AddTaskPreviewRequest from a dict
add_task_preview_request_from_dict = AddTaskPreviewRequest.from_dict(add_task_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


