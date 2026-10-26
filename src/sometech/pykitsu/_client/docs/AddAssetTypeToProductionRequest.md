# AddAssetTypeToProductionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_type_id** | **UUID** | Asset type unique identifier | 

## Example

```python
from sometech.pykitsu._client.models.add_asset_type_to_production_request import AddAssetTypeToProductionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddAssetTypeToProductionRequest from a JSON string
add_asset_type_to_production_request_instance = AddAssetTypeToProductionRequest.from_json(json)
# print the JSON string representation of the object
print(AddAssetTypeToProductionRequest.to_json())

# convert the object into a dict
add_asset_type_to_production_request_dict = add_asset_type_to_production_request_instance.to_dict()
# create an instance of AddAssetTypeToProductionRequest from a dict
add_asset_type_to_production_request_from_dict = AddAssetTypeToProductionRequest.from_dict(add_asset_type_to_production_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


