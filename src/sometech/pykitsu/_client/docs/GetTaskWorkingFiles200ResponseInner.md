# GetTaskWorkingFiles200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Working file unique identifier | [optional] 
**name** | **str** | Working file name | [optional] 
**revision** | **int** | Working file revision | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 
**task_id** | **UUID** | Task identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_task_working_files200_response_inner import GetTaskWorkingFiles200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaskWorkingFiles200ResponseInner from a JSON string
get_task_working_files200_response_inner_instance = GetTaskWorkingFiles200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetTaskWorkingFiles200ResponseInner.to_json())

# convert the object into a dict
get_task_working_files200_response_inner_dict = get_task_working_files200_response_inner_instance.to_dict()
# create an instance of GetTaskWorkingFiles200ResponseInner from a dict
get_task_working_files200_response_inner_from_dict = GetTaskWorkingFiles200ResponseInner.from_dict(get_task_working_files200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


