# GetConceptPreviews200ResponseValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Preview unique identifier | [optional] 
**name** | **str** | Preview name | [optional] 
**original_name** | **str** | Original file name | [optional] 
**file_path** | **str** | File path | [optional] 
**task_type_id** | **UUID** | Task type identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_concept_previews200_response_value_inner import GetConceptPreviews200ResponseValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetConceptPreviews200ResponseValueInner from a JSON string
get_concept_previews200_response_value_inner_instance = GetConceptPreviews200ResponseValueInner.from_json(json)
# print the JSON string representation of the object
print(GetConceptPreviews200ResponseValueInner.to_json())

# convert the object into a dict
get_concept_previews200_response_value_inner_dict = get_concept_previews200_response_value_inner_instance.to_dict()
# create an instance of GetConceptPreviews200ResponseValueInner from a dict
get_concept_previews200_response_value_inner_from_dict = GetConceptPreviews200ResponseValueInner.from_dict(get_concept_previews200_response_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


