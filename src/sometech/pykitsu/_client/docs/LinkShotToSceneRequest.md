# LinkShotToSceneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shot_id** | **UUID** |  | 

## Example

```python
from sometech.pykitsu._client.models.link_shot_to_scene_request import LinkShotToSceneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkShotToSceneRequest from a JSON string
link_shot_to_scene_request_instance = LinkShotToSceneRequest.from_json(json)
# print the JSON string representation of the object
print(LinkShotToSceneRequest.to_json())

# convert the object into a dict
link_shot_to_scene_request_dict = link_shot_to_scene_request_instance.to_dict()
# create an instance of LinkShotToSceneRequest from a dict
link_shot_to_scene_request_from_dict = LinkShotToSceneRequest.from_dict(link_shot_to_scene_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


