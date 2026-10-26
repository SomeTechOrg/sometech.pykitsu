# GetAllDepartmentSoftwareLicenses200ResponseValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Software license unique identifier | [optional] 
**name** | **str** | Software license name | [optional] 
**short_name** | **str** | Software license short name | [optional] 
**file_extension** | **str** | Default file extension for the software license | [optional] 
**department_id** | **UUID** | Department identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_all_department_software_licenses200_response_value_inner import GetAllDepartmentSoftwareLicenses200ResponseValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllDepartmentSoftwareLicenses200ResponseValueInner from a JSON string
get_all_department_software_licenses200_response_value_inner_instance = GetAllDepartmentSoftwareLicenses200ResponseValueInner.from_json(json)
# print the JSON string representation of the object
print(GetAllDepartmentSoftwareLicenses200ResponseValueInner.to_json())

# convert the object into a dict
get_all_department_software_licenses200_response_value_inner_dict = get_all_department_software_licenses200_response_value_inner_instance.to_dict()
# create an instance of GetAllDepartmentSoftwareLicenses200ResponseValueInner from a dict
get_all_department_software_licenses200_response_value_inner_from_dict = GetAllDepartmentSoftwareLicenses200ResponseValueInner.from_dict(get_all_department_software_licenses200_response_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


