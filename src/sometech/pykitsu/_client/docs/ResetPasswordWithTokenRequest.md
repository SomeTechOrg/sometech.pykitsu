# ResetPasswordWithTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email address | 
**token** | **str** | Password reset token | 
**password** | **str** | New password | 
**password2** | **str** | New password confirmation | 

## Example

```python
from sometech.pykitsu._client.models.reset_password_with_token_request import ResetPasswordWithTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResetPasswordWithTokenRequest from a JSON string
reset_password_with_token_request_instance = ResetPasswordWithTokenRequest.from_json(json)
# print the JSON string representation of the object
print(ResetPasswordWithTokenRequest.to_json())

# convert the object into a dict
reset_password_with_token_request_dict = reset_password_with_token_request_instance.to_dict()
# create an instance of ResetPasswordWithTokenRequest from a dict
reset_password_with_token_request_from_dict = ResetPasswordWithTokenRequest.from_dict(reset_password_with_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


