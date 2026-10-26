# GetShotTaskTypesGetDataUserShotsShotIdTaskTypes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Task type unique identifier | [optional] 
**name** | **str** | Task type name | [optional] 
**short_name** | **str** | Task type short name | [optional] 
**color** | **str** | Task type color | [optional] 
**priority** | **int** | Task type priority | [optional] 
**for_entity** | **str** | Entity type this task type applies to | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_shot_task_types_get_data_user_shots_shot_id_task_types200_response_inner import GetShotTaskTypesGetDataUserShotsShotIdTaskTypes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetShotTaskTypesGetDataUserShotsShotIdTaskTypes200ResponseInner from a JSON string
get_shot_task_types_get_data_user_shots_shot_id_task_types200_response_inner_instance = GetShotTaskTypesGetDataUserShotsShotIdTaskTypes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetShotTaskTypesGetDataUserShotsShotIdTaskTypes200ResponseInner.to_json())

# convert the object into a dict
get_shot_task_types_get_data_user_shots_shot_id_task_types200_response_inner_dict = get_shot_task_types_get_data_user_shots_shot_id_task_types200_response_inner_instance.to_dict()
# create an instance of GetShotTaskTypesGetDataUserShotsShotIdTaskTypes200ResponseInner from a dict
get_shot_task_types_get_data_user_shots_shot_id_task_types200_response_inner_from_dict = GetShotTaskTypesGetDataUserShotsShotIdTaskTypes200ResponseInner.from_dict(get_shot_task_types_get_data_user_shots_shot_id_task_types200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


