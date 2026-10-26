# SetAssetTypeAssetsSharedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_shared** | **bool** | Whether to share or unshare the assets | [optional] 

## Example

```python
from sometech.pykitsu._client.models.set_asset_type_assets_shared_request import SetAssetTypeAssetsSharedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetAssetTypeAssetsSharedRequest from a JSON string
set_asset_type_assets_shared_request_instance = SetAssetTypeAssetsSharedRequest.from_json(json)
# print the JSON string representation of the object
print(SetAssetTypeAssetsSharedRequest.to_json())

# convert the object into a dict
set_asset_type_assets_shared_request_dict = set_asset_type_assets_shared_request_instance.to_dict()
# create an instance of SetAssetTypeAssetsSharedRequest from a dict
set_asset_type_assets_shared_request_from_dict = SetAssetTypeAssetsSharedRequest.from_dict(set_asset_type_assets_shared_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


