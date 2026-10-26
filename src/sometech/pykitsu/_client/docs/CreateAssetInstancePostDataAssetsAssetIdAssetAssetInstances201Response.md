# CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstances201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Created asset instance unique identifier | [optional] 
**asset_id** | **UUID** | Parent asset identifier | [optional] 
**target_asset_id** | **UUID** | Target asset identifier | [optional] 
**number** | **str** | Instance number | [optional] 
**description** | **str** | Instance description | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_asset_instance_post_data_assets_asset_id_asset_asset_instances201_response import CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstances201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstances201Response from a JSON string
create_asset_instance_post_data_assets_asset_id_asset_asset_instances201_response_instance = CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstances201Response.from_json(json)
# print the JSON string representation of the object
print(CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstances201Response.to_json())

# convert the object into a dict
create_asset_instance_post_data_assets_asset_id_asset_asset_instances201_response_dict = create_asset_instance_post_data_assets_asset_id_asset_asset_instances201_response_instance.to_dict()
# create an instance of CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstances201Response from a dict
create_asset_instance_post_data_assets_asset_id_asset_asset_instances201_response_from_dict = CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstances201Response.from_dict(create_asset_instance_post_data_assets_asset_id_asset_asset_instances201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


