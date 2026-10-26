# GetAssetTypeCasting200ResponseInnerCastingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **UUID** | Entity identifier | [optional] 
**entity_name** | **str** | Entity name | [optional] 
**entity_type** | **str** | Entity type (shot/sequence) | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_asset_type_casting200_response_inner_casting_inner import GetAssetTypeCasting200ResponseInnerCastingInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetTypeCasting200ResponseInnerCastingInner from a JSON string
get_asset_type_casting200_response_inner_casting_inner_instance = GetAssetTypeCasting200ResponseInnerCastingInner.from_json(json)
# print the JSON string representation of the object
print(GetAssetTypeCasting200ResponseInnerCastingInner.to_json())

# convert the object into a dict
get_asset_type_casting200_response_inner_casting_inner_dict = get_asset_type_casting200_response_inner_casting_inner_instance.to_dict()
# create an instance of GetAssetTypeCasting200ResponseInnerCastingInner from a dict
get_asset_type_casting200_response_inner_casting_inner_from_dict = GetAssetTypeCasting200ResponseInnerCastingInner.from_dict(get_asset_type_casting200_response_inner_casting_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


