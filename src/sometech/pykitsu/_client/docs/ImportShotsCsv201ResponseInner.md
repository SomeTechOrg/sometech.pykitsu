# ImportShotsCsv201ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**parent_id** | **UUID** |  | [optional] 
**nb_frames** | **int** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shots_csv201_response_inner import ImportShotsCsv201ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotsCsv201ResponseInner from a JSON string
import_shots_csv201_response_inner_instance = ImportShotsCsv201ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotsCsv201ResponseInner.to_json())

# convert the object into a dict
import_shots_csv201_response_inner_dict = import_shots_csv201_response_inner_instance.to_dict()
# create an instance of ImportShotsCsv201ResponseInner from a dict
import_shots_csv201_response_inner_from_dict = ImportShotsCsv201ResponseInner.from_dict(import_shots_csv201_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


