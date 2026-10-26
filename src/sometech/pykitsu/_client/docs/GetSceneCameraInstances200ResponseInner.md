# GetSceneCameraInstances200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Camera instance unique identifier | [optional] 
**camera_id** | **UUID** | Camera identifier | [optional] 
**scene_id** | **UUID** | Scene identifier | [optional] 
**number** | **str** | Instance number | [optional] 
**description** | **str** | Instance description | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_scene_camera_instances200_response_inner import GetSceneCameraInstances200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSceneCameraInstances200ResponseInner from a JSON string
get_scene_camera_instances200_response_inner_instance = GetSceneCameraInstances200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetSceneCameraInstances200ResponseInner.to_json())

# convert the object into a dict
get_scene_camera_instances200_response_inner_dict = get_scene_camera_instances200_response_inner_instance.to_dict()
# create an instance of GetSceneCameraInstances200ResponseInner from a dict
get_scene_camera_instances200_response_inner_from_dict = GetSceneCameraInstances200ResponseInner.from_dict(get_scene_camera_instances200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


