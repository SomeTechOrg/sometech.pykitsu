# RegisterFidoDeviceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_response** | **object** | FIDO device registration response | 
**device_name** | **str** | Name for the FIDO device | 

## Example

```python
from sometech.pykitsu._client.models.register_fido_device_request import RegisterFidoDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterFidoDeviceRequest from a JSON string
register_fido_device_request_instance = RegisterFidoDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterFidoDeviceRequest.to_json())

# convert the object into a dict
register_fido_device_request_dict = register_fido_device_request_instance.to_dict()
# create an instance of RegisterFidoDeviceRequest from a dict
register_fido_device_request_from_dict = RegisterFidoDeviceRequest.from_dict(register_fido_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


