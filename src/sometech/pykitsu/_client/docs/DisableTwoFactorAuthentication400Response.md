# DisableTwoFactorAuthentication400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **bool** | Error flag | [optional] 
**message** | **str** | Error message | [optional] 

## Example

```python
from sometech.pykitsu._client.models.disable_two_factor_authentication400_response import DisableTwoFactorAuthentication400Response

# TODO update the JSON string below
json = "{}"
# create an instance of DisableTwoFactorAuthentication400Response from a JSON string
disable_two_factor_authentication400_response_instance = DisableTwoFactorAuthentication400Response.from_json(json)
# print the JSON string representation of the object
print(DisableTwoFactorAuthentication400Response.to_json())

# convert the object into a dict
disable_two_factor_authentication400_response_dict = disable_two_factor_authentication400_response_instance.to_dict()
# create an instance of DisableTwoFactorAuthentication400Response from a dict
disable_two_factor_authentication400_response_from_dict = DisableTwoFactorAuthentication400Response.from_dict(disable_two_factor_authentication400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


