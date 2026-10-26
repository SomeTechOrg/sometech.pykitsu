# CreateProjectTaskTypeLink201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**task_type_id** | **UUID** |  | [optional] 
**priority** | **int** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_project_task_type_link201_response import CreateProjectTaskTypeLink201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectTaskTypeLink201Response from a JSON string
create_project_task_type_link201_response_instance = CreateProjectTaskTypeLink201Response.from_json(json)
# print the JSON string representation of the object
print(CreateProjectTaskTypeLink201Response.to_json())

# convert the object into a dict
create_project_task_type_link201_response_dict = create_project_task_type_link201_response_instance.to_dict()
# create an instance of CreateProjectTaskTypeLink201Response from a dict
create_project_task_type_link201_response_from_dict = CreateProjectTaskTypeLink201Response.from_dict(create_project_task_type_link201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


