# CreateChatMessagePostDataChatMessagesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **UUID** |  | 
**person_id** | **UUID** |  | 
**text** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_chat_message_post_data_chat_messages_request import CreateChatMessagePostDataChatMessagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatMessagePostDataChatMessagesRequest from a JSON string
create_chat_message_post_data_chat_messages_request_instance = CreateChatMessagePostDataChatMessagesRequest.from_json(json)
# print the JSON string representation of the object
print(CreateChatMessagePostDataChatMessagesRequest.to_json())

# convert the object into a dict
create_chat_message_post_data_chat_messages_request_dict = create_chat_message_post_data_chat_messages_request_instance.to_dict()
# create an instance of CreateChatMessagePostDataChatMessagesRequest from a dict
create_chat_message_post_data_chat_messages_request_from_dict = CreateChatMessagePostDataChatMessagesRequest.from_dict(create_chat_message_post_data_chat_messages_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


