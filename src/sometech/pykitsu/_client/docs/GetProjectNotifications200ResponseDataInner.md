# GetProjectNotifications200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**task_id** | **UUID** |  | [optional] 
**comment_id** | **UUID** |  | [optional] 
**notification_type** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_project_notifications200_response_data_inner import GetProjectNotifications200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectNotifications200ResponseDataInner from a JSON string
get_project_notifications200_response_data_inner_instance = GetProjectNotifications200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectNotifications200ResponseDataInner.to_json())

# convert the object into a dict
get_project_notifications200_response_data_inner_dict = get_project_notifications200_response_data_inner_instance.to_dict()
# create an instance of GetProjectNotifications200ResponseDataInner from a dict
get_project_notifications200_response_data_inner_from_dict = GetProjectNotifications200ResponseDataInner.from_dict(get_project_notifications200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


