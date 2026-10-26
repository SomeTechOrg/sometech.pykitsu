# UpdateTaskType200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**for_entity** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_task_type200_response import UpdateTaskType200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaskType200Response from a JSON string
update_task_type200_response_instance = UpdateTaskType200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateTaskType200Response.to_json())

# convert the object into a dict
update_task_type200_response_dict = update_task_type200_response_instance.to_dict()
# create an instance of UpdateTaskType200Response from a dict
update_task_type200_response_from_dict = UpdateTaskType200Response.from_dict(update_task_type200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


