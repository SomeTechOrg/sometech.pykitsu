# RemoveShotgunVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the version to remove | 

## Example

```python
from sometech.pykitsu._client.models.remove_shotgun_version_request import RemoveShotgunVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveShotgunVersionRequest from a JSON string
remove_shotgun_version_request_instance = RemoveShotgunVersionRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveShotgunVersionRequest.to_json())

# convert the object into a dict
remove_shotgun_version_request_dict = remove_shotgun_version_request_instance.to_dict()
# create an instance of RemoveShotgunVersionRequest from a dict
remove_shotgun_version_request_from_dict = RemoveShotgunVersionRequest.from_dict(remove_shotgun_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


