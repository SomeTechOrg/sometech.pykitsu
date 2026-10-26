# GetScenesAndTasks200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**tasks** | [**List[GetScenesAndTasks200ResponseInnerTasksInner]**](GetScenesAndTasks200ResponseInnerTasksInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_scenes_and_tasks200_response_inner import GetScenesAndTasks200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetScenesAndTasks200ResponseInner from a JSON string
get_scenes_and_tasks200_response_inner_instance = GetScenesAndTasks200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetScenesAndTasks200ResponseInner.to_json())

# convert the object into a dict
get_scenes_and_tasks200_response_inner_dict = get_scenes_and_tasks200_response_inner_instance.to_dict()
# create an instance of GetScenesAndTasks200ResponseInner from a dict
get_scenes_and_tasks200_response_inner_from_dict = GetScenesAndTasks200ResponseInner.from_dict(get_scenes_and_tasks200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


