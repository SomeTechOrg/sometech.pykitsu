# UpdateEntityType200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_entity_type200_response import UpdateEntityType200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEntityType200Response from a JSON string
update_entity_type200_response_instance = UpdateEntityType200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateEntityType200Response.to_json())

# convert the object into a dict
update_entity_type200_response_dict = update_entity_type200_response_instance.to_dict()
# create an instance of UpdateEntityType200Response from a dict
update_entity_type200_response_from_dict = UpdateEntityType200Response.from_dict(update_entity_type200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


