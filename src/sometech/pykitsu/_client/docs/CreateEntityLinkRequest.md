# CreateEntityLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_in_id** | **UUID** |  | 
**entity_out_id** | **UUID** |  | 
**nb_occurences** | **int** |  | [optional] [default to 1]
**label** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_entity_link_request import CreateEntityLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntityLinkRequest from a JSON string
create_entity_link_request_instance = CreateEntityLinkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEntityLinkRequest.to_json())

# convert the object into a dict
create_entity_link_request_dict = create_entity_link_request_instance.to_dict()
# create an instance of CreateEntityLinkRequest from a dict
create_entity_link_request_from_dict = CreateEntityLinkRequest.from_dict(create_entity_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


