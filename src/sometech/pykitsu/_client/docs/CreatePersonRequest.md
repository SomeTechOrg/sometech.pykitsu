# CreatePersonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**password** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**active** | **bool** |  | [optional] [default to True]
**contract_type** | **str** |  | [optional] 
**two_factor_authentication** | **str** |  | [optional] 
**expiration_date** | **date** |  | [optional] 
**is_bot** | **bool** |  | [optional] [default to False]

## Example

```python
from sometech.pykitsu._client.models.create_person_request import CreatePersonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePersonRequest from a JSON string
create_person_request_instance = CreatePersonRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePersonRequest.to_json())

# convert the object into a dict
create_person_request_dict = create_person_request_instance.to_dict()
# create an instance of CreatePersonRequest from a dict
create_person_request_from_dict = CreatePersonRequest.from_dict(create_person_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


