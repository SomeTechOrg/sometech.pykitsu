# GetFilterGroups200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Filter group unique identifier | [optional] 
**name** | **str** | Filter group name | [optional] 
**color** | **str** | Filter group color | [optional] 
**list_type** | **str** | List type | [optional] 
**entity_type** | **str** | Entity type | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**is_shared** | **bool** | Whether filter group is shared | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_filter_groups200_response_inner import GetFilterGroups200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetFilterGroups200ResponseInner from a JSON string
get_filter_groups200_response_inner_instance = GetFilterGroups200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetFilterGroups200ResponseInner.to_json())

# convert the object into a dict
get_filter_groups200_response_inner_dict = get_filter_groups200_response_inner_instance.to_dict()
# create an instance of GetFilterGroups200ResponseInner from a dict
get_filter_groups200_response_inner_from_dict = GetFilterGroups200ResponseInner.from_dict(get_filter_groups200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


