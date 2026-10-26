# GetEntity200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**entity_type_id** | **UUID** |  | [optional] 
**status** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_entity200_response import GetEntity200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntity200Response from a JSON string
get_entity200_response_instance = GetEntity200Response.from_json(json)
# print the JSON string representation of the object
print(GetEntity200Response.to_json())

# convert the object into a dict
get_entity200_response_dict = get_entity200_response_instance.to_dict()
# create an instance of GetEntity200Response from a dict
get_entity200_response_from_dict = GetEntity200Response.from_dict(get_entity200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


