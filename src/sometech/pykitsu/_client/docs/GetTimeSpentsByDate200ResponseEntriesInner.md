# GetTimeSpentsByDate200ResponseEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Time spent unique identifier | [optional] 
**task_id** | **UUID** | Task identifier | [optional] 
**duration** | **float** | Duration in seconds | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_time_spents_by_date200_response_entries_inner import GetTimeSpentsByDate200ResponseEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimeSpentsByDate200ResponseEntriesInner from a JSON string
get_time_spents_by_date200_response_entries_inner_instance = GetTimeSpentsByDate200ResponseEntriesInner.from_json(json)
# print the JSON string representation of the object
print(GetTimeSpentsByDate200ResponseEntriesInner.to_json())

# convert the object into a dict
get_time_spents_by_date200_response_entries_inner_dict = get_time_spents_by_date200_response_entries_inner_instance.to_dict()
# create an instance of GetTimeSpentsByDate200ResponseEntriesInner from a dict
get_time_spents_by_date200_response_entries_inner_from_dict = GetTimeSpentsByDate200ResponseEntriesInner.from_dict(get_time_spents_by_date200_response_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


