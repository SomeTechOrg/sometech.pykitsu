# CreateProjectSceneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**sequence_id** | **UUID** |  | 

## Example

```python
from sometech.pykitsu._client.models.create_project_scene_request import CreateProjectSceneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectSceneRequest from a JSON string
create_project_scene_request_instance = CreateProjectSceneRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectSceneRequest.to_json())

# convert the object into a dict
create_project_scene_request_dict = create_project_scene_request_instance.to_dict()
# create an instance of CreateProjectSceneRequest from a dict
create_project_scene_request_from_dict = CreateProjectSceneRequest.from_dict(create_project_scene_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


