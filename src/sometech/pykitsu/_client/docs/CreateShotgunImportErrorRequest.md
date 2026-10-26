# CreateShotgunImportErrorRequest

Error event data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message | [optional] 
**details** | **object** | Additional error details | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_shotgun_import_error_request import CreateShotgunImportErrorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShotgunImportErrorRequest from a JSON string
create_shotgun_import_error_request_instance = CreateShotgunImportErrorRequest.from_json(json)
# print the JSON string representation of the object
print(CreateShotgunImportErrorRequest.to_json())

# convert the object into a dict
create_shotgun_import_error_request_dict = create_shotgun_import_error_request_instance.to_dict()
# create an instance of CreateShotgunImportErrorRequest from a dict
create_shotgun_import_error_request_from_dict = CreateShotgunImportErrorRequest.from_dict(create_shotgun_import_error_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


