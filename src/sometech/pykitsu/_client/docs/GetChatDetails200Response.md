# GetChatDetails200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Chat unique identifier | [optional] 
**entity_id** | **UUID** | Entity ID this chat is associated with | [optional] 
**participants** | **List[UUID]** | List of participant user IDs | [optional] 
**messages** | **List[object]** | Array of chat messages | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_chat_details200_response import GetChatDetails200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatDetails200Response from a JSON string
get_chat_details200_response_instance = GetChatDetails200Response.from_json(json)
# print the JSON string representation of the object
print(GetChatDetails200Response.to_json())

# convert the object into a dict
get_chat_details200_response_dict = get_chat_details200_response_instance.to_dict()
# create an instance of GetChatDetails200Response from a dict
get_chat_details200_response_from_dict = GetChatDetails200Response.from_dict(get_chat_details200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


