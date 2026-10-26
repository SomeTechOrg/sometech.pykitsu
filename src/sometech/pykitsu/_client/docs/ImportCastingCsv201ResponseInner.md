# ImportCastingCsv201ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**entity_in_id** | **UUID** |  | [optional] 
**entity_out_id** | **UUID** |  | [optional] 
**nb_occurences** | **int** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_casting_csv201_response_inner import ImportCastingCsv201ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCastingCsv201ResponseInner from a JSON string
import_casting_csv201_response_inner_instance = ImportCastingCsv201ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ImportCastingCsv201ResponseInner.to_json())

# convert the object into a dict
import_casting_csv201_response_inner_dict = import_casting_csv201_response_inner_instance.to_dict()
# create an instance of ImportCastingCsv201ResponseInner from a dict
import_casting_csv201_response_inner_from_dict = ImportCastingCsv201ResponseInner.from_dict(import_casting_csv201_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


