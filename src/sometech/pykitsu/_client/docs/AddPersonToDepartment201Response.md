# AddPersonToDepartment201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Person unique identifier | [optional] 
**department_id** | **UUID** | Department unique identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.add_person_to_department201_response import AddPersonToDepartment201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddPersonToDepartment201Response from a JSON string
add_person_to_department201_response_instance = AddPersonToDepartment201Response.from_json(json)
# print the JSON string representation of the object
print(AddPersonToDepartment201Response.to_json())

# convert the object into a dict
add_person_to_department201_response_dict = add_person_to_department201_response_instance.to_dict()
# create an instance of AddPersonToDepartment201Response from a dict
add_person_to_department201_response_from_dict = AddPersonToDepartment201Response.from_dict(add_person_to_department201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


