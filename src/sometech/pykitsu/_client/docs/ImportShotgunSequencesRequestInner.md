# ImportShotgunSequencesRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the sequence | [optional] 
**code** | **str** | Sequence code | [optional] 
**description** | **str** | Sequence description | [optional] 
**project** | [**ImportShotgunEpisodesRequestInnerProject**](ImportShotgunEpisodesRequestInnerProject.md) |  | [optional] 
**episode** | [**ImportShotgunSequencesRequestInnerEpisode**](ImportShotgunSequencesRequestInnerEpisode.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_sequences_request_inner import ImportShotgunSequencesRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunSequencesRequestInner from a JSON string
import_shotgun_sequences_request_inner_instance = ImportShotgunSequencesRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunSequencesRequestInner.to_json())

# convert the object into a dict
import_shotgun_sequences_request_inner_dict = import_shotgun_sequences_request_inner_instance.to_dict()
# create an instance of ImportShotgunSequencesRequestInner from a dict
import_shotgun_sequences_request_inner_from_dict = ImportShotgunSequencesRequestInner.from_dict(import_shotgun_sequences_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


