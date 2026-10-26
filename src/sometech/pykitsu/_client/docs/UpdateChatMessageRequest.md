# UpdateChatMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_chat_message_request import UpdateChatMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateChatMessageRequest from a JSON string
update_chat_message_request_instance = UpdateChatMessageRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateChatMessageRequest.to_json())

# convert the object into a dict
update_chat_message_request_dict = update_chat_message_request_instance.to_dict()
# create an instance of UpdateChatMessageRequest from a dict
update_chat_message_request_from_dict = UpdateChatMessageRequest.from_dict(update_chat_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


