# GetTaskTimeSpentGetDataUserTasksTaskIdTimeSpentsDate200Response


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
from sometech.pykitsu._client.models.get_task_time_spent_get_data_user_tasks_task_id_time_spents_date200_response import GetTaskTimeSpentGetDataUserTasksTaskIdTimeSpentsDate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaskTimeSpentGetDataUserTasksTaskIdTimeSpentsDate200Response from a JSON string
get_task_time_spent_get_data_user_tasks_task_id_time_spents_date200_response_instance = GetTaskTimeSpentGetDataUserTasksTaskIdTimeSpentsDate200Response.from_json(json)
# print the JSON string representation of the object
print(GetTaskTimeSpentGetDataUserTasksTaskIdTimeSpentsDate200Response.to_json())

# convert the object into a dict
get_task_time_spent_get_data_user_tasks_task_id_time_spents_date200_response_dict = get_task_time_spent_get_data_user_tasks_task_id_time_spents_date200_response_instance.to_dict()
# create an instance of GetTaskTimeSpentGetDataUserTasksTaskIdTimeSpentsDate200Response from a dict
get_task_time_spent_get_data_user_tasks_task_id_time_spents_date200_response_from_dict = GetTaskTimeSpentGetDataUserTasksTaskIdTimeSpentsDate200Response.from_dict(get_task_time_spent_get_data_user_tasks_task_id_time_spents_date200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


