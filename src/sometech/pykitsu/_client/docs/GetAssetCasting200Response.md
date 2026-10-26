# GetAssetCasting200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** | Asset unique identifier | [optional] 
**casting** | [**List[GetAssetCasting200ResponseCastingInner]**](GetAssetCasting200ResponseCastingInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_asset_casting200_response import GetAssetCasting200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetCasting200Response from a JSON string
get_asset_casting200_response_instance = GetAssetCasting200Response.from_json(json)
# print the JSON string representation of the object
print(GetAssetCasting200Response.to_json())

# convert the object into a dict
get_asset_casting200_response_dict = get_asset_casting200_response_instance.to_dict()
# create an instance of GetAssetCasting200Response from a dict
get_asset_casting200_response_from_dict = GetAssetCasting200Response.from_dict(get_asset_casting200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


