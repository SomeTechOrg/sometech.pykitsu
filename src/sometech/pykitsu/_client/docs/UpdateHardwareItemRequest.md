# UpdateHardwareItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_hardware_item_request import UpdateHardwareItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHardwareItemRequest from a JSON string
update_hardware_item_request_instance = UpdateHardwareItemRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateHardwareItemRequest.to_json())

# convert the object into a dict
update_hardware_item_request_dict = update_hardware_item_request_instance.to_dict()
# create an instance of UpdateHardwareItemRequest from a dict
update_hardware_item_request_from_dict = UpdateHardwareItemRequest.from_dict(update_hardware_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


