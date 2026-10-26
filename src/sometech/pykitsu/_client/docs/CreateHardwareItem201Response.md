# CreateHardwareItem201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_hardware_item201_response import CreateHardwareItem201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHardwareItem201Response from a JSON string
create_hardware_item201_response_instance = CreateHardwareItem201Response.from_json(json)
# print the JSON string representation of the object
print(CreateHardwareItem201Response.to_json())

# convert the object into a dict
create_hardware_item201_response_dict = create_hardware_item201_response_instance.to_dict()
# create an instance of CreateHardwareItem201Response from a dict
create_hardware_item201_response_from_dict = CreateHardwareItem201Response.from_dict(create_hardware_item201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


