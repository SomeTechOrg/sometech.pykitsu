# GetEntityPreviewFiles200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Preview file unique identifier | [optional] 
**name** | **str** | Preview file name | [optional] 
**path** | **str** | File path | [optional] 
**revision** | **int** | File revision number | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**entity_id** | **UUID** | Entity identifier | [optional] 
**task_id** | **UUID** | Task identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_entity_preview_files200_response_inner import GetEntityPreviewFiles200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityPreviewFiles200ResponseInner from a JSON string
get_entity_preview_files200_response_inner_instance = GetEntityPreviewFiles200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetEntityPreviewFiles200ResponseInner.to_json())

# convert the object into a dict
get_entity_preview_files200_response_inner_dict = get_entity_preview_files200_response_inner_instance.to_dict()
# create an instance of GetEntityPreviewFiles200ResponseInner from a dict
get_entity_preview_files200_response_inner_from_dict = GetEntityPreviewFiles200ResponseInner.from_dict(get_entity_preview_files200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


