# ImportPersonsCsv201ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_persons_csv201_response_inner import ImportPersonsCsv201ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportPersonsCsv201ResponseInner from a JSON string
import_persons_csv201_response_inner_instance = ImportPersonsCsv201ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ImportPersonsCsv201ResponseInner.to_json())

# convert the object into a dict
import_persons_csv201_response_inner_dict = import_persons_csv201_response_inner_instance.to_dict()
# create an instance of ImportPersonsCsv201ResponseInner from a dict
import_persons_csv201_response_inner_from_dict = ImportPersonsCsv201ResponseInner.from_dict(import_persons_csv201_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


