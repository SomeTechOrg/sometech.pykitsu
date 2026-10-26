# GetNotificationsGetDataUserNotifications200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Notification unique identifier | [optional] 
**type** | **str** | Notification type | [optional] 
**read** | **bool** | Whether notification is read | [optional] 
**author_id** | **UUID** | Author person identifier | [optional] 
**comment_id** | **UUID** | Comment identifier | [optional] 
**task_id** | **UUID** | Task identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_notifications_get_data_user_notifications200_response_inner import GetNotificationsGetDataUserNotifications200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotificationsGetDataUserNotifications200ResponseInner from a JSON string
get_notifications_get_data_user_notifications200_response_inner_instance = GetNotificationsGetDataUserNotifications200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetNotificationsGetDataUserNotifications200ResponseInner.to_json())

# convert the object into a dict
get_notifications_get_data_user_notifications200_response_inner_dict = get_notifications_get_data_user_notifications200_response_inner_instance.to_dict()
# create an instance of GetNotificationsGetDataUserNotifications200ResponseInner from a dict
get_notifications_get_data_user_notifications200_response_inner_from_dict = GetNotificationsGetDataUserNotifications200ResponseInner.from_dict(get_notifications_get_data_user_notifications200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


