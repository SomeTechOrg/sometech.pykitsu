# DataImportError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_data** | **str** | JSON field to add event data | [optional] 
**source** | **List[str]** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.data_import_error import DataImportError

# TODO update the JSON string below
json = "{}"
# create an instance of DataImportError from a JSON string
data_import_error_instance = DataImportError.from_json(json)
# print the JSON string representation of the object
print(DataImportError.to_json())

# convert the object into a dict
data_import_error_dict = data_import_error_instance.to_dict()
# create an instance of DataImportError from a dict
data_import_error_from_dict = DataImportError.from_dict(data_import_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


