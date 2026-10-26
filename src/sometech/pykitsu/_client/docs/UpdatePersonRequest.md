# UpdatePersonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**role** | **str** | Admin only | [optional] 
**active** | **bool** | Admin only | [optional] 
**contract_type** | **str** |  | [optional] 
**two_factor_authentication** | **str** |  | [optional] 
**expiration_date** | **date** | Person or admin only | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_person_request import UpdatePersonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePersonRequest from a JSON string
update_person_request_instance = UpdatePersonRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePersonRequest.to_json())

# convert the object into a dict
update_person_request_dict = update_person_request_instance.to_dict()
# create an instance of UpdatePersonRequest from a dict
update_person_request_from_dict = UpdatePersonRequest.from_dict(update_person_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


