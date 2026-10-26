# ImportShotgunEpisodes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Episode unique identifier | [optional] 
**name** | **str** | Episode name | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_episodes200_response_inner import ImportShotgunEpisodes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunEpisodes200ResponseInner from a JSON string
import_shotgun_episodes200_response_inner_instance = ImportShotgunEpisodes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunEpisodes200ResponseInner.to_json())

# convert the object into a dict
import_shotgun_episodes200_response_inner_dict = import_shotgun_episodes200_response_inner_instance.to_dict()
# create an instance of ImportShotgunEpisodes200ResponseInner from a dict
import_shotgun_episodes200_response_inner_from_dict = ImportShotgunEpisodes200ResponseInner.from_dict(import_shotgun_episodes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


