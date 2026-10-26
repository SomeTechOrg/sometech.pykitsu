# CreateEntityTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**color** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_entity_type_request import CreateEntityTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntityTypeRequest from a JSON string
create_entity_type_request_instance = CreateEntityTypeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEntityTypeRequest.to_json())

# convert the object into a dict
create_entity_type_request_dict = create_entity_type_request_instance.to_dict()
# create an instance of CreateEntityTypeRequest from a dict
create_entity_type_request_from_dict = CreateEntityTypeRequest.from_dict(create_entity_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


