# GetDayTimeSpents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_duration** | **float** | Total duration in hours | [optional] 
**year** | **int** | Year | [optional] 
**month** | **int** | Month | [optional] 
**day** | **int** | Day | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_day_time_spents200_response import GetDayTimeSpents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDayTimeSpents200Response from a JSON string
get_day_time_spents200_response_instance = GetDayTimeSpents200Response.from_json(json)
# print the JSON string representation of the object
print(GetDayTimeSpents200Response.to_json())

# convert the object into a dict
get_day_time_spents200_response_dict = get_day_time_spents200_response_instance.to_dict()
# create an instance of GetDayTimeSpents200Response from a dict
get_day_time_spents200_response_from_dict = GetDayTimeSpents200Response.from_dict(get_day_time_spents200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


