# ImportKitsuTasksRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Kitsu ID of the task | [optional] 
**name** | **str** | Task name | [optional] 
**project_id** | **UUID** | Project ID | [optional] 
**entity_id** | **UUID** | Entity ID the task is linked to | [optional] 
**task_type_id** | **UUID** | Task type ID | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_kitsu_tasks_request_inner import ImportKitsuTasksRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportKitsuTasksRequestInner from a JSON string
import_kitsu_tasks_request_inner_instance = ImportKitsuTasksRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportKitsuTasksRequestInner.to_json())

# convert the object into a dict
import_kitsu_tasks_request_inner_dict = import_kitsu_tasks_request_inner_instance.to_dict()
# create an instance of ImportKitsuTasksRequestInner from a dict
import_kitsu_tasks_request_inner_from_dict = ImportKitsuTasksRequestInner.from_dict(import_kitsu_tasks_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


