# GetAssetTypeCasting200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** | Asset unique identifier | [optional] 
**asset_name** | **str** | Asset name | [optional] 
**asset_type_id** | **UUID** | Asset type identifier | [optional] 
**casting** | [**List[GetAssetTypeCasting200ResponseInnerCastingInner]**](GetAssetTypeCasting200ResponseInnerCastingInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_asset_type_casting200_response_inner import GetAssetTypeCasting200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetTypeCasting200ResponseInner from a JSON string
get_asset_type_casting200_response_inner_instance = GetAssetTypeCasting200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetAssetTypeCasting200ResponseInner.to_json())

# convert the object into a dict
get_asset_type_casting200_response_inner_dict = get_asset_type_casting200_response_inner_instance.to_dict()
# create an instance of GetAssetTypeCasting200ResponseInner from a dict
get_asset_type_casting200_response_inner_from_dict = GetAssetTypeCasting200ResponseInner.from_dict(get_asset_type_casting200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


