# GetEventsGetDataEvents200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_events_get_data_events200_response_inner import GetEventsGetDataEvents200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventsGetDataEvents200ResponseInner from a JSON string
get_events_get_data_events200_response_inner_instance = GetEventsGetDataEvents200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetEventsGetDataEvents200ResponseInner.to_json())

# convert the object into a dict
get_events_get_data_events200_response_inner_dict = get_events_get_data_events200_response_inner_instance.to_dict()
# create an instance of GetEventsGetDataEvents200ResponseInner from a dict
get_events_get_data_events200_response_inner_from_dict = GetEventsGetDataEvents200ResponseInner.from_dict(get_events_get_data_events200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


