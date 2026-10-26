# GetProductionTaskTypeTimeSpents200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Time spent unique identifier | [optional] 
**person_id** | **UUID** | Person unique identifier | [optional] 
**duration** | **float** | Time spent duration in hours | [optional] 
**var_date** | **date** | Date of time spent entry | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_production_task_type_time_spents200_response_inner import GetProductionTaskTypeTimeSpents200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductionTaskTypeTimeSpents200ResponseInner from a JSON string
get_production_task_type_time_spents200_response_inner_instance = GetProductionTaskTypeTimeSpents200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProductionTaskTypeTimeSpents200ResponseInner.to_json())

# convert the object into a dict
get_production_task_type_time_spents200_response_inner_dict = get_production_task_type_time_spents200_response_inner_instance.to_dict()
# create an instance of GetProductionTaskTypeTimeSpents200ResponseInner from a dict
get_production_task_type_time_spents200_response_inner_from_dict = GetProductionTaskTypeTimeSpents200ResponseInner.from_dict(get_production_task_type_time_spents200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


