# CreateNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_id** | **UUID** |  | 
**comment_id** | **UUID** |  | 
**read** | **bool** |  | [optional] [default to False]

## Example

```python
from sometech.pykitsu._client.models.create_notification_request import CreateNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationRequest from a JSON string
create_notification_request_instance = CreateNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNotificationRequest.to_json())

# convert the object into a dict
create_notification_request_dict = create_notification_request_instance.to_dict()
# create an instance of CreateNotificationRequest from a dict
create_notification_request_from_dict = CreateNotificationRequest.from_dict(create_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


