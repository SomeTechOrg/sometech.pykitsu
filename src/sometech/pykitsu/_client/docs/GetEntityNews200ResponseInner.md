# GetEntityNews200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | News unique identifier | [optional] 
**change** | **bool** | Whether this news represents a change | [optional] 
**author_id** | **UUID** | Author person identifier | [optional] 
**comment_id** | **UUID** | Comment identifier | [optional] 
**task_id** | **UUID** | Task identifier | [optional] 
**preview_file_id** | **UUID** | Preview file identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_entity_news200_response_inner import GetEntityNews200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityNews200ResponseInner from a JSON string
get_entity_news200_response_inner_instance = GetEntityNews200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetEntityNews200ResponseInner.to_json())

# convert the object into a dict
get_entity_news200_response_inner_dict = get_entity_news200_response_inner_instance.to_dict()
# create an instance of GetEntityNews200ResponseInner from a dict
get_entity_news200_response_inner_from_dict = GetEntityNews200ResponseInner.from_dict(get_entity_news200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


