# UpdateAssetInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_asset_instance_request import UpdateAssetInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAssetInstanceRequest from a JSON string
update_asset_instance_request_instance = UpdateAssetInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAssetInstanceRequest.to_json())

# convert the object into a dict
update_asset_instance_request_dict = update_asset_instance_request_instance.to_dict()
# create an instance of UpdateAssetInstanceRequest from a dict
update_asset_instance_request_from_dict = UpdateAssetInstanceRequest.from_dict(update_asset_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


