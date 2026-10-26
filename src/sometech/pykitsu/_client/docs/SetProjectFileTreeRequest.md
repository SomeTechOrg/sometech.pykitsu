# SetProjectFileTreeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tree_name** | **str** | Name of the file tree template | 

## Example

```python
from sometech.pykitsu._client.models.set_project_file_tree_request import SetProjectFileTreeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetProjectFileTreeRequest from a JSON string
set_project_file_tree_request_instance = SetProjectFileTreeRequest.from_json(json)
# print the JSON string representation of the object
print(SetProjectFileTreeRequest.to_json())

# convert the object into a dict
set_project_file_tree_request_dict = set_project_file_tree_request_instance.to_dict()
# create an instance of SetProjectFileTreeRequest from a dict
set_project_file_tree_request_from_dict = SetProjectFileTreeRequest.from_dict(set_project_file_tree_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


