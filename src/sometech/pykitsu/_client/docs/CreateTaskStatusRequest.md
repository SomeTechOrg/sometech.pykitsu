# CreateTaskStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**short_name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] [default to False]

## Example

```python
from sometech.pykitsu._client.models.create_task_status_request import CreateTaskStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaskStatusRequest from a JSON string
create_task_status_request_instance = CreateTaskStatusRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTaskStatusRequest.to_json())

# convert the object into a dict
create_task_status_request_dict = create_task_status_request_instance.to_dict()
# create an instance of CreateTaskStatusRequest from a dict
create_task_status_request_from_dict = CreateTaskStatusRequest.from_dict(create_task_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


