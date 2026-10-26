# GetAllDepartmentHardwareItems200ResponseValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Hardware item unique identifier | [optional] 
**name** | **str** | Hardware item name | [optional] 
**description** | **str** | Hardware item description | [optional] 
**department_id** | **UUID** | Department identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_all_department_hardware_items200_response_value_inner import GetAllDepartmentHardwareItems200ResponseValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllDepartmentHardwareItems200ResponseValueInner from a JSON string
get_all_department_hardware_items200_response_value_inner_instance = GetAllDepartmentHardwareItems200ResponseValueInner.from_json(json)
# print the JSON string representation of the object
print(GetAllDepartmentHardwareItems200ResponseValueInner.to_json())

# convert the object into a dict
get_all_department_hardware_items200_response_value_inner_dict = get_all_department_hardware_items200_response_value_inner_instance.to_dict()
# create an instance of GetAllDepartmentHardwareItems200ResponseValueInner from a dict
get_all_department_hardware_items200_response_value_inner_from_dict = GetAllDepartmentHardwareItems200ResponseValueInner.from_dict(get_all_department_hardware_items200_response_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


