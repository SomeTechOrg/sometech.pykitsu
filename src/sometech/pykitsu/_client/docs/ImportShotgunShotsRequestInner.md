# ImportShotgunShotsRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the shot | [optional] 
**code** | **str** | Shot code | [optional] 
**sg_cut_in** | **int** | Cut in frame | [optional] 
**sg_cut_duration** | **int** | Cut duration in frames | [optional] 
**project** | [**ImportShotgunEpisodesRequestInnerProject**](ImportShotgunEpisodesRequestInnerProject.md) |  | [optional] 
**sg_sequence** | [**ImportShotgunShotsRequestInnerSgSequence**](ImportShotgunShotsRequestInnerSgSequence.md) |  | [optional] 
**sg_scene** | [**ImportShotgunShotsRequestInnerSgScene**](ImportShotgunShotsRequestInnerSgScene.md) |  | [optional] 
**assets** | [**List[ImportShotgunShotsRequestInnerAssetsInner]**](ImportShotgunShotsRequestInnerAssetsInner.md) | Linked assets | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_shots_request_inner import ImportShotgunShotsRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunShotsRequestInner from a JSON string
import_shotgun_shots_request_inner_instance = ImportShotgunShotsRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunShotsRequestInner.to_json())

# convert the object into a dict
import_shotgun_shots_request_inner_dict = import_shotgun_shots_request_inner_instance.to_dict()
# create an instance of ImportShotgunShotsRequestInner from a dict
import_shotgun_shots_request_inner_from_dict = ImportShotgunShotsRequestInner.from_dict(import_shotgun_shots_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


