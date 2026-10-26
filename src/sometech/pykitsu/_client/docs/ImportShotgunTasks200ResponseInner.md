# ImportShotgunTasks200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Task unique identifier | [optional] 
**name** | **str** | Task name | [optional] 
**start_date** | **date** | Start date | [optional] 
**due_date** | **date** | Due date | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_tasks200_response_inner import ImportShotgunTasks200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunTasks200ResponseInner from a JSON string
import_shotgun_tasks200_response_inner_instance = ImportShotgunTasks200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunTasks200ResponseInner.to_json())

# convert the object into a dict
import_shotgun_tasks200_response_inner_dict = import_shotgun_tasks200_response_inner_instance.to_dict()
# create an instance of ImportShotgunTasks200ResponseInner from a dict
import_shotgun_tasks200_response_inner_from_dict = ImportShotgunTasks200ResponseInner.from_dict(import_shotgun_tasks200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


