# Metadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** | ID of project for which metadata are added | [optional] 
**entity_type** | **str** | Asset or Shot | [optional] 
**name** | **str** | Field name for GUI | [optional] 
**field_name** | **str** | Technical field name | [optional] 
**choices** | **str** | Array of string that represents the available values for this metadata (this metadata is considered as a free field if this array is empty) | [optional] 
**for_client** | **bool** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.metadata import Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of Metadata from a JSON string
metadata_instance = Metadata.from_json(json)
# print the JSON string representation of the object
print(Metadata.to_json())

# convert the object into a dict
metadata_dict = metadata_instance.to_dict()
# create an instance of Metadata from a dict
metadata_from_dict = Metadata.from_dict(metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


