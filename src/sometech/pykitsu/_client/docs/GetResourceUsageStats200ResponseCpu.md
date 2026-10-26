# GetResourceUsageStats200ResponseCpu


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent** | **List[float]** |  | [optional] 
**loadavg** | [**GetResourceUsageStats200ResponseCpuLoadavg**](GetResourceUsageStats200ResponseCpuLoadavg.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_resource_usage_stats200_response_cpu import GetResourceUsageStats200ResponseCpu

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceUsageStats200ResponseCpu from a JSON string
get_resource_usage_stats200_response_cpu_instance = GetResourceUsageStats200ResponseCpu.from_json(json)
# print the JSON string representation of the object
print(GetResourceUsageStats200ResponseCpu.to_json())

# convert the object into a dict
get_resource_usage_stats200_response_cpu_dict = get_resource_usage_stats200_response_cpu_instance.to_dict()
# create an instance of GetResourceUsageStats200ResponseCpu from a dict
get_resource_usage_stats200_response_cpu_from_dict = GetResourceUsageStats200ResponseCpu.from_dict(get_resource_usage_stats200_response_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


