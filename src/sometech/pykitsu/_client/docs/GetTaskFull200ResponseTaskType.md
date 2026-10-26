# GetTaskFull200ResponseTaskType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_task_full200_response_task_type import GetTaskFull200ResponseTaskType

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaskFull200ResponseTaskType from a JSON string
get_task_full200_response_task_type_instance = GetTaskFull200ResponseTaskType.from_json(json)
# print the JSON string representation of the object
print(GetTaskFull200ResponseTaskType.to_json())

# convert the object into a dict
get_task_full200_response_task_type_dict = get_task_full200_response_task_type_instance.to_dict()
# create an instance of GetTaskFull200ResponseTaskType from a dict
get_task_full200_response_task_type_from_dict = GetTaskFull200ResponseTaskType.from_dict(get_task_full200_response_task_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


