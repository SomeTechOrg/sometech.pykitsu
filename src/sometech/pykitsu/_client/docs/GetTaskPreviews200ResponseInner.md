# GetTaskPreviews200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**task_id** | **UUID** |  | [optional] 
**revision** | **int** |  | [optional] 
**comment_id** | **UUID** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_task_previews200_response_inner import GetTaskPreviews200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaskPreviews200ResponseInner from a JSON string
get_task_previews200_response_inner_instance = GetTaskPreviews200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetTaskPreviews200ResponseInner.to_json())

# convert the object into a dict
get_task_previews200_response_inner_dict = get_task_previews200_response_inner_instance.to_dict()
# create an instance of GetTaskPreviews200ResponseInner from a dict
get_task_previews200_response_inner_from_dict = GetTaskPreviews200ResponseInner.from_dict(get_task_previews200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


