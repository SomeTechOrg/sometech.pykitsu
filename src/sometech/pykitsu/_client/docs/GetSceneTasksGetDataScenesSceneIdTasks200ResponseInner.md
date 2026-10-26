# GetSceneTasksGetDataScenesSceneIdTasks200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**task_type_id** | **UUID** |  | [optional] 
**task_status_id** | **UUID** |  | [optional] 
**entity_id** | **UUID** |  | [optional] 
**project_id** | **UUID** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_scene_tasks_get_data_scenes_scene_id_tasks200_response_inner import GetSceneTasksGetDataScenesSceneIdTasks200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSceneTasksGetDataScenesSceneIdTasks200ResponseInner from a JSON string
get_scene_tasks_get_data_scenes_scene_id_tasks200_response_inner_instance = GetSceneTasksGetDataScenesSceneIdTasks200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetSceneTasksGetDataScenesSceneIdTasks200ResponseInner.to_json())

# convert the object into a dict
get_scene_tasks_get_data_scenes_scene_id_tasks200_response_inner_dict = get_scene_tasks_get_data_scenes_scene_id_tasks200_response_inner_instance.to_dict()
# create an instance of GetSceneTasksGetDataScenesSceneIdTasks200ResponseInner from a dict
get_scene_tasks_get_data_scenes_scene_id_tasks200_response_inner_from_dict = GetSceneTasksGetDataScenesSceneIdTasks200ResponseInner.from_dict(get_scene_tasks_get_data_scenes_scene_id_tasks200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


