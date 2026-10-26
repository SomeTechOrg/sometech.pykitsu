# UpdateTaskStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_task_status_request import UpdateTaskStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaskStatusRequest from a JSON string
update_task_status_request_instance = UpdateTaskStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTaskStatusRequest.to_json())

# convert the object into a dict
update_task_status_request_dict = update_task_status_request_instance.to_dict()
# create an instance of UpdateTaskStatusRequest from a dict
update_task_status_request_from_dict = UpdateTaskStatusRequest.from_dict(update_task_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


