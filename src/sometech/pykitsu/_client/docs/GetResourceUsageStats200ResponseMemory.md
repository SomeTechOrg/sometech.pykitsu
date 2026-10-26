# GetResourceUsageStats200ResponseMemory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**used** | **int** |  | [optional] 
**available** | **int** |  | [optional] 
**percent** | **float** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_resource_usage_stats200_response_memory import GetResourceUsageStats200ResponseMemory

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceUsageStats200ResponseMemory from a JSON string
get_resource_usage_stats200_response_memory_instance = GetResourceUsageStats200ResponseMemory.from_json(json)
# print the JSON string representation of the object
print(GetResourceUsageStats200ResponseMemory.to_json())

# convert the object into a dict
get_resource_usage_stats200_response_memory_dict = get_resource_usage_stats200_response_memory_instance.to_dict()
# create an instance of GetResourceUsageStats200ResponseMemory from a dict
get_resource_usage_stats200_response_memory_from_dict = GetResourceUsageStats200ResponseMemory.from_dict(get_resource_usage_stats200_response_memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


