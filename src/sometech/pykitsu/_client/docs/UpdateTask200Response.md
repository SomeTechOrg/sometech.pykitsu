# UpdateTask200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**task_type_id** | **UUID** |  | [optional] 
**entity_id** | **UUID** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**task_status_id** | **UUID** |  | [optional] 
**assignees** | **List[UUID]** |  | [optional] 
**duration** | **float** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_task200_response import UpdateTask200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTask200Response from a JSON string
update_task200_response_instance = UpdateTask200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateTask200Response.to_json())

# convert the object into a dict
update_task200_response_dict = update_task200_response_instance.to_dict()
# create an instance of UpdateTask200Response from a dict
update_task200_response_from_dict = UpdateTask200Response.from_dict(update_task200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


