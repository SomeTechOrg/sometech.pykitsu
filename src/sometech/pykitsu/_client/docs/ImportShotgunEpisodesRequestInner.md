# ImportShotgunEpisodesRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the episode | [optional] 
**code** | **str** | Episode code | [optional] 
**description** | **str** | Episode description | [optional] 
**project** | [**ImportShotgunEpisodesRequestInnerProject**](ImportShotgunEpisodesRequestInnerProject.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_episodes_request_inner import ImportShotgunEpisodesRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunEpisodesRequestInner from a JSON string
import_shotgun_episodes_request_inner_instance = ImportShotgunEpisodesRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunEpisodesRequestInner.to_json())

# convert the object into a dict
import_shotgun_episodes_request_inner_dict = import_shotgun_episodes_request_inner_instance.to_dict()
# create an instance of ImportShotgunEpisodesRequestInner from a dict
import_shotgun_episodes_request_inner_from_dict = ImportShotgunEpisodesRequestInner.from_dict(import_shotgun_episodes_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


