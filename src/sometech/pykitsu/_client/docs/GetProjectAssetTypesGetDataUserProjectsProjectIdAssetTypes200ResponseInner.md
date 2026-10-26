# GetProjectAssetTypesGetDataUserProjectsProjectIdAssetTypes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Asset type unique identifier | [optional] 
**name** | **str** | Asset type name | [optional] 
**short_name** | **str** | Asset type short name | [optional] 
**color** | **str** | Asset type color | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_project_asset_types_get_data_user_projects_project_id_asset_types200_response_inner import GetProjectAssetTypesGetDataUserProjectsProjectIdAssetTypes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectAssetTypesGetDataUserProjectsProjectIdAssetTypes200ResponseInner from a JSON string
get_project_asset_types_get_data_user_projects_project_id_asset_types200_response_inner_instance = GetProjectAssetTypesGetDataUserProjectsProjectIdAssetTypes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectAssetTypesGetDataUserProjectsProjectIdAssetTypes200ResponseInner.to_json())

# convert the object into a dict
get_project_asset_types_get_data_user_projects_project_id_asset_types200_response_inner_dict = get_project_asset_types_get_data_user_projects_project_id_asset_types200_response_inner_instance.to_dict()
# create an instance of GetProjectAssetTypesGetDataUserProjectsProjectIdAssetTypes200ResponseInner from a dict
get_project_asset_types_get_data_user_projects_project_id_asset_types200_response_inner_from_dict = GetProjectAssetTypesGetDataUserProjectsProjectIdAssetTypes200ResponseInner.from_dict(get_project_asset_types_get_data_user_projects_project_id_asset_types200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


