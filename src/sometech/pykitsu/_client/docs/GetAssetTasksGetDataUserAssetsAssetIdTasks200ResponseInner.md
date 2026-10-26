# GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Task unique identifier | [optional] 
**name** | **str** | Task name | [optional] 
**task_type_id** | **UUID** | Task type identifier | [optional] 
**task_status_id** | **UUID** | Task status identifier | [optional] 
**assigner_id** | **UUID** | Person who assigned the task | [optional] 
**assignees** | **List[UUID]** | List of assigned person identifiers | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_asset_tasks_get_data_user_assets_asset_id_tasks200_response_inner import GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner from a JSON string
get_asset_tasks_get_data_user_assets_asset_id_tasks200_response_inner_instance = GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner.to_json())

# convert the object into a dict
get_asset_tasks_get_data_user_assets_asset_id_tasks200_response_inner_dict = get_asset_tasks_get_data_user_assets_asset_id_tasks200_response_inner_instance.to_dict()
# create an instance of GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner from a dict
get_asset_tasks_get_data_user_assets_asset_id_tasks200_response_inner_from_dict = GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner.from_dict(get_asset_tasks_get_data_user_assets_asset_id_tasks200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


