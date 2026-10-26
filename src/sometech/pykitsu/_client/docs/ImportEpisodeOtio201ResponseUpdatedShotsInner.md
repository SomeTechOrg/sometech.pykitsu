# ImportEpisodeOtio201ResponseUpdatedShotsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**nb_frames** | **int** |  | [optional] 
**data** | [**ImportOtioEdl201ResponseUpdatedShotsInnerData**](ImportOtioEdl201ResponseUpdatedShotsInnerData.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_episode_otio201_response_updated_shots_inner import ImportEpisodeOtio201ResponseUpdatedShotsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportEpisodeOtio201ResponseUpdatedShotsInner from a JSON string
import_episode_otio201_response_updated_shots_inner_instance = ImportEpisodeOtio201ResponseUpdatedShotsInner.from_json(json)
# print the JSON string representation of the object
print(ImportEpisodeOtio201ResponseUpdatedShotsInner.to_json())

# convert the object into a dict
import_episode_otio201_response_updated_shots_inner_dict = import_episode_otio201_response_updated_shots_inner_instance.to_dict()
# create an instance of ImportEpisodeOtio201ResponseUpdatedShotsInner from a dict
import_episode_otio201_response_updated_shots_inner_from_dict = ImportEpisodeOtio201ResponseUpdatedShotsInner.from_dict(import_episode_otio201_response_updated_shots_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


