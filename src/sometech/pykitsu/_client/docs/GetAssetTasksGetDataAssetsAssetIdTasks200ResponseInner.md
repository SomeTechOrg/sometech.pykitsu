# GetAssetTasksGetDataAssetsAssetIdTasks200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Task unique identifier | [optional] 
**name** | **str** | Task name | [optional] 
**task_type_id** | **UUID** | Task type identifier | [optional] 
**task_status_id** | **UUID** | Task status identifier | [optional] 
**entity_id** | **UUID** | Asset identifier | [optional] 
**assigned_to** | **UUID** | Assigned user identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_asset_tasks_get_data_assets_asset_id_tasks200_response_inner import GetAssetTasksGetDataAssetsAssetIdTasks200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetTasksGetDataAssetsAssetIdTasks200ResponseInner from a JSON string
get_asset_tasks_get_data_assets_asset_id_tasks200_response_inner_instance = GetAssetTasksGetDataAssetsAssetIdTasks200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetAssetTasksGetDataAssetsAssetIdTasks200ResponseInner.to_json())

# convert the object into a dict
get_asset_tasks_get_data_assets_asset_id_tasks200_response_inner_dict = get_asset_tasks_get_data_assets_asset_id_tasks200_response_inner_instance.to_dict()
# create an instance of GetAssetTasksGetDataAssetsAssetIdTasks200ResponseInner from a dict
get_asset_tasks_get_data_assets_asset_id_tasks200_response_inner_from_dict = GetAssetTasksGetDataAssetsAssetIdTasks200ResponseInner.from_dict(get_asset_tasks_get_data_assets_asset_id_tasks200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


