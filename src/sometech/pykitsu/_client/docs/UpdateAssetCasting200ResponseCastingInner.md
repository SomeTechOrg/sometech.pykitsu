# UpdateAssetCasting200ResponseCastingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Casting entry unique identifier | [optional] 
**entity_id** | **UUID** | Entity identifier | [optional] 
**entity_name** | **str** | Entity name | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_asset_casting200_response_casting_inner import UpdateAssetCasting200ResponseCastingInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAssetCasting200ResponseCastingInner from a JSON string
update_asset_casting200_response_casting_inner_instance = UpdateAssetCasting200ResponseCastingInner.from_json(json)
# print the JSON string representation of the object
print(UpdateAssetCasting200ResponseCastingInner.to_json())

# convert the object into a dict
update_asset_casting200_response_casting_inner_dict = update_asset_casting200_response_casting_inner_instance.to_dict()
# create an instance of UpdateAssetCasting200ResponseCastingInner from a dict
update_asset_casting200_response_casting_inner_from_dict = UpdateAssetCasting200ResponseCastingInner.from_dict(update_asset_casting200_response_casting_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


