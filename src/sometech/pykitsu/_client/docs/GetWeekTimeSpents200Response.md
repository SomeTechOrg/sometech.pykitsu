# GetWeekTimeSpents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_duration** | **float** | Total duration in hours | [optional] 
**year** | **int** | Year | [optional] 
**week** | **int** | Week number | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_week_time_spents200_response import GetWeekTimeSpents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWeekTimeSpents200Response from a JSON string
get_week_time_spents200_response_instance = GetWeekTimeSpents200Response.from_json(json)
# print the JSON string representation of the object
print(GetWeekTimeSpents200Response.to_json())

# convert the object into a dict
get_week_time_spents200_response_dict = get_week_time_spents200_response_instance.to_dict()
# create an instance of GetWeekTimeSpents200Response from a dict
get_week_time_spents200_response_from_dict = GetWeekTimeSpents200Response.from_dict(get_week_time_spents200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


