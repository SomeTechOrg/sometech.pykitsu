# GetProjectAssetsGetDataUserProjectsProjectIdAssetTypesAssetTypeIdAssets200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Asset unique identifier | [optional] 
**name** | **str** | Asset name | [optional] 
**description** | **str** | Asset description | [optional] 
**asset_type_id** | **UUID** | Asset type identifier | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_project_assets_get_data_user_projects_project_id_asset_types_asset_type_id_assets200_response_inner import GetProjectAssetsGetDataUserProjectsProjectIdAssetTypesAssetTypeIdAssets200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectAssetsGetDataUserProjectsProjectIdAssetTypesAssetTypeIdAssets200ResponseInner from a JSON string
get_project_assets_get_data_user_projects_project_id_asset_types_asset_type_id_assets200_response_inner_instance = GetProjectAssetsGetDataUserProjectsProjectIdAssetTypesAssetTypeIdAssets200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectAssetsGetDataUserProjectsProjectIdAssetTypesAssetTypeIdAssets200ResponseInner.to_json())

# convert the object into a dict
get_project_assets_get_data_user_projects_project_id_asset_types_asset_type_id_assets200_response_inner_dict = get_project_assets_get_data_user_projects_project_id_asset_types_asset_type_id_assets200_response_inner_instance.to_dict()
# create an instance of GetProjectAssetsGetDataUserProjectsProjectIdAssetTypesAssetTypeIdAssets200ResponseInner from a dict
get_project_assets_get_data_user_projects_project_id_asset_types_asset_type_id_assets200_response_inner_from_dict = GetProjectAssetsGetDataUserProjectsProjectIdAssetTypesAssetTypeIdAssets200ResponseInner.from_dict(get_project_assets_get_data_user_projects_project_id_asset_types_asset_type_id_assets200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


