# CreateTaskTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**for_entity** | **str** |  | 
**color** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_task_type_request import CreateTaskTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaskTypeRequest from a JSON string
create_task_type_request_instance = CreateTaskTypeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTaskTypeRequest.to_json())

# convert the object into a dict
create_task_type_request_dict = create_task_type_request_instance.to_dict()
# create an instance of CreateTaskTypeRequest from a dict
create_task_type_request_from_dict = CreateTaskTypeRequest.from_dict(create_task_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


