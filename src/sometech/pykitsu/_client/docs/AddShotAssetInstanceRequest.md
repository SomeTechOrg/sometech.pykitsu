# AddShotAssetInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_instance_id** | **UUID** | Asset instance identifier to add | 

## Example

```python
from sometech.pykitsu._client.models.add_shot_asset_instance_request import AddShotAssetInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddShotAssetInstanceRequest from a JSON string
add_shot_asset_instance_request_instance = AddShotAssetInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(AddShotAssetInstanceRequest.to_json())

# convert the object into a dict
add_shot_asset_instance_request_dict = add_shot_asset_instance_request_instance.to_dict()
# create an instance of AddShotAssetInstanceRequest from a dict
add_shot_asset_instance_request_from_dict = AddShotAssetInstanceRequest.from_dict(add_shot_asset_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


