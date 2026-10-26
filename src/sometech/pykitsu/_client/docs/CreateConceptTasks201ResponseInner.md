# CreateConceptTasks201ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**task_type_id** | **UUID** |  | [optional] 
**task_status_id** | **UUID** |  | [optional] 
**entity_id** | **UUID** |  | [optional] 
**project_id** | **UUID** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_concept_tasks201_response_inner import CreateConceptTasks201ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConceptTasks201ResponseInner from a JSON string
create_concept_tasks201_response_inner_instance = CreateConceptTasks201ResponseInner.from_json(json)
# print the JSON string representation of the object
print(CreateConceptTasks201ResponseInner.to_json())

# convert the object into a dict
create_concept_tasks201_response_inner_dict = create_concept_tasks201_response_inner_instance.to_dict()
# create an instance of CreateConceptTasks201ResponseInner from a dict
create_concept_tasks201_response_inner_from_dict = CreateConceptTasks201ResponseInner.from_dict(create_concept_tasks201_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


