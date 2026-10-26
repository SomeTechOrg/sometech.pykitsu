# AddShotAssetInstance201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Shot unique identifier | [optional] 
**name** | **str** | Shot name | [optional] 
**asset_instances** | [**List[AddShotAssetInstance201ResponseAssetInstancesInner]**](AddShotAssetInstance201ResponseAssetInstancesInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.add_shot_asset_instance201_response import AddShotAssetInstance201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddShotAssetInstance201Response from a JSON string
add_shot_asset_instance201_response_instance = AddShotAssetInstance201Response.from_json(json)
# print the JSON string representation of the object
print(AddShotAssetInstance201Response.to_json())

# convert the object into a dict
add_shot_asset_instance201_response_dict = add_shot_asset_instance201_response_instance.to_dict()
# create an instance of AddShotAssetInstance201Response from a dict
add_shot_asset_instance201_response_from_dict = AddShotAssetInstance201Response.from_dict(add_shot_asset_instance201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


