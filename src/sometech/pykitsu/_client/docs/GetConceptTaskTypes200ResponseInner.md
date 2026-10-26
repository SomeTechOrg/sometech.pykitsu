# GetConceptTaskTypes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Task type unique identifier | [optional] 
**name** | **str** | Task type name | [optional] 
**short_name** | **str** | Task type short name | [optional] 
**color** | **str** | Task type color code | [optional] 
**for_entity** | **str** | Entity type this task type is for | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_concept_task_types200_response_inner import GetConceptTaskTypes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetConceptTaskTypes200ResponseInner from a JSON string
get_concept_task_types200_response_inner_instance = GetConceptTaskTypes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetConceptTaskTypes200ResponseInner.to_json())

# convert the object into a dict
get_concept_task_types200_response_inner_dict = get_concept_task_types200_response_inner_instance.to_dict()
# create an instance of GetConceptTaskTypes200ResponseInner from a dict
get_concept_task_types200_response_inner_from_dict = GetConceptTaskTypes200ResponseInner.from_dict(get_concept_task_types200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


