# GetTimeSpentsGetDataUserTimeSpents200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Time spent unique identifier | [optional] 
**person_id** | **UUID** | Person identifier | [optional] 
**task_id** | **UUID** | Task identifier | [optional] 
**var_date** | **date** | Date of time spent | [optional] 
**duration** | **float** | Duration in seconds | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_time_spents_get_data_user_time_spents200_response_inner import GetTimeSpentsGetDataUserTimeSpents200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimeSpentsGetDataUserTimeSpents200ResponseInner from a JSON string
get_time_spents_get_data_user_time_spents200_response_inner_instance = GetTimeSpentsGetDataUserTimeSpents200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetTimeSpentsGetDataUserTimeSpents200ResponseInner.to_json())

# convert the object into a dict
get_time_spents_get_data_user_time_spents200_response_inner_dict = get_time_spents_get_data_user_time_spents200_response_inner_instance.to_dict()
# create an instance of GetTimeSpentsGetDataUserTimeSpents200ResponseInner from a dict
get_time_spents_get_data_user_time_spents200_response_inner_from_dict = GetTimeSpentsGetDataUserTimeSpents200ResponseInner.from_dict(get_time_spents_get_data_user_time_spents200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


