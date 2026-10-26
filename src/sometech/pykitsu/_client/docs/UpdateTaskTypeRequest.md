# UpdateTaskTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_task_type_request import UpdateTaskTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaskTypeRequest from a JSON string
update_task_type_request_instance = UpdateTaskTypeRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTaskTypeRequest.to_json())

# convert the object into a dict
update_task_type_request_dict = update_task_type_request_instance.to_dict()
# create an instance of UpdateTaskTypeRequest from a dict
update_task_type_request_from_dict = UpdateTaskTypeRequest.from_dict(update_task_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


