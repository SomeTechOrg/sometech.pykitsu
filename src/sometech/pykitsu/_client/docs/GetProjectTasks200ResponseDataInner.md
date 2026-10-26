# GetProjectTasks200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**task_type_id** | **UUID** |  | [optional] 
**task_status_id** | **UUID** |  | [optional] 
**entity_id** | **UUID** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**assignees** | **List[UUID]** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_project_tasks200_response_data_inner import GetProjectTasks200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectTasks200ResponseDataInner from a JSON string
get_project_tasks200_response_data_inner_instance = GetProjectTasks200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectTasks200ResponseDataInner.to_json())

# convert the object into a dict
get_project_tasks200_response_data_inner_dict = get_project_tasks200_response_data_inner_instance.to_dict()
# create an instance of GetProjectTasks200ResponseDataInner from a dict
get_project_tasks200_response_data_inner_from_dict = GetProjectTasks200ResponseDataInner.from_dict(get_project_tasks200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


