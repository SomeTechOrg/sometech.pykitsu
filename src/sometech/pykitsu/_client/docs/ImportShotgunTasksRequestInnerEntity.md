# ImportShotgunTasksRequestInnerEntity

Entity information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_tasks_request_inner_entity import ImportShotgunTasksRequestInnerEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunTasksRequestInnerEntity from a JSON string
import_shotgun_tasks_request_inner_entity_instance = ImportShotgunTasksRequestInnerEntity.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunTasksRequestInnerEntity.to_json())

# convert the object into a dict
import_shotgun_tasks_request_inner_entity_dict = import_shotgun_tasks_request_inner_entity_instance.to_dict()
# create an instance of ImportShotgunTasksRequestInnerEntity from a dict
import_shotgun_tasks_request_inner_entity_from_dict = ImportShotgunTasksRequestInnerEntity.from_dict(import_shotgun_tasks_request_inner_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


