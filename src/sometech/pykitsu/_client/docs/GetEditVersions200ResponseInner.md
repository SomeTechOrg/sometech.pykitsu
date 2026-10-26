# GetEditVersions200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Version unique identifier | [optional] 
**edit_id** | **UUID** | Edit identifier | [optional] 
**version_number** | **int** | Version number | [optional] 
**data** | **object** | Version data content | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**created_by** | **UUID** | Creator person identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_edit_versions200_response_inner import GetEditVersions200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEditVersions200ResponseInner from a JSON string
get_edit_versions200_response_inner_instance = GetEditVersions200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetEditVersions200ResponseInner.to_json())

# convert the object into a dict
get_edit_versions200_response_inner_dict = get_edit_versions200_response_inner_instance.to_dict()
# create an instance of GetEditVersions200ResponseInner from a dict
get_edit_versions200_response_inner_from_dict = GetEditVersions200ResponseInner.from_dict(get_edit_versions200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


