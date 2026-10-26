# CreateShotgunImportError201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Import error unique identifier | [optional] 
**source** | **str** | Source of the import error | [optional] 
**event_data** | **object** | Error event data | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_shotgun_import_error201_response import CreateShotgunImportError201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShotgunImportError201Response from a JSON string
create_shotgun_import_error201_response_instance = CreateShotgunImportError201Response.from_json(json)
# print the JSON string representation of the object
print(CreateShotgunImportError201Response.to_json())

# convert the object into a dict
create_shotgun_import_error201_response_dict = create_shotgun_import_error201_response_instance.to_dict()
# create an instance of CreateShotgunImportError201Response from a dict
create_shotgun_import_error201_response_from_dict = CreateShotgunImportError201Response.from_dict(create_shotgun_import_error201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


