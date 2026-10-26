# GetEntityCasting200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **UUID** | Entity unique identifier | [optional] 
**casting** | [**List[GetEntityCasting200ResponseCastingInner]**](GetEntityCasting200ResponseCastingInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_entity_casting200_response import GetEntityCasting200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityCasting200Response from a JSON string
get_entity_casting200_response_instance = GetEntityCasting200Response.from_json(json)
# print the JSON string representation of the object
print(GetEntityCasting200Response.to_json())

# convert the object into a dict
get_entity_casting200_response_dict = get_entity_casting200_response_instance.to_dict()
# create an instance of GetEntityCasting200Response from a dict
get_entity_casting200_response_from_dict = GetEntityCasting200Response.from_dict(get_entity_casting200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


