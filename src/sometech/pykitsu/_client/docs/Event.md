# Event


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of event | [optional] 
**user_id** | **UUID** | The user who made the action that emitted the event | [optional] 
**project_id** | **UUID** | Project ID | [optional] 
**data** | **str** | Free JSON field to add metadata | [optional] 

## Example

```python
from sometech.pykitsu._client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


