# GetProjectEpisodesGetDataUserProjectsProjectIdEpisodes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Episode unique identifier | [optional] 
**name** | **str** | Episode name | [optional] 
**description** | **str** | Episode description | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_project_episodes_get_data_user_projects_project_id_episodes200_response_inner import GetProjectEpisodesGetDataUserProjectsProjectIdEpisodes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectEpisodesGetDataUserProjectsProjectIdEpisodes200ResponseInner from a JSON string
get_project_episodes_get_data_user_projects_project_id_episodes200_response_inner_instance = GetProjectEpisodesGetDataUserProjectsProjectIdEpisodes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectEpisodesGetDataUserProjectsProjectIdEpisodes200ResponseInner.to_json())

# convert the object into a dict
get_project_episodes_get_data_user_projects_project_id_episodes200_response_inner_dict = get_project_episodes_get_data_user_projects_project_id_episodes200_response_inner_instance.to_dict()
# create an instance of GetProjectEpisodesGetDataUserProjectsProjectIdEpisodes200ResponseInner from a dict
get_project_episodes_get_data_user_projects_project_id_episodes200_response_inner_from_dict = GetProjectEpisodesGetDataUserProjectsProjectIdEpisodes200ResponseInner.from_dict(get_project_episodes_get_data_user_projects_project_id_episodes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


