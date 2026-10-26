# TaskStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of task status | [optional] 
**short_name** | **str** | Short name of task status | [optional] 
**color** | **str** |  | [optional] 
**is_done** | **bool** | True if the task is done, False otherwise | [optional] [default to False]
**is_artist_allowed** | **bool** | True if the artist is allowed, False otherwise | [optional] [default to True]
**is_client_allowed** | **bool** | True if the client is allowed, False otherwise | [optional] [default to True]
**is_retake** | **bool** | True if the task was retaken, False otherwise | [optional] [default to False]
**is_feedback_request** | **bool** | True if feedback was requested, False otherwise | [optional] [default to False]
**is_default** | **bool** | True if the task is default, False otherwise | [optional] [default to False]
**shotgun_id** | **int** | Used for synchronization with a Shotgun instance | [optional] 

## Example

```python
from sometech.pykitsu._client.models.task_status import TaskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStatus from a JSON string
task_status_instance = TaskStatus.from_json(json)
# print the JSON string representation of the object
print(TaskStatus.to_json())

# convert the object into a dict
task_status_dict = task_status_instance.to_dict()
# create an instance of TaskStatus from a dict
task_status_from_dict = TaskStatus.from_dict(task_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


