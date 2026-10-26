# GetChatMessagesGetDataEntitiesEntityIdChatMessages200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Message unique identifier | [optional] 
**message** | **str** | Message content | [optional] 
**person_id** | **UUID** | ID of the message sender | [optional] 
**created_at** | **datetime** | Message creation timestamp | [optional] 
**attachments** | **List[object]** | Array of file attachments | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_chat_messages_get_data_entities_entity_id_chat_messages200_response_inner import GetChatMessagesGetDataEntitiesEntityIdChatMessages200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatMessagesGetDataEntitiesEntityIdChatMessages200ResponseInner from a JSON string
get_chat_messages_get_data_entities_entity_id_chat_messages200_response_inner_instance = GetChatMessagesGetDataEntitiesEntityIdChatMessages200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetChatMessagesGetDataEntitiesEntityIdChatMessages200ResponseInner.to_json())

# convert the object into a dict
get_chat_messages_get_data_entities_entity_id_chat_messages200_response_inner_dict = get_chat_messages_get_data_entities_entity_id_chat_messages200_response_inner_instance.to_dict()
# create an instance of GetChatMessagesGetDataEntitiesEntityIdChatMessages200ResponseInner from a dict
get_chat_messages_get_data_entities_entity_id_chat_messages200_response_inner_from_dict = GetChatMessagesGetDataEntitiesEntityIdChatMessages200ResponseInner.from_dict(get_chat_messages_get_data_entities_entity_id_chat_messages200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


