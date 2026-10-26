# GetConceptsAndTasks200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Concept unique identifier | [optional] 
**name** | **str** | Concept name | [optional] 
**description** | **str** | Concept description | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**project_name** | **str** | Project name | [optional] 
**asset_type_name** | **str** | Asset type name | [optional] 
**tasks** | [**List[GetConceptsAndTasks200ResponseInnerTasksInner]**](GetConceptsAndTasks200ResponseInnerTasksInner.md) |  | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_concepts_and_tasks200_response_inner import GetConceptsAndTasks200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetConceptsAndTasks200ResponseInner from a JSON string
get_concepts_and_tasks200_response_inner_instance = GetConceptsAndTasks200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetConceptsAndTasks200ResponseInner.to_json())

# convert the object into a dict
get_concepts_and_tasks200_response_inner_dict = get_concepts_and_tasks200_response_inner_instance.to_dict()
# create an instance of GetConceptsAndTasks200ResponseInner from a dict
get_concepts_and_tasks200_response_inner_from_dict = GetConceptsAndTasks200ResponseInner.from_dict(get_concepts_and_tasks200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


