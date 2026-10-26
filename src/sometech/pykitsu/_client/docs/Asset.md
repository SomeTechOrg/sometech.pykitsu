# Asset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of asset | [optional] 
**code** | **str** | Utility field for the pipeline to identify the asset | [optional] 
**description** | **str** | Asset brief | [optional] 
**canceled** | **bool** | True if the asset has been delete one time, False otherwise | [optional] [default to False]
**project_id** | **UUID** | Project ID | [optional] 
**entity_type_id** | **UUID** | Asset type ID | [optional] 
**source_id** | **UUID** | Field used to set the episode_id | [optional] 
**preview_file_id** | **UUID** | ID of preview file used as thumbnail | [optional] 
**data** | **str** | Free JSON field to add metadata | [optional] 
**shotgun_id** | **int** | Used for synchronization with a Shotgun instance | [optional] 
**id** | **UUID** | Linked asset unique identifier | [optional] 
**is_shared** | **bool** | Whether the asset is shared | [optional] 

## Example

```python
from sometech.pykitsu._client.models.asset import Asset

# TODO update the JSON string below
json = "{}"
# create an instance of Asset from a JSON string
asset_instance = Asset.from_json(json)
# print the JSON string representation of the object
print(Asset.to_json())

# convert the object into a dict
asset_dict = asset_instance.to_dict()
# create an instance of Asset from a dict
asset_from_dict = Asset.from_dict(asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


