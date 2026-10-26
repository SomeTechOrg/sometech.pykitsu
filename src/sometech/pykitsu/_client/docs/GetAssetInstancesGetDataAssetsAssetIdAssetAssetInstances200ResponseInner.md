# GetAssetInstancesGetDataAssetsAssetIdAssetAssetInstances200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Asset instance unique identifier | [optional] 
**asset_id** | **UUID** | Parent asset identifier | [optional] 
**target_asset_id** | **UUID** | Target asset identifier | [optional] 
**number** | **str** | Instance number | [optional] 
**description** | **str** | Instance description | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_asset_instances_get_data_assets_asset_id_asset_asset_instances200_response_inner import GetAssetInstancesGetDataAssetsAssetIdAssetAssetInstances200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetInstancesGetDataAssetsAssetIdAssetAssetInstances200ResponseInner from a JSON string
get_asset_instances_get_data_assets_asset_id_asset_asset_instances200_response_inner_instance = GetAssetInstancesGetDataAssetsAssetIdAssetAssetInstances200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetAssetInstancesGetDataAssetsAssetIdAssetAssetInstances200ResponseInner.to_json())

# convert the object into a dict
get_asset_instances_get_data_assets_asset_id_asset_asset_instances200_response_inner_dict = get_asset_instances_get_data_assets_asset_id_asset_asset_instances200_response_inner_instance.to_dict()
# create an instance of GetAssetInstancesGetDataAssetsAssetIdAssetAssetInstances200ResponseInner from a dict
get_asset_instances_get_data_assets_asset_id_asset_asset_instances200_response_inner_from_dict = GetAssetInstancesGetDataAssetsAssetIdAssetAssetInstances200ResponseInner.from_dict(get_asset_instances_get_data_assets_asset_id_asset_asset_instances200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


