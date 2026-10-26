# ImportShotgunScenesRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the scene | [optional] 
**code** | **str** | Scene code | [optional] 
**project** | [**ImportShotgunEpisodesRequestInnerProject**](ImportShotgunEpisodesRequestInnerProject.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_scenes_request_inner import ImportShotgunScenesRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunScenesRequestInner from a JSON string
import_shotgun_scenes_request_inner_instance = ImportShotgunScenesRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunScenesRequestInner.to_json())

# convert the object into a dict
import_shotgun_scenes_request_inner_dict = import_shotgun_scenes_request_inner_instance.to_dict()
# create an instance of ImportShotgunScenesRequestInner from a dict
import_shotgun_scenes_request_inner_from_dict = ImportShotgunScenesRequestInner.from_dict(import_shotgun_scenes_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


