# CreatePerson201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**contract_type** | **str** |  | [optional] 
**two_factor_authentication** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_person201_response import CreatePerson201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePerson201Response from a JSON string
create_person201_response_instance = CreatePerson201Response.from_json(json)
# print the JSON string representation of the object
print(CreatePerson201Response.to_json())

# convert the object into a dict
create_person201_response_dict = create_person201_response_instance.to_dict()
# create an instance of CreatePerson201Response from a dict
create_person201_response_from_dict = CreatePerson201Response.from_dict(create_person201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


