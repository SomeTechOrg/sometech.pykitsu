# UpdateNotificationPutDataUserNotificationsNotificationId200Response


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
from sometech.pykitsu._client.models.update_notification_put_data_user_notifications_notification_id200_response import UpdateNotificationPutDataUserNotificationsNotificationId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNotificationPutDataUserNotificationsNotificationId200Response from a JSON string
update_notification_put_data_user_notifications_notification_id200_response_instance = UpdateNotificationPutDataUserNotificationsNotificationId200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateNotificationPutDataUserNotificationsNotificationId200Response.to_json())

# convert the object into a dict
update_notification_put_data_user_notifications_notification_id200_response_dict = update_notification_put_data_user_notifications_notification_id200_response_instance.to_dict()
# create an instance of UpdateNotificationPutDataUserNotificationsNotificationId200Response from a dict
update_notification_put_data_user_notifications_notification_id200_response_from_dict = UpdateNotificationPutDataUserNotificationsNotificationId200Response.from_dict(update_notification_put_data_user_notifications_notification_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


