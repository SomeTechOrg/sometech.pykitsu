# RemoveShotgunSceneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the scene to remove | 

## Example

```python
from sometech.pykitsu._client.models.remove_shotgun_scene_request import RemoveShotgunSceneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveShotgunSceneRequest from a JSON string
remove_shotgun_scene_request_instance = RemoveShotgunSceneRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveShotgunSceneRequest.to_json())

# convert the object into a dict
remove_shotgun_scene_request_dict = remove_shotgun_scene_request_instance.to_dict()
# create an instance of RemoveShotgunSceneRequest from a dict
remove_shotgun_scene_request_from_dict = RemoveShotgunSceneRequest.from_dict(remove_shotgun_scene_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


