# UpdateAssetCastingRequestCastingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **UUID** | Entity identifier to cast | [optional] 
**entity_type** | **str** | Entity type (shot/sequence) | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_asset_casting_request_casting_inner import UpdateAssetCastingRequestCastingInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAssetCastingRequestCastingInner from a JSON string
update_asset_casting_request_casting_inner_instance = UpdateAssetCastingRequestCastingInner.from_json(json)
# print the JSON string representation of the object
print(UpdateAssetCastingRequestCastingInner.to_json())

# convert the object into a dict
update_asset_casting_request_casting_inner_dict = update_asset_casting_request_casting_inner_instance.to_dict()
# create an instance of UpdateAssetCastingRequestCastingInner from a dict
update_asset_casting_request_casting_inner_from_dict = UpdateAssetCastingRequestCastingInner.from_dict(update_asset_casting_request_casting_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


