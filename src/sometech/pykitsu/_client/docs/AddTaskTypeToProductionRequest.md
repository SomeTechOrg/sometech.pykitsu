# AddTaskTypeToProductionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_type_id** | **UUID** | Task type unique identifier | 
**priority** | **str** | Task type priority | [optional] 

## Example

```python
from sometech.pykitsu._client.models.add_task_type_to_production_request import AddTaskTypeToProductionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTaskTypeToProductionRequest from a JSON string
add_task_type_to_production_request_instance = AddTaskTypeToProductionRequest.from_json(json)
# print the JSON string representation of the object
print(AddTaskTypeToProductionRequest.to_json())

# convert the object into a dict
add_task_type_to_production_request_dict = add_task_type_to_production_request_instance.to_dict()
# create an instance of AddTaskTypeToProductionRequest from a dict
add_task_type_to_production_request_from_dict = AddTaskTypeToProductionRequest.from_dict(add_task_type_to_production_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


