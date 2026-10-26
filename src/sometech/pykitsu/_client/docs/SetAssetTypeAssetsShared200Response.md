# SetAssetTypeAssetsShared200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_count** | **int** | Number of assets updated | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**asset_type_id** | **UUID** | Asset type identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.set_asset_type_assets_shared200_response import SetAssetTypeAssetsShared200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetAssetTypeAssetsShared200Response from a JSON string
set_asset_type_assets_shared200_response_instance = SetAssetTypeAssetsShared200Response.from_json(json)
# print the JSON string representation of the object
print(SetAssetTypeAssetsShared200Response.to_json())

# convert the object into a dict
set_asset_type_assets_shared200_response_dict = set_asset_type_assets_shared200_response_instance.to_dict()
# create an instance of SetAssetTypeAssetsShared200Response from a dict
set_asset_type_assets_shared200_response_from_dict = SetAssetTypeAssetsShared200Response.from_dict(set_asset_type_assets_shared200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


