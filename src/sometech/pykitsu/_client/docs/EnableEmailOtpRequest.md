# EnableEmailOtpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_otp** | **str** | Email OTP verification code | 

## Example

```python
from sometech.pykitsu._client.models.enable_email_otp_request import EnableEmailOtpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnableEmailOtpRequest from a JSON string
enable_email_otp_request_instance = EnableEmailOtpRequest.from_json(json)
# print the JSON string representation of the object
print(EnableEmailOtpRequest.to_json())

# convert the object into a dict
enable_email_otp_request_dict = enable_email_otp_request_instance.to_dict()
# create an instance of EnableEmailOtpRequest from a dict
enable_email_otp_request_from_dict = EnableEmailOtpRequest.from_dict(enable_email_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


