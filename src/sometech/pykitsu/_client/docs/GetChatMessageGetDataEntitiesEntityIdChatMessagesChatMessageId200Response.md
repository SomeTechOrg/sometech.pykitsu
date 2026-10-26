# GetChatMessageGetDataEntitiesEntityIdChatMessagesChatMessageId200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Message unique identifier | [optional] 
**message** | **str** | Message content | [optional] 
**person_id** | **UUID** | ID of the message sender | [optional] 
**created_at** | **datetime** | Message creation timestamp | [optional] 
**updated_at** | **datetime** | Message last update timestamp | [optional] 
**attachments** | **List[object]** | Array of file attachments | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_chat_message_get_data_entities_entity_id_chat_messages_chat_message_id200_response import GetChatMessageGetDataEntitiesEntityIdChatMessagesChatMessageId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatMessageGetDataEntitiesEntityIdChatMessagesChatMessageId200Response from a JSON string
get_chat_message_get_data_entities_entity_id_chat_messages_chat_message_id200_response_instance = GetChatMessageGetDataEntitiesEntityIdChatMessagesChatMessageId200Response.from_json(json)
# print the JSON string representation of the object
print(GetChatMessageGetDataEntitiesEntityIdChatMessagesChatMessageId200Response.to_json())

# convert the object into a dict
get_chat_message_get_data_entities_entity_id_chat_messages_chat_message_id200_response_dict = get_chat_message_get_data_entities_entity_id_chat_messages_chat_message_id200_response_instance.to_dict()
# create an instance of GetChatMessageGetDataEntitiesEntityIdChatMessagesChatMessageId200Response from a dict
get_chat_message_get_data_entities_entity_id_chat_messages_chat_message_id200_response_from_dict = GetChatMessageGetDataEntitiesEntityIdChatMessagesChatMessageId200Response.from_dict(get_chat_message_get_data_entities_entity_id_chat_messages_chat_message_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


