# ImportShotgunNotesRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the note | [optional] 
**content** | **str** | Note content | [optional] 
**tasks** | [**List[ImportShotgunNotesRequestInnerTasksInner]**](ImportShotgunNotesRequestInnerTasksInner.md) | Linked tasks | [optional] 
**user** | [**ImportShotgunNotesRequestInnerUser**](ImportShotgunNotesRequestInnerUser.md) |  | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_notes_request_inner import ImportShotgunNotesRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunNotesRequestInner from a JSON string
import_shotgun_notes_request_inner_instance = ImportShotgunNotesRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunNotesRequestInner.to_json())

# convert the object into a dict
import_shotgun_notes_request_inner_dict = import_shotgun_notes_request_inner_instance.to_dict()
# create an instance of ImportShotgunNotesRequestInner from a dict
import_shotgun_notes_request_inner_from_dict = ImportShotgunNotesRequestInner.from_dict(import_shotgun_notes_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


