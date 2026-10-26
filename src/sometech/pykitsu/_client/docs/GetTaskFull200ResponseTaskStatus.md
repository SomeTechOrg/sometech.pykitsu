# GetTaskFull200ResponseTaskStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_task_full200_response_task_status import GetTaskFull200ResponseTaskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaskFull200ResponseTaskStatus from a JSON string
get_task_full200_response_task_status_instance = GetTaskFull200ResponseTaskStatus.from_json(json)
# print the JSON string representation of the object
print(GetTaskFull200ResponseTaskStatus.to_json())

# convert the object into a dict
get_task_full200_response_task_status_dict = get_task_full200_response_task_status_instance.to_dict()
# create an instance of GetTaskFull200ResponseTaskStatus from a dict
get_task_full200_response_task_status_from_dict = GetTaskFull200ResponseTaskStatus.from_dict(get_task_full200_response_task_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


