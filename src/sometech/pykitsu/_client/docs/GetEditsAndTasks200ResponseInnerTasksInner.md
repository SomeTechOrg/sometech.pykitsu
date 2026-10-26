# GetEditsAndTasks200ResponseInnerTasksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Task unique identifier | [optional] 
**name** | **str** | Task name | [optional] 
**task_type_id** | **UUID** | Task type identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_edits_and_tasks200_response_inner_tasks_inner import GetEditsAndTasks200ResponseInnerTasksInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEditsAndTasks200ResponseInnerTasksInner from a JSON string
get_edits_and_tasks200_response_inner_tasks_inner_instance = GetEditsAndTasks200ResponseInnerTasksInner.from_json(json)
# print the JSON string representation of the object
print(GetEditsAndTasks200ResponseInnerTasksInner.to_json())

# convert the object into a dict
get_edits_and_tasks200_response_inner_tasks_inner_dict = get_edits_and_tasks200_response_inner_tasks_inner_instance.to_dict()
# create an instance of GetEditsAndTasks200ResponseInnerTasksInner from a dict
get_edits_and_tasks200_response_inner_tasks_inner_from_dict = GetEditsAndTasks200ResponseInnerTasksInner.from_dict(get_edits_and_tasks200_response_inner_tasks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


