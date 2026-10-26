# SubscriptionToNotifications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_id** | **UUID** | Person ID | [optional] 
**task_id** | **UUID** | Task ID | [optional] 
**entity_id** | **UUID** | Entity ID | [optional] 
**task_type_id** | **UUID** | Task type ID | [optional] 

## Example

```python
from sometech.pykitsu._client.models.subscription_to_notifications import SubscriptionToNotifications

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionToNotifications from a JSON string
subscription_to_notifications_instance = SubscriptionToNotifications.from_json(json)
# print the JSON string representation of the object
print(SubscriptionToNotifications.to_json())

# convert the object into a dict
subscription_to_notifications_dict = subscription_to_notifications_instance.to_dict()
# create an instance of SubscriptionToNotifications from a dict
subscription_to_notifications_from_dict = SubscriptionToNotifications.from_dict(subscription_to_notifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


