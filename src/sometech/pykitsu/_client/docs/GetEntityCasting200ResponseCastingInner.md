# GetEntityCasting200ResponseCastingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Casting entry unique identifier | [optional] 
**asset_id** | **UUID** | Asset identifier | [optional] 
**asset_name** | **str** | Asset name | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_entity_casting200_response_casting_inner import GetEntityCasting200ResponseCastingInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityCasting200ResponseCastingInner from a JSON string
get_entity_casting200_response_casting_inner_instance = GetEntityCasting200ResponseCastingInner.from_json(json)
# print the JSON string representation of the object
print(GetEntityCasting200ResponseCastingInner.to_json())

# convert the object into a dict
get_entity_casting200_response_casting_inner_dict = get_entity_casting200_response_casting_inner_instance.to_dict()
# create an instance of GetEntityCasting200ResponseCastingInner from a dict
get_entity_casting200_response_casting_inner_from_dict = GetEntityCasting200ResponseCastingInner.from_dict(get_entity_casting200_response_casting_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


