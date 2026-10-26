# Sequence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of sequence | [optional] 
**code** | **str** | Utility field for the pipeline to identify the sequence | [optional] 
**description** | **str** | Sequence brief | [optional] 
**canceled** | **bool** | True if the sequence has been delete one time, False otherwise | [optional] [default to False]
**project_id** | **UUID** | Project ID | [optional] 
**parent_id** | **UUID** | Episode ID | [optional] 
**source_id** | **UUID** | Field used to set the episode_id | [optional] 
**preview_file_id** | **UUID** | ID of preview file used as thumbnail | [optional] 
**data** | **str** | Free JSON field to add metadata | [optional] 
**shotgun_id** | **int** | Used for synchronization with a Shotgun instance | [optional] 
**id** | **UUID** |  | [optional] 
**episode_id** | **UUID** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.sequence import Sequence

# TODO update the JSON string below
json = "{}"
# create an instance of Sequence from a JSON string
sequence_instance = Sequence.from_json(json)
# print the JSON string representation of the object
print(Sequence.to_json())

# convert the object into a dict
sequence_dict = sequence_instance.to_dict()
# create an instance of Sequence from a dict
sequence_from_dict = Sequence.from_dict(sequence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


