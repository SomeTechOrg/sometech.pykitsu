# GetNotificationGetDataUserNotificationsNotificationId200Response


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
from sometech.pykitsu._client.models.get_notification_get_data_user_notifications_notification_id200_response import GetNotificationGetDataUserNotificationsNotificationId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotificationGetDataUserNotificationsNotificationId200Response from a JSON string
get_notification_get_data_user_notifications_notification_id200_response_instance = GetNotificationGetDataUserNotificationsNotificationId200Response.from_json(json)
# print the JSON string representation of the object
print(GetNotificationGetDataUserNotificationsNotificationId200Response.to_json())

# convert the object into a dict
get_notification_get_data_user_notifications_notification_id200_response_dict = get_notification_get_data_user_notifications_notification_id200_response_instance.to_dict()
# create an instance of GetNotificationGetDataUserNotificationsNotificationId200Response from a dict
get_notification_get_data_user_notifications_notification_id200_response_from_dict = GetNotificationGetDataUserNotificationsNotificationId200Response.from_dict(get_notification_get_data_user_notifications_notification_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


