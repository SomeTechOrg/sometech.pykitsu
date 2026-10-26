# UpdateHardwareItem200Response


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
from sometech.pykitsu._client.models.update_hardware_item200_response import UpdateHardwareItem200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHardwareItem200Response from a JSON string
update_hardware_item200_response_instance = UpdateHardwareItem200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateHardwareItem200Response.to_json())

# convert the object into a dict
update_hardware_item200_response_dict = update_hardware_item200_response_instance.to_dict()
# create an instance of UpdateHardwareItem200Response from a dict
update_hardware_item200_response_from_dict = UpdateHardwareItem200Response.from_dict(update_hardware_item200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


