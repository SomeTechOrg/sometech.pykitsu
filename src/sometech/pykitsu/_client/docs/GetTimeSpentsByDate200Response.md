# GetTimeSpentsByDate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date of time spent | [optional] 
**total_duration** | **float** | Total duration in seconds | [optional] 
**entries** | [**List[GetTimeSpentsByDate200ResponseEntriesInner]**](GetTimeSpentsByDate200ResponseEntriesInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_time_spents_by_date200_response import GetTimeSpentsByDate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimeSpentsByDate200Response from a JSON string
get_time_spents_by_date200_response_instance = GetTimeSpentsByDate200Response.from_json(json)
# print the JSON string representation of the object
print(GetTimeSpentsByDate200Response.to_json())

# convert the object into a dict
get_time_spents_by_date200_response_dict = get_time_spents_by_date200_response_instance.to_dict()
# create an instance of GetTimeSpentsByDate200Response from a dict
get_time_spents_by_date200_response_from_dict = GetTimeSpentsByDate200Response.from_dict(get_time_spents_by_date200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


