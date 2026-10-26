# CreateEntityLink201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**entity_in_id** | **UUID** |  | [optional] 
**entity_out_id** | **UUID** |  | [optional] 
**nb_occurences** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_entity_link201_response import CreateEntityLink201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntityLink201Response from a JSON string
create_entity_link201_response_instance = CreateEntityLink201Response.from_json(json)
# print the JSON string representation of the object
print(CreateEntityLink201Response.to_json())

# convert the object into a dict
create_entity_link201_response_dict = create_entity_link201_response_instance.to_dict()
# create an instance of CreateEntityLink201Response from a dict
create_entity_link201_response_from_dict = CreateEntityLink201Response.from_dict(create_entity_link201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


