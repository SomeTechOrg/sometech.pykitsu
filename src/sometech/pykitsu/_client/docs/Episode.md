# Episode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of episode | [optional] 
**code** | **str** | Utility field for the pipeline to identify the episode | [optional] 
**description** | **str** | Episode brief | [optional] 
**canceled** | **bool** | True if the episode has been delete one time, False otherwise | [optional] [default to False]
**project_id** | **UUID** | Project ID | [optional] 
**source_id** | **UUID** | Field used to set the episode_id | [optional] 
**preview_file_id** | **UUID** | ID of preview file used as thumbnail | [optional] 
**data** | **str** | Free JSON field to add metadata | [optional] 
**shotgun_id** | **int** | Used for synchronization with a Shotgun instance | [optional] 
**id** | **UUID** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.episode import Episode

# TODO update the JSON string below
json = "{}"
# create an instance of Episode from a JSON string
episode_instance = Episode.from_json(json)
# print the JSON string representation of the object
print(Episode.to_json())

# convert the object into a dict
episode_dict = episode_instance.to_dict()
# create an instance of Episode from a dict
episode_from_dict = Episode.from_dict(episode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


