# GetAssetCasting200ResponseCastingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Casting entry unique identifier | [optional] 
**entity_id** | **UUID** | Entity identifier (shot/sequence) | [optional] 
**entity_name** | **str** | Entity name | [optional] 
**entity_type** | **str** | Entity type (shot/sequence) | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_asset_casting200_response_casting_inner import GetAssetCasting200ResponseCastingInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetCasting200ResponseCastingInner from a JSON string
get_asset_casting200_response_casting_inner_instance = GetAssetCasting200ResponseCastingInner.from_json(json)
# print the JSON string representation of the object
print(GetAssetCasting200ResponseCastingInner.to_json())

# convert the object into a dict
get_asset_casting200_response_casting_inner_dict = get_asset_casting200_response_casting_inner_instance.to_dict()
# create an instance of GetAssetCasting200ResponseCastingInner from a dict
get_asset_casting200_response_casting_inner_from_dict = GetAssetCasting200ResponseCastingInner.from_dict(get_asset_casting200_response_casting_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


