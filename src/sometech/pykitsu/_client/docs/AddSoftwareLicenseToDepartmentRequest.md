# AddSoftwareLicenseToDepartmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**software_id** | **UUID** | Software identifier to add to department | 

## Example

```python
from sometech.pykitsu._client.models.add_software_license_to_department_request import AddSoftwareLicenseToDepartmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddSoftwareLicenseToDepartmentRequest from a JSON string
add_software_license_to_department_request_instance = AddSoftwareLicenseToDepartmentRequest.from_json(json)
# print the JSON string representation of the object
print(AddSoftwareLicenseToDepartmentRequest.to_json())

# convert the object into a dict
add_software_license_to_department_request_dict = add_software_license_to_department_request_instance.to_dict()
# create an instance of AddSoftwareLicenseToDepartmentRequest from a dict
add_software_license_to_department_request_from_dict = AddSoftwareLicenseToDepartmentRequest.from_dict(add_software_license_to_department_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


