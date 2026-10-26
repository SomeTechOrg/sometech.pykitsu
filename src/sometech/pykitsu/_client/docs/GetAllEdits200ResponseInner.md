# GetAllEdits200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Edit unique identifier | [optional] 
**name** | **str** | Edit name | [optional] 
**description** | **str** | Edit description | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**episode_id** | **UUID** | Episode identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_all_edits200_response_inner import GetAllEdits200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllEdits200ResponseInner from a JSON string
get_all_edits200_response_inner_instance = GetAllEdits200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetAllEdits200ResponseInner.to_json())

# convert the object into a dict
get_all_edits200_response_inner_dict = get_all_edits200_response_inner_instance.to_dict()
# create an instance of GetAllEdits200ResponseInner from a dict
get_all_edits200_response_inner_from_dict = GetAllEdits200ResponseInner.from_dict(get_all_edits200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


