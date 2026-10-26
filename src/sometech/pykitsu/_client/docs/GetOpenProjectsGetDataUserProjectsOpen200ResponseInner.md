# GetOpenProjectsGetDataUserProjectsOpen200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Project unique identifier | [optional] 
**name** | **str** | Project name | [optional] 
**description** | **str** | Project description | [optional] 
**status** | **str** | Project status | [optional] 
**fps** | **float** | Frames per second | [optional] 
**ratio** | **str** | Aspect ratio | [optional] 
**resolution** | **str** | Project resolution | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_open_projects_get_data_user_projects_open200_response_inner import GetOpenProjectsGetDataUserProjectsOpen200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenProjectsGetDataUserProjectsOpen200ResponseInner from a JSON string
get_open_projects_get_data_user_projects_open200_response_inner_instance = GetOpenProjectsGetDataUserProjectsOpen200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetOpenProjectsGetDataUserProjectsOpen200ResponseInner.to_json())

# convert the object into a dict
get_open_projects_get_data_user_projects_open200_response_inner_dict = get_open_projects_get_data_user_projects_open200_response_inner_instance.to_dict()
# create an instance of GetOpenProjectsGetDataUserProjectsOpen200ResponseInner from a dict
get_open_projects_get_data_user_projects_open200_response_inner_from_dict = GetOpenProjectsGetDataUserProjectsOpen200ResponseInner.from_dict(get_open_projects_get_data_user_projects_open200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


