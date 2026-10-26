# CreateFileStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**color** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_file_status_request import CreateFileStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFileStatusRequest from a JSON string
create_file_status_request_instance = CreateFileStatusRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFileStatusRequest.to_json())

# convert the object into a dict
create_file_status_request_dict = create_file_status_request_instance.to_dict()
# create an instance of CreateFileStatusRequest from a dict
create_file_status_request_from_dict = CreateFileStatusRequest.from_dict(create_file_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


