# ImportOtioEdl201ResponseUpdatedShotsInner


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
from sometech.pykitsu._client.models.import_otio_edl201_response_updated_shots_inner import ImportOtioEdl201ResponseUpdatedShotsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportOtioEdl201ResponseUpdatedShotsInner from a JSON string
import_otio_edl201_response_updated_shots_inner_instance = ImportOtioEdl201ResponseUpdatedShotsInner.from_json(json)
# print the JSON string representation of the object
print(ImportOtioEdl201ResponseUpdatedShotsInner.to_json())

# convert the object into a dict
import_otio_edl201_response_updated_shots_inner_dict = import_otio_edl201_response_updated_shots_inner_instance.to_dict()
# create an instance of ImportOtioEdl201ResponseUpdatedShotsInner from a dict
import_otio_edl201_response_updated_shots_inner_from_dict = ImportOtioEdl201ResponseUpdatedShotsInner.from_dict(import_otio_edl201_response_updated_shots_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


