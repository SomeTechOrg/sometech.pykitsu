# Task


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of task | [optional] 
**description** | **str** | Task brief | [optional] 
**priority** | **int** | Priority of task | [optional] 
**duration** | **float** | Duration of task | [optional] 
**estimation** | **float** | Estimation of duration of task | [optional] 
**completion_rate** | **int** | Completion rate of task | [optional] 
**retake_count** | **int** | Retake count of task | [optional] 
**sort_order** | **int** | Sort order of task | [optional] 
**start_date** | **datetime** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**real_start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**last_comment_date** | **datetime** |  | [optional] 
**nb_assets_ready** | **int** | Number of assets ready | [optional] 
**data** | **str** | Free JSON field to add metadata | [optional] 
**shotgun_id** | **int** | Used for synchronization with a Shotgun instance | [optional] 
**project_id** | **UUID** | Project ID | [optional] 
**task_type_id** | **UUID** | Task type ID | [optional] 
**task_status_id** | **UUID** | Task status ID | [optional] 
**entity_id** | **UUID** | Entity ID | [optional] 
**assigner_id** | **UUID** | Person ID | [optional] 
**id** | **UUID** |  | [optional] 
**roles_for_board** | **List[str]** |  | [optional] 
**assignees** | **List[UUID]** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


