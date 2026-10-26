# GetMonthTimeSpents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_duration** | **float** | Total duration in hours | [optional] 
**year** | **int** | Year | [optional] 
**month** | **int** | Month | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_month_time_spents200_response import GetMonthTimeSpents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMonthTimeSpents200Response from a JSON string
get_month_time_spents200_response_instance = GetMonthTimeSpents200Response.from_json(json)
# print the JSON string representation of the object
print(GetMonthTimeSpents200Response.to_json())

# convert the object into a dict
get_month_time_spents200_response_dict = get_month_time_spents200_response_instance.to_dict()
# create an instance of GetMonthTimeSpents200Response from a dict
get_month_time_spents200_response_from_dict = GetMonthTimeSpents200Response.from_dict(get_month_time_spents200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


