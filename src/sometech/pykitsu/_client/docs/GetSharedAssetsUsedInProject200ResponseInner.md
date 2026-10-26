# GetSharedAssetsUsedInProject200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Asset unique identifier | [optional] 
**name** | **str** | Asset name | [optional] 
**project_id** | **UUID** | Original project identifier | [optional] 
**entity_type_id** | **UUID** | Asset type identifier | [optional] 
**is_shared** | **bool** | Whether the asset is shared | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_shared_assets_used_in_project200_response_inner import GetSharedAssetsUsedInProject200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSharedAssetsUsedInProject200ResponseInner from a JSON string
get_shared_assets_used_in_project200_response_inner_instance = GetSharedAssetsUsedInProject200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetSharedAssetsUsedInProject200ResponseInner.to_json())

# convert the object into a dict
get_shared_assets_used_in_project200_response_inner_dict = get_shared_assets_used_in_project200_response_inner_instance.to_dict()
# create an instance of GetSharedAssetsUsedInProject200ResponseInner from a dict
get_shared_assets_used_in_project200_response_inner_from_dict = GetSharedAssetsUsedInProject200ResponseInner.from_dict(get_shared_assets_used_in_project200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


