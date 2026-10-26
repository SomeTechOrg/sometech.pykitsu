# RemoveShotgunProjectConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the connection to remove | 

## Example

```python
from sometech.pykitsu._client.models.remove_shotgun_project_connection_request import RemoveShotgunProjectConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveShotgunProjectConnectionRequest from a JSON string
remove_shotgun_project_connection_request_instance = RemoveShotgunProjectConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveShotgunProjectConnectionRequest.to_json())

# convert the object into a dict
remove_shotgun_project_connection_request_dict = remove_shotgun_project_connection_request_instance.to_dict()
# create an instance of RemoveShotgunProjectConnectionRequest from a dict
remove_shotgun_project_connection_request_from_dict = RemoveShotgunProjectConnectionRequest.from_dict(remove_shotgun_project_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


