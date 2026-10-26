# DisableTotpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totp** | **str** | TOTP verification code | [optional] 
**email_otp** | **str** | Email OTP verification code | [optional] 
**fido_authentication_response** | **object** | FIDO authentication response | [optional] 
**recovery_code** | **str** | Recovery code for two-factor authentication | [optional] 

## Example

```python
from sometech.pykitsu._client.models.disable_totp_request import DisableTotpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisableTotpRequest from a JSON string
disable_totp_request_instance = DisableTotpRequest.from_json(json)
# print the JSON string representation of the object
print(DisableTotpRequest.to_json())

# convert the object into a dict
disable_totp_request_dict = disable_totp_request_instance.to_dict()
# create an instance of DisableTotpRequest from a dict
disable_totp_request_from_dict = DisableTotpRequest.from_dict(disable_totp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


