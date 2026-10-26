# AddPersonToDepartmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**department_id** | **UUID** | Department unique identifier | 

## Example

```python
from sometech.pykitsu._client.models.add_person_to_department_request import AddPersonToDepartmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddPersonToDepartmentRequest from a JSON string
add_person_to_department_request_instance = AddPersonToDepartmentRequest.from_json(json)
# print the JSON string representation of the object
print(AddPersonToDepartmentRequest.to_json())

# convert the object into a dict
add_person_to_department_request_dict = add_person_to_department_request_instance.to_dict()
# create an instance of AddPersonToDepartmentRequest from a dict
add_person_to_department_request_from_dict = AddPersonToDepartmentRequest.from_dict(add_person_to_department_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


