# TaskType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of task type | [optional] 
**short_name** | **str** | Short name of task type | [optional] 
**color** | **str** |  | [optional] [default to '#FFFFFF']
**priority** | **int** | Priority of task type | [optional] 
**for_entity** | **str** |  | [optional] [default to 'Asset']
**allow_timelog** | **bool** | True if timelog is allowed, False otherwise | [optional] [default to True]
**shotgun_id** | **int** | Used for synchronization with a Shotgun instance | [optional] 
**department_id** | **UUID** | Department ID | [optional] 
**id** | **UUID** | Task type unique identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.task_type import TaskType

# TODO update the JSON string below
json = "{}"
# create an instance of TaskType from a JSON string
task_type_instance = TaskType.from_json(json)
# print the JSON string representation of the object
print(TaskType.to_json())

# convert the object into a dict
task_type_dict = task_type_instance.to_dict()
# create an instance of TaskType from a dict
task_type_from_dict = TaskType.from_dict(task_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


