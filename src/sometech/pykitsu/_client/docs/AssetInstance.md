# AssetInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** | Instantiated asset | [optional] 
**name** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**active** | **bool** |  | [optional] [default to True]
**data** | **str** | Free JSON field to add metadata | [optional] 
**scene_id** | **UUID** | Target scene | [optional] 
**target_asset_id** | **UUID** | Use when instantiating an asset in an asset is required | [optional] 

## Example

```python
from sometech.pykitsu._client.models.asset_instance import AssetInstance

# TODO update the JSON string below
json = "{}"
# create an instance of AssetInstance from a JSON string
asset_instance_instance = AssetInstance.from_json(json)
# print the JSON string representation of the object
print(AssetInstance.to_json())

# convert the object into a dict
asset_instance_dict = asset_instance_instance.to_dict()
# create an instance of AssetInstance from a dict
asset_instance_from_dict = AssetInstance.from_dict(asset_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


