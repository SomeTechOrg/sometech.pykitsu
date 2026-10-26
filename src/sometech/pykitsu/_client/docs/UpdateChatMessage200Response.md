# UpdateChatMessage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**chat_id** | **UUID** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**text** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_chat_message200_response import UpdateChatMessage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChatMessage200Response from a JSON string
update_chat_message200_response_instance = UpdateChatMessage200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateChatMessage200Response.to_json())

# convert the object into a dict
update_chat_message200_response_dict = update_chat_message200_response_instance.to_dict()
# create an instance of UpdateChatMessage200Response from a dict
update_chat_message200_response_from_dict = UpdateChatMessage200Response.from_dict(update_chat_message200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


