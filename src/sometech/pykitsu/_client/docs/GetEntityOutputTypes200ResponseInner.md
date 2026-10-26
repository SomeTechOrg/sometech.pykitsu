# GetEntityOutputTypes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Output type unique identifier | [optional] 
**name** | **str** | Output type name | [optional] 
**short_name** | **str** | Output type short name | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_entity_output_types200_response_inner import GetEntityOutputTypes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityOutputTypes200ResponseInner from a JSON string
get_entity_output_types200_response_inner_instance = GetEntityOutputTypes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetEntityOutputTypes200ResponseInner.to_json())

# convert the object into a dict
get_entity_output_types200_response_inner_dict = get_entity_output_types200_response_inner_instance.to_dict()
# create an instance of GetEntityOutputTypes200ResponseInner from a dict
get_entity_output_types200_response_inner_from_dict = GetEntityOutputTypes200ResponseInner.from_dict(get_entity_output_types200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


