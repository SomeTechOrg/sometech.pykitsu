# EnableTotpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totp** | **str** | TOTP verification code from authenticator app | 

## Example

```python
from sometech.pykitsu._client.models.enable_totp_request import EnableTotpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnableTotpRequest from a JSON string
enable_totp_request_instance = EnableTotpRequest.from_json(json)
# print the JSON string representation of the object
print(EnableTotpRequest.to_json())

# convert the object into a dict
enable_totp_request_dict = enable_totp_request_instance.to_dict()
# create an instance of EnableTotpRequest from a dict
enable_totp_request_from_dict = EnableTotpRequest.from_dict(enable_totp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


