# GetResourceUsageStats200ResponseCpuLoadavg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_1_min** | **float** |  | [optional] 
**last_5_min** | **float** |  | [optional] 
**last_10_min** | **float** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_resource_usage_stats200_response_cpu_loadavg import GetResourceUsageStats200ResponseCpuLoadavg

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceUsageStats200ResponseCpuLoadavg from a JSON string
get_resource_usage_stats200_response_cpu_loadavg_instance = GetResourceUsageStats200ResponseCpuLoadavg.from_json(json)
# print the JSON string representation of the object
print(GetResourceUsageStats200ResponseCpuLoadavg.to_json())

# convert the object into a dict
get_resource_usage_stats200_response_cpu_loadavg_dict = get_resource_usage_stats200_response_cpu_loadavg_instance.to_dict()
# create an instance of GetResourceUsageStats200ResponseCpuLoadavg from a dict
get_resource_usage_stats200_response_cpu_loadavg_from_dict = GetResourceUsageStats200ResponseCpuLoadavg.from_dict(get_resource_usage_stats200_response_cpu_loadavg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


