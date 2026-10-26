# GetChatsGetDataUserChats200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Chat unique identifier | [optional] 
**entity_id** | **UUID** | Entity identifier | [optional] 
**entity_type** | **str** | Entity type | [optional] 
**participants** | **List[UUID]** | List of participant person identifiers | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_chats_get_data_user_chats200_response_inner import GetChatsGetDataUserChats200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetChatsGetDataUserChats200ResponseInner from a JSON string
get_chats_get_data_user_chats200_response_inner_instance = GetChatsGetDataUserChats200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetChatsGetDataUserChats200ResponseInner.to_json())

# convert the object into a dict
get_chats_get_data_user_chats200_response_inner_dict = get_chats_get_data_user_chats200_response_inner_instance.to_dict()
# create an instance of GetChatsGetDataUserChats200ResponseInner from a dict
get_chats_get_data_user_chats200_response_inner_from_dict = GetChatsGetDataUserChats200ResponseInner.from_dict(get_chats_get_data_user_chats200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


