# CreateSceneAssetInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** | Asset identifier to create instance from | 
**description** | **str** | Instance description | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_scene_asset_instance_request import CreateSceneAssetInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSceneAssetInstanceRequest from a JSON string
create_scene_asset_instance_request_instance = CreateSceneAssetInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSceneAssetInstanceRequest.to_json())

# convert the object into a dict
create_scene_asset_instance_request_dict = create_scene_asset_instance_request_instance.to_dict()
# create an instance of CreateSceneAssetInstanceRequest from a dict
create_scene_asset_instance_request_from_dict = CreateSceneAssetInstanceRequest.from_dict(create_scene_asset_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


