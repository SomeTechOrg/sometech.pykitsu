# CreateHardwareItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**serial_number** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_hardware_item_request import CreateHardwareItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHardwareItemRequest from a JSON string
create_hardware_item_request_instance = CreateHardwareItemRequest.from_json(json)
# print the JSON string representation of the object
print(CreateHardwareItemRequest.to_json())

# convert the object into a dict
create_hardware_item_request_dict = create_hardware_item_request_instance.to_dict()
# create an instance of CreateHardwareItemRequest from a dict
create_hardware_item_request_from_dict = CreateHardwareItemRequest.from_dict(create_hardware_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


