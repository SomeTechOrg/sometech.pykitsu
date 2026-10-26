# UpdateEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_event_request import UpdateEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEventRequest from a JSON string
update_event_request_instance = UpdateEventRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEventRequest.to_json())

# convert the object into a dict
update_event_request_dict = update_event_request_instance.to_dict()
# create an instance of UpdateEventRequest from a dict
update_event_request_from_dict = UpdateEventRequest.from_dict(update_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


