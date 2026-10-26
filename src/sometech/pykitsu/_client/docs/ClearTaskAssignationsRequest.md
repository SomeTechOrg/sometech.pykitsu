# ClearTaskAssignationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_ids** | **List[UUID]** |  | 
**person_id** | **UUID** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.clear_task_assignations_request import ClearTaskAssignationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClearTaskAssignationsRequest from a JSON string
clear_task_assignations_request_instance = ClearTaskAssignationsRequest.from_json(json)
# print the JSON string representation of the object
print(ClearTaskAssignationsRequest.to_json())

# convert the object into a dict
clear_task_assignations_request_dict = clear_task_assignations_request_instance.to_dict()
# create an instance of ClearTaskAssignationsRequest from a dict
clear_task_assignations_request_from_dict = ClearTaskAssignationsRequest.from_dict(clear_task_assignations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


