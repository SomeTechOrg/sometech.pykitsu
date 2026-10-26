# GetLinkedAssets200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Linked asset unique identifier | [optional] 
**name** | **str** | Linked asset name | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**entity_type_id** | **UUID** | Asset type identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_linked_assets200_response_inner import GetLinkedAssets200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinkedAssets200ResponseInner from a JSON string
get_linked_assets200_response_inner_instance = GetLinkedAssets200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetLinkedAssets200ResponseInner.to_json())

# convert the object into a dict
get_linked_assets200_response_inner_dict = get_linked_assets200_response_inner_instance.to_dict()
# create an instance of GetLinkedAssets200ResponseInner from a dict
get_linked_assets200_response_inner_from_dict = GetLinkedAssets200ResponseInner.from_dict(get_linked_assets200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


