# CreateProjectEpisodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**status** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_project_episode_request import CreateProjectEpisodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectEpisodeRequest from a JSON string
create_project_episode_request_instance = CreateProjectEpisodeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectEpisodeRequest.to_json())

# convert the object into a dict
create_project_episode_request_dict = create_project_episode_request_instance.to_dict()
# create an instance of CreateProjectEpisodeRequest from a dict
create_project_episode_request_from_dict = CreateProjectEpisodeRequest.from_dict(create_project_episode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


