# AddSoftwareLicenseToDepartment201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Software license department link unique identifier | [optional] 
**department_id** | **UUID** | Department identifier | [optional] 
**software_id** | **UUID** | Software license identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.add_software_license_to_department201_response import AddSoftwareLicenseToDepartment201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddSoftwareLicenseToDepartment201Response from a JSON string
add_software_license_to_department201_response_instance = AddSoftwareLicenseToDepartment201Response.from_json(json)
# print the JSON string representation of the object
print(AddSoftwareLicenseToDepartment201Response.to_json())

# convert the object into a dict
add_software_license_to_department201_response_dict = add_software_license_to_department201_response_instance.to_dict()
# create an instance of AddSoftwareLicenseToDepartment201Response from a dict
add_software_license_to_department201_response_from_dict = AddSoftwareLicenseToDepartment201Response.from_dict(add_software_license_to_department201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


