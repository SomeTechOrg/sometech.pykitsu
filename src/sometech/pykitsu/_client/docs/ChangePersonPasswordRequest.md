# ChangePersonPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | New password | 
**password_2** | **str** | Password confirmation | 

## Example

```python
from sometech.pykitsu._client.models.change_person_password_request import ChangePersonPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePersonPasswordRequest from a JSON string
change_person_password_request_instance = ChangePersonPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(ChangePersonPasswordRequest.to_json())

# convert the object into a dict
change_person_password_request_dict = change_person_password_request_instance.to_dict()
# create an instance of ChangePersonPasswordRequest from a dict
change_person_password_request_from_dict = ChangePersonPasswordRequest.from_dict(change_person_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


