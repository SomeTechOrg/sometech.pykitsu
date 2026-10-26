# SetProjectFileTree200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Project unique identifier | [optional] 
**name** | **str** | Project name | [optional] 
**file_tree** | **object** | File tree template configuration | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.set_project_file_tree200_response import SetProjectFileTree200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetProjectFileTree200Response from a JSON string
set_project_file_tree200_response_instance = SetProjectFileTree200Response.from_json(json)
# print the JSON string representation of the object
print(SetProjectFileTree200Response.to_json())

# convert the object into a dict
set_project_file_tree200_response_dict = set_project_file_tree200_response_instance.to_dict()
# create an instance of SetProjectFileTree200Response from a dict
set_project_file_tree200_response_from_dict = SetProjectFileTree200Response.from_dict(set_project_file_tree200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


