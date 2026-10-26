# UpdateNotificationPutDataNotificationsInstanceId200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**comment_id** | **UUID** |  | [optional] 
**read** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_notification_put_data_notifications_instance_id200_response import UpdateNotificationPutDataNotificationsInstanceId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNotificationPutDataNotificationsInstanceId200Response from a JSON string
update_notification_put_data_notifications_instance_id200_response_instance = UpdateNotificationPutDataNotificationsInstanceId200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateNotificationPutDataNotificationsInstanceId200Response.to_json())

# convert the object into a dict
update_notification_put_data_notifications_instance_id200_response_dict = update_notification_put_data_notifications_instance_id200_response_instance.to_dict()
# create an instance of UpdateNotificationPutDataNotificationsInstanceId200Response from a dict
update_notification_put_data_notifications_instance_id200_response_from_dict = UpdateNotificationPutDataNotificationsInstanceId200Response.from_dict(update_notification_put_data_notifications_instance_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


