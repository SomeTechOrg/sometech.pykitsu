# ImportEpisodeOtio201ResponseCreatedShotsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**nb_frames** | **int** |  | [optional] 
**data** | [**ImportOtioEdl201ResponseCreatedShotsInnerData**](ImportOtioEdl201ResponseCreatedShotsInnerData.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_episode_otio201_response_created_shots_inner import ImportEpisodeOtio201ResponseCreatedShotsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportEpisodeOtio201ResponseCreatedShotsInner from a JSON string
import_episode_otio201_response_created_shots_inner_instance = ImportEpisodeOtio201ResponseCreatedShotsInner.from_json(json)
# print the JSON string representation of the object
print(ImportEpisodeOtio201ResponseCreatedShotsInner.to_json())

# convert the object into a dict
import_episode_otio201_response_created_shots_inner_dict = import_episode_otio201_response_created_shots_inner_instance.to_dict()
# create an instance of ImportEpisodeOtio201ResponseCreatedShotsInner from a dict
import_episode_otio201_response_created_shots_inner_from_dict = ImportEpisodeOtio201ResponseCreatedShotsInner.from_dict(import_episode_otio201_response_created_shots_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


