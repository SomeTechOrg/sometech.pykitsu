# CreateProjectTaskStatusLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** |  | 
**task_status_id** | **UUID** |  | 
**priority** | **int** | Priority of the task status in the project | [optional] [default to 1]
**roles_for_board** | **List[str]** | Roles allowed to see this status on the board | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_project_task_status_link_request import CreateProjectTaskStatusLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectTaskStatusLinkRequest from a JSON string
create_project_task_status_link_request_instance = CreateProjectTaskStatusLinkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectTaskStatusLinkRequest.to_json())

# convert the object into a dict
create_project_task_status_link_request_dict = create_project_task_status_link_request_instance.to_dict()
# create an instance of CreateProjectTaskStatusLinkRequest from a dict
create_project_task_status_link_request_from_dict = CreateProjectTaskStatusLinkRequest.from_dict(create_project_task_status_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


