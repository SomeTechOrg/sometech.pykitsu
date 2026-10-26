# AddHardwareItemToDepartmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hardware_item_id** | **UUID** | Hardware item identifier to add to department | 

## Example

```python
from sometech.pykitsu._client.models.add_hardware_item_to_department_request import AddHardwareItemToDepartmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddHardwareItemToDepartmentRequest from a JSON string
add_hardware_item_to_department_request_instance = AddHardwareItemToDepartmentRequest.from_json(json)
# print the JSON string representation of the object
print(AddHardwareItemToDepartmentRequest.to_json())

# convert the object into a dict
add_hardware_item_to_department_request_dict = add_hardware_item_to_department_request_instance.to_dict()
# create an instance of AddHardwareItemToDepartmentRequest from a dict
add_hardware_item_to_department_request_from_dict = AddHardwareItemToDepartmentRequest.from_dict(add_hardware_item_to_department_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


