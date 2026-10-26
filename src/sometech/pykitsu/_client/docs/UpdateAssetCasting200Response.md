# UpdateAssetCasting200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** | Asset unique identifier | [optional] 
**casting** | [**List[UpdateAssetCasting200ResponseCastingInner]**](UpdateAssetCasting200ResponseCastingInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_asset_casting200_response import UpdateAssetCasting200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAssetCasting200Response from a JSON string
update_asset_casting200_response_instance = UpdateAssetCasting200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateAssetCasting200Response.to_json())

# convert the object into a dict
update_asset_casting200_response_dict = update_asset_casting200_response_instance.to_dict()
# create an instance of UpdateAssetCasting200Response from a dict
update_asset_casting200_response_from_dict = UpdateAssetCasting200Response.from_dict(update_asset_casting200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


