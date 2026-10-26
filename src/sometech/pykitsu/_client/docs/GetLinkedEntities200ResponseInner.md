# GetLinkedEntities200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Entity unique identifier | [optional] 
**name** | **str** | Entity name | [optional] 
**entity_type_id** | **UUID** | Entity type identifier | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**parent_id** | **UUID** | Parent entity identifier | [optional] 
**tasks** | [**List[GetLinkedEntities200ResponseInnerTasksInner]**](GetLinkedEntities200ResponseInnerTasksInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_linked_entities200_response_inner import GetLinkedEntities200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinkedEntities200ResponseInner from a JSON string
get_linked_entities200_response_inner_instance = GetLinkedEntities200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetLinkedEntities200ResponseInner.to_json())

# convert the object into a dict
get_linked_entities200_response_inner_dict = get_linked_entities200_response_inner_instance.to_dict()
# create an instance of GetLinkedEntities200ResponseInner from a dict
get_linked_entities200_response_inner_from_dict = GetLinkedEntities200ResponseInner.from_dict(get_linked_entities200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


