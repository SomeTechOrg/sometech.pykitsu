# ChangePersonPassword400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **bool** | Error flag | [optional] 
**message** | **str** | Error message | [optional] 

## Example

```python
from sometech.pykitsu._client.models.change_person_password400_response import ChangePersonPassword400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePersonPassword400Response from a JSON string
change_person_password400_response_instance = ChangePersonPassword400Response.from_json(json)
# print the JSON string representation of the object
print(ChangePersonPassword400Response.to_json())

# convert the object into a dict
change_person_password400_response_dict = change_person_password400_response_instance.to_dict()
# create an instance of ChangePersonPassword400Response from a dict
change_person_password400_response_from_dict = ChangePersonPassword400Response.from_dict(change_person_password400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


