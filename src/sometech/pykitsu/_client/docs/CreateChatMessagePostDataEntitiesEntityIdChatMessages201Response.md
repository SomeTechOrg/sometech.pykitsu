# CreateChatMessagePostDataEntitiesEntityIdChatMessages201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Created message unique identifier | [optional] 
**message** | **str** | Message content | [optional] 
**person_id** | **UUID** | ID of the message sender | [optional] 
**created_at** | **datetime** | Message creation timestamp | [optional] 
**attachments** | **List[object]** | Array of attached files | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_chat_message_post_data_entities_entity_id_chat_messages201_response import CreateChatMessagePostDataEntitiesEntityIdChatMessages201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatMessagePostDataEntitiesEntityIdChatMessages201Response from a JSON string
create_chat_message_post_data_entities_entity_id_chat_messages201_response_instance = CreateChatMessagePostDataEntitiesEntityIdChatMessages201Response.from_json(json)
# print the JSON string representation of the object
print(CreateChatMessagePostDataEntitiesEntityIdChatMessages201Response.to_json())

# convert the object into a dict
create_chat_message_post_data_entities_entity_id_chat_messages201_response_dict = create_chat_message_post_data_entities_entity_id_chat_messages201_response_instance.to_dict()
# create an instance of CreateChatMessagePostDataEntitiesEntityIdChatMessages201Response from a dict
create_chat_message_post_data_entities_entity_id_chat_messages201_response_from_dict = CreateChatMessagePostDataEntitiesEntityIdChatMessages201Response.from_dict(create_chat_message_post_data_entities_entity_id_chat_messages201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


