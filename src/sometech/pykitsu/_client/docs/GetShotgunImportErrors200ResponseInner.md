# GetShotgunImportErrors200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Import error unique identifier | [optional] 
**source** | **str** | Source of the import error | [optional] 
**event_data** | **object** | Error event data | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_shotgun_import_errors200_response_inner import GetShotgunImportErrors200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetShotgunImportErrors200ResponseInner from a JSON string
get_shotgun_import_errors200_response_inner_instance = GetShotgunImportErrors200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetShotgunImportErrors200ResponseInner.to_json())

# convert the object into a dict
get_shotgun_import_errors200_response_inner_dict = get_shotgun_import_errors200_response_inner_instance.to_dict()
# create an instance of GetShotgunImportErrors200ResponseInner from a dict
get_shotgun_import_errors200_response_inner_from_dict = GetShotgunImportErrors200ResponseInner.from_dict(get_shotgun_import_errors200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


