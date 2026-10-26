# ImportOtioEdl201ResponseCreatedShotsInner


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
from sometech.pykitsu._client.models.import_otio_edl201_response_created_shots_inner import ImportOtioEdl201ResponseCreatedShotsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportOtioEdl201ResponseCreatedShotsInner from a JSON string
import_otio_edl201_response_created_shots_inner_instance = ImportOtioEdl201ResponseCreatedShotsInner.from_json(json)
# print the JSON string representation of the object
print(ImportOtioEdl201ResponseCreatedShotsInner.to_json())

# convert the object into a dict
import_otio_edl201_response_created_shots_inner_dict = import_otio_edl201_response_created_shots_inner_instance.to_dict()
# create an instance of ImportOtioEdl201ResponseCreatedShotsInner from a dict
import_otio_edl201_response_created_shots_inner_from_dict = ImportOtioEdl201ResponseCreatedShotsInner.from_dict(import_otio_edl201_response_created_shots_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


