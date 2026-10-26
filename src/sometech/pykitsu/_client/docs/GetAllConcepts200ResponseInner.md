# GetAllConcepts200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Concept unique identifier | [optional] 
**name** | **str** | Concept name | [optional] 
**description** | **str** | Concept description | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**parent_id** | **UUID** | Parent concept identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_all_concepts200_response_inner import GetAllConcepts200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllConcepts200ResponseInner from a JSON string
get_all_concepts200_response_inner_instance = GetAllConcepts200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetAllConcepts200ResponseInner.to_json())

# convert the object into a dict
get_all_concepts200_response_inner_dict = get_all_concepts200_response_inner_instance.to_dict()
# create an instance of GetAllConcepts200ResponseInner from a dict
get_all_concepts200_response_inner_from_dict = GetAllConcepts200ResponseInner.from_dict(get_all_concepts200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


