# UpdateEntityLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nb_occurences** | **int** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_entity_link_request import UpdateEntityLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEntityLinkRequest from a JSON string
update_entity_link_request_instance = UpdateEntityLinkRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEntityLinkRequest.to_json())

# convert the object into a dict
update_entity_link_request_dict = update_entity_link_request_instance.to_dict()
# create an instance of UpdateEntityLinkRequest from a dict
update_entity_link_request_from_dict = UpdateEntityLinkRequest.from_dict(update_entity_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


