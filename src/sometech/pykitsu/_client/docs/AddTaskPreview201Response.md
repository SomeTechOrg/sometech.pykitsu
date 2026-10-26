# AddTaskPreview201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**comment_id** | **UUID** |  | [optional] 
**task_id** | **UUID** |  | [optional] 
**revision** | **int** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.add_task_preview201_response import AddTaskPreview201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddTaskPreview201Response from a JSON string
add_task_preview201_response_instance = AddTaskPreview201Response.from_json(json)
# print the JSON string representation of the object
print(AddTaskPreview201Response.to_json())

# convert the object into a dict
add_task_preview201_response_dict = add_task_preview201_response_instance.to_dict()
# create an instance of AddTaskPreview201Response from a dict
add_task_preview201_response_from_dict = AddTaskPreview201Response.from_dict(add_task_preview201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


