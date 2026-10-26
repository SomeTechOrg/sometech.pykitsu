# Shot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of shot | [optional] 
**code** | **str** | Utility field for the pipeline to identify the shot | [optional] 
**description** | **str** | Shot brief | [optional] 
**canceled** | **bool** | True if the shot has been delete one time, False otherwise | [optional] [default to False]
**project_id** | **UUID** | Project ID | [optional] 
**parent_id** | **UUID** | Episode ID | [optional] 
**entity_type_id** | **UUID** | Shot type ID | [optional] 
**source_id** | **UUID** | Field used to set the episode_id | [optional] 
**preview_file_id** | **UUID** | ID of preview file used as thumbnail | [optional] 
**data** | **str** | Free JSON field to add metadata | [optional] 
**shotgun_id** | **int** | Used for synchronization with a Shotgun instance | [optional] 
**id** | **UUID** |  | [optional] 
**nb_frames** | **int** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.shot import Shot

# TODO update the JSON string below
json = "{}"
# create an instance of Shot from a JSON string
shot_instance = Shot.from_json(json)
# print the JSON string representation of the object
print(Shot.to_json())

# convert the object into a dict
shot_dict = shot_instance.to_dict()
# create an instance of Shot from a dict
shot_from_dict = Shot.from_dict(shot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


