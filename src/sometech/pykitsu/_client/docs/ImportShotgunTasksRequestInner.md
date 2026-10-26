# ImportShotgunTasksRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the task | [optional] 
**cached_display_name** | **str** | Task display name | [optional] 
**start_date** | **date** | Start date | [optional] 
**due_date** | **date** | Due date | [optional] 
**sg_sort_order** | **int** | Sort order | [optional] 
**duration** | **int** | Duration in days | [optional] 
**step** | [**ImportShotgunTasksRequestInnerStep**](ImportShotgunTasksRequestInnerStep.md) |  | [optional] 
**project** | [**ImportShotgunTasksRequestInnerProject**](ImportShotgunTasksRequestInnerProject.md) |  | [optional] 
**entity** | [**ImportShotgunTasksRequestInnerEntity**](ImportShotgunTasksRequestInnerEntity.md) |  | [optional] 
**sg_status_list** | **str** | Status short name | [optional] 
**created_by** | [**ImportShotgunTasksRequestInnerCreatedBy**](ImportShotgunTasksRequestInnerCreatedBy.md) |  | [optional] 
**task_assignees** | [**List[ImportShotgunTasksRequestInnerTaskAssigneesInner]**](ImportShotgunTasksRequestInnerTaskAssigneesInner.md) | Task assignees | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_tasks_request_inner import ImportShotgunTasksRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunTasksRequestInner from a JSON string
import_shotgun_tasks_request_inner_instance = ImportShotgunTasksRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunTasksRequestInner.to_json())

# convert the object into a dict
import_shotgun_tasks_request_inner_dict = import_shotgun_tasks_request_inner_instance.to_dict()
# create an instance of ImportShotgunTasksRequestInner from a dict
import_shotgun_tasks_request_inner_from_dict = ImportShotgunTasksRequestInner.from_dict(import_shotgun_tasks_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


