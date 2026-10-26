# RegisterNewUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email address | 
**password** | **str** | User password | 
**password_2** | **str** | Password confirmation | 
**first_name** | **str** | User first name | 
**last_name** | **str** | User last name | 

## Example

```python
from sometech.pykitsu._client.models.register_new_user_request import RegisterNewUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterNewUserRequest from a JSON string
register_new_user_request_instance = RegisterNewUserRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterNewUserRequest.to_json())

# convert the object into a dict
register_new_user_request_dict = register_new_user_request_instance.to_dict()
# create an instance of RegisterNewUserRequest from a dict
register_new_user_request_from_dict = RegisterNewUserRequest.from_dict(register_new_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


