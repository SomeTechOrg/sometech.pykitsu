# UpdateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**production_style** | **str** |  | [optional] 
**preview_background_file_id** | **UUID** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_project_request import UpdateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectRequest from a JSON string
update_project_request_instance = UpdateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProjectRequest.to_json())

# convert the object into a dict
update_project_request_dict = update_project_request_instance.to_dict()
# create an instance of UpdateProjectRequest from a dict
update_project_request_from_dict = UpdateProjectRequest.from_dict(update_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


