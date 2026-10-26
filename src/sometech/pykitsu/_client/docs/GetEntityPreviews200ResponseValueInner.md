# GetEntityPreviews200ResponseValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Preview file unique identifier | [optional] 
**name** | **str** | Preview file name | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_entity_previews200_response_value_inner import GetEntityPreviews200ResponseValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityPreviews200ResponseValueInner from a JSON string
get_entity_previews200_response_value_inner_instance = GetEntityPreviews200ResponseValueInner.from_json(json)
# print the JSON string representation of the object
print(GetEntityPreviews200ResponseValueInner.to_json())

# convert the object into a dict
get_entity_previews200_response_value_inner_dict = get_entity_previews200_response_value_inner_instance.to_dict()
# create an instance of GetEntityPreviews200ResponseValueInner from a dict
get_entity_previews200_response_value_inner_from_dict = GetEntityPreviews200ResponseValueInner.from_dict(get_entity_previews200_response_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


