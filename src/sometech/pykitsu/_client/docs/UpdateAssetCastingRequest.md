# UpdateAssetCastingRequest

Casting data to update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**casting** | [**List[UpdateAssetCastingRequestCastingInner]**](UpdateAssetCastingRequestCastingInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_asset_casting_request import UpdateAssetCastingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAssetCastingRequest from a JSON string
update_asset_casting_request_instance = UpdateAssetCastingRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAssetCastingRequest.to_json())

# convert the object into a dict
update_asset_casting_request_dict = update_asset_casting_request_instance.to_dict()
# create an instance of UpdateAssetCastingRequest from a dict
update_asset_casting_request_from_dict = UpdateAssetCastingRequest.from_dict(update_asset_casting_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


