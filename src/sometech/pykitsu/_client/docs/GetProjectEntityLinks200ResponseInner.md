# GetProjectEntityLinks200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Entity link unique identifier | [optional] 
**entity_in_id** | **UUID** | Source entity identifier | [optional] 
**entity_out_id** | **UUID** | Target entity identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_project_entity_links200_response_inner import GetProjectEntityLinks200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectEntityLinks200ResponseInner from a JSON string
get_project_entity_links200_response_inner_instance = GetProjectEntityLinks200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectEntityLinks200ResponseInner.to_json())

# convert the object into a dict
get_project_entity_links200_response_inner_dict = get_project_entity_links200_response_inner_instance.to_dict()
# create an instance of GetProjectEntityLinks200ResponseInner from a dict
get_project_entity_links200_response_inner_from_dict = GetProjectEntityLinks200ResponseInner.from_dict(get_project_entity_links200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


