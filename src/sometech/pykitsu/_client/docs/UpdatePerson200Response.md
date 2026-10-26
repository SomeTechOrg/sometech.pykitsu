# UpdatePerson200Response


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
**departments** | **List[UUID]** |  | [optional] 
**access_token** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_person200_response import UpdatePerson200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePerson200Response from a JSON string
update_person200_response_instance = UpdatePerson200Response.from_json(json)
# print the JSON string representation of the object
print(UpdatePerson200Response.to_json())

# convert the object into a dict
update_person200_response_dict = update_person200_response_instance.to_dict()
# create an instance of UpdatePerson200Response from a dict
update_person200_response_from_dict = UpdatePerson200Response.from_dict(update_person200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


