# CreateProjectTaskTypeLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** |  | 
**task_type_id** | **UUID** |  | 
**priority** | **int** | Priority of the task type in the project | [optional] [default to 1]

## Example

```python
from sometech.pykitsu._client.models.create_project_task_type_link_request import CreateProjectTaskTypeLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectTaskTypeLinkRequest from a JSON string
create_project_task_type_link_request_instance = CreateProjectTaskTypeLinkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectTaskTypeLinkRequest.to_json())

# convert the object into a dict
create_project_task_type_link_request_dict = create_project_task_type_link_request_instance.to_dict()
# create an instance of CreateProjectTaskTypeLinkRequest from a dict
create_project_task_type_link_request_from_dict = CreateProjectTaskTypeLinkRequest.from_dict(create_project_task_type_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


