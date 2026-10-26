# UpdateEntityCastingRequest

Casting data to update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**casting** | [**List[UpdateEntityCastingRequestCastingInner]**](UpdateEntityCastingRequestCastingInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_entity_casting_request import UpdateEntityCastingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEntityCastingRequest from a JSON string
update_entity_casting_request_instance = UpdateEntityCastingRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEntityCastingRequest.to_json())

# convert the object into a dict
update_entity_casting_request_dict = update_entity_casting_request_instance.to_dict()
# create an instance of UpdateEntityCastingRequest from a dict
update_entity_casting_request_from_dict = UpdateEntityCastingRequest.from_dict(update_entity_casting_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


