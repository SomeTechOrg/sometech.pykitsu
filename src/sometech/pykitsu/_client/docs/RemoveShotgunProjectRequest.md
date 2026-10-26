# RemoveShotgunProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the project to remove | 

## Example

```python
from sometech.pykitsu._client.models.remove_shotgun_project_request import RemoveShotgunProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveShotgunProjectRequest from a JSON string
remove_shotgun_project_request_instance = RemoveShotgunProjectRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveShotgunProjectRequest.to_json())

# convert the object into a dict
remove_shotgun_project_request_dict = remove_shotgun_project_request_instance.to_dict()
# create an instance of RemoveShotgunProjectRequest from a dict
remove_shotgun_project_request_from_dict = RemoveShotgunProjectRequest.from_dict(remove_shotgun_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


