# Notification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | **bool** | True if user read it, False otherwise | [optional] 
**change** | **bool** | True if there is status change related to this status, False otherwise | [optional] 
**person_id** | **UUID** | The user to who the notification is aimed at | [optional] 
**author_id** | **UUID** | Author of the event to notify | [optional] 
**comment_id** | **UUID** | Comment related to the notification, if there is any | [optional] 
**task_id** | **UUID** | Task related to the notification, if there is any | [optional] 
**reply_id** | **UUID** | Reply related to notification | [optional] 
**type** | **str** | Type of notification | [optional] 
**id** | **UUID** | Notification unique identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print(Notification.to_json())

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_from_dict = Notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


