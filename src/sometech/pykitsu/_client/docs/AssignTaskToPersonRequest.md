# AssignTaskToPersonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_id** | **UUID** |  | 

## Example

```python
from sometech.pykitsu._client.models.assign_task_to_person_request import AssignTaskToPersonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignTaskToPersonRequest from a JSON string
assign_task_to_person_request_instance = AssignTaskToPersonRequest.from_json(json)
# print the JSON string representation of the object
print(AssignTaskToPersonRequest.to_json())

# convert the object into a dict
assign_task_to_person_request_dict = assign_task_to_person_request_instance.to_dict()
# create an instance of AssignTaskToPersonRequest from a dict
assign_task_to_person_request_from_dict = AssignTaskToPersonRequest.from_dict(assign_task_to_person_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


