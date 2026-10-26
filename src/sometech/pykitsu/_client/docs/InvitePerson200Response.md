# InvitePerson200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success flag | [optional] 
**message** | **str** | Success message | [optional] 

## Example

```python
from sometech.pykitsu._client.models.invite_person200_response import InvitePerson200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvitePerson200Response from a JSON string
invite_person200_response_instance = InvitePerson200Response.from_json(json)
# print the JSON string representation of the object
print(InvitePerson200Response.to_json())

# convert the object into a dict
invite_person200_response_dict = invite_person200_response_instance.to_dict()
# create an instance of InvitePerson200Response from a dict
invite_person200_response_from_dict = InvitePerson200Response.from_dict(invite_person200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


