# GetRunningPreviewFiles200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Preview file unique identifier | [optional] 
**status** | **str** | Preview file status | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_running_preview_files200_response_inner import GetRunningPreviewFiles200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRunningPreviewFiles200ResponseInner from a JSON string
get_running_preview_files200_response_inner_instance = GetRunningPreviewFiles200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetRunningPreviewFiles200ResponseInner.to_json())

# convert the object into a dict
get_running_preview_files200_response_inner_dict = get_running_preview_files200_response_inner_instance.to_dict()
# create an instance of GetRunningPreviewFiles200ResponseInner from a dict
get_running_preview_files200_response_inner_from_dict = GetRunningPreviewFiles200ResponseInner.from_dict(get_running_preview_files200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


