# GetShotTasksGetDataShotsShotIdTasks200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**task_type_id** | **UUID** |  | [optional] 
**task_status_id** | **UUID** |  | [optional] 
**entity_id** | **UUID** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**assignees** | **List[UUID]** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_shot_tasks_get_data_shots_shot_id_tasks200_response_inner import GetShotTasksGetDataShotsShotIdTasks200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetShotTasksGetDataShotsShotIdTasks200ResponseInner from a JSON string
get_shot_tasks_get_data_shots_shot_id_tasks200_response_inner_instance = GetShotTasksGetDataShotsShotIdTasks200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetShotTasksGetDataShotsShotIdTasks200ResponseInner.to_json())

# convert the object into a dict
get_shot_tasks_get_data_shots_shot_id_tasks200_response_inner_dict = get_shot_tasks_get_data_shots_shot_id_tasks200_response_inner_instance.to_dict()
# create an instance of GetShotTasksGetDataShotsShotIdTasks200ResponseInner from a dict
get_shot_tasks_get_data_shots_shot_id_tasks200_response_inner_from_dict = GetShotTasksGetDataShotsShotIdTasks200ResponseInner.from_dict(get_shot_tasks_get_data_shots_shot_id_tasks200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


