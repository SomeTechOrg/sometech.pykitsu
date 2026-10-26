# CreateEntityTasks201ResponseInner


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
from sometech.pykitsu._client.models.create_entity_tasks201_response_inner import CreateEntityTasks201ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntityTasks201ResponseInner from a JSON string
create_entity_tasks201_response_inner_instance = CreateEntityTasks201ResponseInner.from_json(json)
# print the JSON string representation of the object
print(CreateEntityTasks201ResponseInner.to_json())

# convert the object into a dict
create_entity_tasks201_response_inner_dict = create_entity_tasks201_response_inner_instance.to_dict()
# create an instance of CreateEntityTasks201ResponseInner from a dict
create_entity_tasks201_response_inner_from_dict = CreateEntityTasks201ResponseInner.from_dict(create_entity_tasks201_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


