# GetTask200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**task_type_id** | **UUID** |  | [optional] 
**entity_id** | **UUID** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**task_status_id** | **UUID** |  | [optional] 
**assignees** | **List[UUID]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_task200_response import GetTask200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTask200Response from a JSON string
get_task200_response_instance = GetTask200Response.from_json(json)
# print the JSON string representation of the object
print(GetTask200Response.to_json())

# convert the object into a dict
get_task200_response_dict = get_task200_response_instance.to_dict()
# create an instance of GetTask200Response from a dict
get_task200_response_from_dict = GetTask200Response.from_dict(get_task200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


