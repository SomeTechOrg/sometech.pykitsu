# CreateProjectTaskStatusLink201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**task_status_id** | **UUID** |  | [optional] 
**priority** | **int** |  | [optional] 
**roles_for_board** | **List[str]** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_project_task_status_link201_response import CreateProjectTaskStatusLink201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectTaskStatusLink201Response from a JSON string
create_project_task_status_link201_response_instance = CreateProjectTaskStatusLink201Response.from_json(json)
# print the JSON string representation of the object
print(CreateProjectTaskStatusLink201Response.to_json())

# convert the object into a dict
create_project_task_status_link201_response_dict = create_project_task_status_link201_response_instance.to_dict()
# create an instance of CreateProjectTaskStatusLink201Response from a dict
create_project_task_status_link201_response_from_dict = CreateProjectTaskStatusLink201Response.from_dict(create_project_task_status_link201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


