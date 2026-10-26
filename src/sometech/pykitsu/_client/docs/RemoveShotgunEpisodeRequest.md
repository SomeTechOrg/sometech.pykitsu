# RemoveShotgunEpisodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the episode to remove | 

## Example

```python
from sometech.pykitsu._client.models.remove_shotgun_episode_request import RemoveShotgunEpisodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveShotgunEpisodeRequest from a JSON string
remove_shotgun_episode_request_instance = RemoveShotgunEpisodeRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveShotgunEpisodeRequest.to_json())

# convert the object into a dict
remove_shotgun_episode_request_dict = remove_shotgun_episode_request_instance.to_dict()
# create an instance of RemoveShotgunEpisodeRequest from a dict
remove_shotgun_episode_request_from_dict = RemoveShotgunEpisodeRequest.from_dict(remove_shotgun_episode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


