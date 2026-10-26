# GetTaskFull200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**task_type_id** | **UUID** |  | [optional] 
**task_status_id** | **UUID** |  | [optional] 
**entity_id** | **UUID** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**assignees** | [**List[GetTaskFull200ResponseAssigneesInner]**](GetTaskFull200ResponseAssigneesInner.md) |  | [optional] 
**task_type** | [**GetTaskFull200ResponseTaskType**](GetTaskFull200ResponseTaskType.md) |  | [optional] 
**task_status** | [**GetTaskFull200ResponseTaskStatus**](GetTaskFull200ResponseTaskStatus.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_task_full200_response import GetTaskFull200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaskFull200Response from a JSON string
get_task_full200_response_instance = GetTaskFull200Response.from_json(json)
# print the JSON string representation of the object
print(GetTaskFull200Response.to_json())

# convert the object into a dict
get_task_full200_response_dict = get_task_full200_response_instance.to_dict()
# create an instance of GetTaskFull200Response from a dict
get_task_full200_response_from_dict = GetTaskFull200Response.from_dict(get_task_full200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


