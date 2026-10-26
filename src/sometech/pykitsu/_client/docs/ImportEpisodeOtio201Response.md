# ImportEpisodeOtio201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_shots** | [**List[ImportEpisodeOtio201ResponseUpdatedShotsInner]**](ImportEpisodeOtio201ResponseUpdatedShotsInner.md) |  | [optional] 
**created_shots** | [**List[ImportEpisodeOtio201ResponseCreatedShotsInner]**](ImportEpisodeOtio201ResponseCreatedShotsInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_episode_otio201_response import ImportEpisodeOtio201Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImportEpisodeOtio201Response from a JSON string
import_episode_otio201_response_instance = ImportEpisodeOtio201Response.from_json(json)
# print the JSON string representation of the object
print(ImportEpisodeOtio201Response.to_json())

# convert the object into a dict
import_episode_otio201_response_dict = import_episode_otio201_response_instance.to_dict()
# create an instance of ImportEpisodeOtio201Response from a dict
import_episode_otio201_response_from_dict = ImportEpisodeOtio201Response.from_dict(import_episode_otio201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


