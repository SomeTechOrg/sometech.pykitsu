# GetOpenProjectsGetDataProjectsOpen200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Project unique identifier | [optional] 
**name** | **str** | Project name | [optional] 
**project_status_id** | **UUID** | Project status unique identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_open_projects_get_data_projects_open200_response_inner import GetOpenProjectsGetDataProjectsOpen200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenProjectsGetDataProjectsOpen200ResponseInner from a JSON string
get_open_projects_get_data_projects_open200_response_inner_instance = GetOpenProjectsGetDataProjectsOpen200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetOpenProjectsGetDataProjectsOpen200ResponseInner.to_json())

# convert the object into a dict
get_open_projects_get_data_projects_open200_response_inner_dict = get_open_projects_get_data_projects_open200_response_inner_instance.to_dict()
# create an instance of GetOpenProjectsGetDataProjectsOpen200ResponseInner from a dict
get_open_projects_get_data_projects_open200_response_inner_from_dict = GetOpenProjectsGetDataProjectsOpen200ResponseInner.from_dict(get_open_projects_get_data_projects_open200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


