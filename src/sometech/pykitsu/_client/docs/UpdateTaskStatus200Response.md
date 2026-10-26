# UpdateTaskStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_task_status200_response import UpdateTaskStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTaskStatus200Response from a JSON string
update_task_status200_response_instance = UpdateTaskStatus200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateTaskStatus200Response.to_json())

# convert the object into a dict
update_task_status200_response_dict = update_task_status200_response_instance.to_dict()
# create an instance of UpdateTaskStatus200Response from a dict
update_task_status200_response_from_dict = UpdateTaskStatus200Response.from_dict(update_task_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


