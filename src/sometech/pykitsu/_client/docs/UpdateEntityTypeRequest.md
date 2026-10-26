# UpdateEntityTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_entity_type_request import UpdateEntityTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEntityTypeRequest from a JSON string
update_entity_type_request_instance = UpdateEntityTypeRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEntityTypeRequest.to_json())

# convert the object into a dict
update_entity_type_request_dict = update_entity_type_request_instance.to_dict()
# create an instance of UpdateEntityTypeRequest from a dict
update_entity_type_request_from_dict = UpdateEntityTypeRequest.from_dict(update_entity_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


