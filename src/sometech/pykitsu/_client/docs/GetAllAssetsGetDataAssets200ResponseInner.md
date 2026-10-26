# GetAllAssetsGetDataAssets200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Asset unique identifier | [optional] 
**name** | **str** | Asset name | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**entity_type_id** | **UUID** | Asset type identifier | [optional] 
**project_name** | **str** | Project name | [optional] 
**asset_type_name** | **str** | Asset type name | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_all_assets_get_data_assets200_response_inner import GetAllAssetsGetDataAssets200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllAssetsGetDataAssets200ResponseInner from a JSON string
get_all_assets_get_data_assets200_response_inner_instance = GetAllAssetsGetDataAssets200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetAllAssetsGetDataAssets200ResponseInner.to_json())

# convert the object into a dict
get_all_assets_get_data_assets200_response_inner_dict = get_all_assets_get_data_assets200_response_inner_instance.to_dict()
# create an instance of GetAllAssetsGetDataAssets200ResponseInner from a dict
get_all_assets_get_data_assets200_response_inner_from_dict = GetAllAssetsGetDataAssets200ResponseInner.from_dict(get_all_assets_get_data_assets200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


