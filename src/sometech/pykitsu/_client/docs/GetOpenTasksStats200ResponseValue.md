# GetOpenTasksStats200ResponseValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**done** | **int** |  | [optional] 
**estimation** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_open_tasks_stats200_response_value import GetOpenTasksStats200ResponseValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenTasksStats200ResponseValue from a JSON string
get_open_tasks_stats200_response_value_instance = GetOpenTasksStats200ResponseValue.from_json(json)
# print the JSON string representation of the object
print(GetOpenTasksStats200ResponseValue.to_json())

# convert the object into a dict
get_open_tasks_stats200_response_value_dict = get_open_tasks_stats200_response_value_instance.to_dict()
# create an instance of GetOpenTasksStats200ResponseValue from a dict
get_open_tasks_stats200_response_value_from_dict = GetOpenTasksStats200ResponseValue.from_dict(get_open_tasks_stats200_response_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


