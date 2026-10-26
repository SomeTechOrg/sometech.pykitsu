# LoginUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email address | 
**password** | **str** | User password | 
**totp** | **str** | TOTP verification code for two-factor authentication | [optional] 
**email_otp** | **str** | Email OTP verification code for two-factor authentication | [optional] 
**fido_authentication_response** | **object** | FIDO authentication response for WebAuth | [optional] 
**recovery_code** | **str** | Recovery code for two-factor authentication | [optional] 

## Example

```python
from sometech.pykitsu._client.models.login_user_request import LoginUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoginUserRequest from a JSON string
login_user_request_instance = LoginUserRequest.from_json(json)
# print the JSON string representation of the object
print(LoginUserRequest.to_json())

# convert the object into a dict
login_user_request_dict = login_user_request_instance.to_dict()
# create an instance of LoginUserRequest from a dict
login_user_request_from_dict = LoginUserRequest.from_dict(login_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


