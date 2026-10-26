# GetResourceUsageStats200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**cpu** | [**GetResourceUsageStats200ResponseCpu**](GetResourceUsageStats200ResponseCpu.md) |  | [optional] 
**memory** | [**GetResourceUsageStats200ResponseMemory**](GetResourceUsageStats200ResponseMemory.md) |  | [optional] 
**jobs** | [**GetResourceUsageStats200ResponseJobs**](GetResourceUsageStats200ResponseJobs.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_resource_usage_stats200_response import GetResourceUsageStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceUsageStats200Response from a JSON string
get_resource_usage_stats200_response_instance = GetResourceUsageStats200Response.from_json(json)
# print the JSON string representation of the object
print(GetResourceUsageStats200Response.to_json())

# convert the object into a dict
get_resource_usage_stats200_response_dict = get_resource_usage_stats200_response_instance.to_dict()
# create an instance of GetResourceUsageStats200Response from a dict
get_resource_usage_stats200_response_from_dict = GetResourceUsageStats200Response.from_dict(get_resource_usage_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


