# GetOpenTasks200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** | List of tasks | [optional] 
**stats** | [**GetOpenTasks200ResponseStats**](GetOpenTasks200ResponseStats.md) |  | [optional] 
**limit** | **int** | Number of tasks per page | [optional] 
**page** | **int** | Page number | [optional] 
**is_more** | **bool** | True if there are more tasks to retrieve | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_open_tasks200_response import GetOpenTasks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenTasks200Response from a JSON string
get_open_tasks200_response_instance = GetOpenTasks200Response.from_json(json)
# print the JSON string representation of the object
print(GetOpenTasks200Response.to_json())

# convert the object into a dict
get_open_tasks200_response_dict = get_open_tasks200_response_instance.to_dict()
# create an instance of GetOpenTasks200Response from a dict
get_open_tasks200_response_from_dict = GetOpenTasks200Response.from_dict(get_open_tasks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


