# CreateChatMessagePostDataChatMessages201Response


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
from sometech.pykitsu._client.models.create_chat_message_post_data_chat_messages201_response import CreateChatMessagePostDataChatMessages201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatMessagePostDataChatMessages201Response from a JSON string
create_chat_message_post_data_chat_messages201_response_instance = CreateChatMessagePostDataChatMessages201Response.from_json(json)
# print the JSON string representation of the object
print(CreateChatMessagePostDataChatMessages201Response.to_json())

# convert the object into a dict
create_chat_message_post_data_chat_messages201_response_dict = create_chat_message_post_data_chat_messages201_response_instance.to_dict()
# create an instance of CreateChatMessagePostDataChatMessages201Response from a dict
create_chat_message_post_data_chat_messages201_response_from_dict = CreateChatMessagePostDataChatMessages201Response.from_dict(create_chat_message_post_data_chat_messages201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


