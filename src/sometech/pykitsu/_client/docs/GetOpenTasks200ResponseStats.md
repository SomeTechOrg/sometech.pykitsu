# GetOpenTasks200ResponseStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of tasks | [optional] 
**total_duration** | **int** | Total duration of tasks in minutes | [optional] 
**total_estimation** | **int** | Total estimation of tasks in minutes | [optional] 
**status** | **object** | Number of tasks per status | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_open_tasks200_response_stats import GetOpenTasks200ResponseStats

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenTasks200ResponseStats from a JSON string
get_open_tasks200_response_stats_instance = GetOpenTasks200ResponseStats.from_json(json)
# print the JSON string representation of the object
print(GetOpenTasks200ResponseStats.to_json())

# convert the object into a dict
get_open_tasks200_response_stats_dict = get_open_tasks200_response_stats_instance.to_dict()
# create an instance of GetOpenTasks200ResponseStats from a dict
get_open_tasks200_response_stats_from_dict = GetOpenTasks200ResponseStats.from_dict(get_open_tasks200_response_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


