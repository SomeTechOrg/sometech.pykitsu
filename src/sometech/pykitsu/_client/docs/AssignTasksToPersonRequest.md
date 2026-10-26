# AssignTasksToPersonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_ids** | **List[UUID]** |  | 

## Example

```python
from sometech.pykitsu._client.models.assign_tasks_to_person_request import AssignTasksToPersonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignTasksToPersonRequest from a JSON string
assign_tasks_to_person_request_instance = AssignTasksToPersonRequest.from_json(json)
# print the JSON string representation of the object
print(AssignTasksToPersonRequest.to_json())

# convert the object into a dict
assign_tasks_to_person_request_dict = assign_tasks_to_person_request_instance.to_dict()
# create an instance of AssignTasksToPersonRequest from a dict
assign_tasks_to_person_request_from_dict = AssignTasksToPersonRequest.from_dict(assign_tasks_to_person_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


