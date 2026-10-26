# CreateSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_id** | **UUID** |  | 
**entity_id** | **UUID** |  | 

## Example

```python
from sometech.pykitsu._client.models.create_subscription_request import CreateSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionRequest from a JSON string
create_subscription_request_instance = CreateSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionRequest.to_json())

# convert the object into a dict
create_subscription_request_dict = create_subscription_request_instance.to_dict()
# create an instance of CreateSubscriptionRequest from a dict
create_subscription_request_from_dict = CreateSubscriptionRequest.from_dict(create_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


