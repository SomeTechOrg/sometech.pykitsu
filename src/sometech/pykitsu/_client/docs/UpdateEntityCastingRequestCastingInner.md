# UpdateEntityCastingRequestCastingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** | Asset identifier to link | [optional] 
**asset_name** | **str** | Asset name | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_entity_casting_request_casting_inner import UpdateEntityCastingRequestCastingInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEntityCastingRequestCastingInner from a JSON string
update_entity_casting_request_casting_inner_instance = UpdateEntityCastingRequestCastingInner.from_json(json)
# print the JSON string representation of the object
print(UpdateEntityCastingRequestCastingInner.to_json())

# convert the object into a dict
update_entity_casting_request_casting_inner_dict = update_entity_casting_request_casting_inner_instance.to_dict()
# create an instance of UpdateEntityCastingRequestCastingInner from a dict
update_entity_casting_request_casting_inner_from_dict = UpdateEntityCastingRequestCastingInner.from_dict(update_entity_casting_request_casting_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


