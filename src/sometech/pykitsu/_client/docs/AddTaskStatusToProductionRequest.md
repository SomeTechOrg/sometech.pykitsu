# AddTaskStatusToProductionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_status_id** | **UUID** | Task status unique identifier | 

## Example

```python
from sometech.pykitsu._client.models.add_task_status_to_production_request import AddTaskStatusToProductionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTaskStatusToProductionRequest from a JSON string
add_task_status_to_production_request_instance = AddTaskStatusToProductionRequest.from_json(json)
# print the JSON string representation of the object
print(AddTaskStatusToProductionRequest.to_json())

# convert the object into a dict
add_task_status_to_production_request_dict = add_task_status_to_production_request_instance.to_dict()
# create an instance of AddTaskStatusToProductionRequest from a dict
add_task_status_to_production_request_from_dict = AddTaskStatusToProductionRequest.from_dict(add_task_status_to_production_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


