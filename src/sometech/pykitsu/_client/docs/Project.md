# Project


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of project | [optional] 
**code** | **str** | Utility field for the pipeline to identify the project | [optional] 
**description** | **str** | Project brief | [optional] 
**shotgun_id** | **int** | Used for synchronization with a Shotgun instance | [optional] 
**file_tree** | **str** | Templates to use to build file paths | [optional] 
**data** | **str** | Free JSON field to add metadata | [optional] 
**project_status_id** | **UUID** | Project status ID | [optional] 
**has_avatar** | **bool** | True if the project has an avatar, False otherwise | [optional] [default to False]
**fps** | **str** | Frames per second | [optional] 
**ratio** | **str** |  | [optional] 
**resolution** | **str** |  | [optional] 
**production_type** | **str** | short, featurefilm or tvshow | [optional] [default to 'short']
**end_date** | **date** |  | [optional] 
**start_date** | **date** |  | [optional] 
**man_days** | **int** | Estimated number of working days to complete the project | [optional] 
**nb_episodes** | **int** |  | [optional] 
**episode_span** | **int** |  | [optional] 
**max_retakes** | **int** |  | [optional] 
**is_clients_isolated** | **bool** | True if the clients are isolated from the project, False otherwise | [optional] [default to False]

## Example

```python
from sometech.pykitsu._client.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


