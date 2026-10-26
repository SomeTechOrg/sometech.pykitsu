# ProjectStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.project_status import ProjectStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStatus from a JSON string
project_status_instance = ProjectStatus.from_json(json)
# print the JSON string representation of the object
print(ProjectStatus.to_json())

# convert the object into a dict
project_status_dict = project_status_instance.to_dict()
# create an instance of ProjectStatus from a dict
project_status_from_dict = ProjectStatus.from_dict(project_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


