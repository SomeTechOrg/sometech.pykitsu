# CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstancesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_to_instantiate_id** | **UUID** | Unique identifier of the asset to instantiate | 
**description** | **str** | Description for the asset instance | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_asset_instance_post_data_assets_asset_id_asset_asset_instances_request import CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstancesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstancesRequest from a JSON string
create_asset_instance_post_data_assets_asset_id_asset_asset_instances_request_instance = CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstancesRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstancesRequest.to_json())

# convert the object into a dict
create_asset_instance_post_data_assets_asset_id_asset_asset_instances_request_dict = create_asset_instance_post_data_assets_asset_id_asset_asset_instances_request_instance.to_dict()
# create an instance of CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstancesRequest from a dict
create_asset_instance_post_data_assets_asset_id_asset_asset_instances_request_from_dict = CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstancesRequest.from_dict(create_asset_instance_post_data_assets_asset_id_asset_asset_instances_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


