# GetEventsGetDataEventsLast200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Event unique identifier | [optional] 
**name** | **str** | Event name | [optional] 
**data** | **object** | Event data content | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**created_at** | **datetime** | Event timestamp | [optional] 
**user_id** | **UUID** | User identifier who triggered the event | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_events_get_data_events_last200_response_inner import GetEventsGetDataEventsLast200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventsGetDataEventsLast200ResponseInner from a JSON string
get_events_get_data_events_last200_response_inner_instance = GetEventsGetDataEventsLast200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetEventsGetDataEventsLast200ResponseInner.to_json())

# convert the object into a dict
get_events_get_data_events_last200_response_inner_dict = get_events_get_data_events_last200_response_inner_instance.to_dict()
# create an instance of GetEventsGetDataEventsLast200ResponseInner from a dict
get_events_get_data_events_last200_response_inner_from_dict = GetEventsGetDataEventsLast200ResponseInner.from_dict(get_events_get_data_events_last200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


