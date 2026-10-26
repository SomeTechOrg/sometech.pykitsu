# UnregisterFidoDeviceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | Name of the FIDO device to unregister | 

## Example

```python
from sometech.pykitsu._client.models.unregister_fido_device_request import UnregisterFidoDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnregisterFidoDeviceRequest from a JSON string
unregister_fido_device_request_instance = UnregisterFidoDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(UnregisterFidoDeviceRequest.to_json())

# convert the object into a dict
unregister_fido_device_request_dict = unregister_fido_device_request_instance.to_dict()
# create an instance of UnregisterFidoDeviceRequest from a dict
unregister_fido_device_request_from_dict = UnregisterFidoDeviceRequest.from_dict(unregister_fido_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


