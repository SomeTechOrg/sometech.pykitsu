# GetSequenceShotsGetDataUserSequencesSequenceIdShots200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Shot unique identifier | [optional] 
**name** | **str** | Shot name | [optional] 
**description** | **str** | Shot description | [optional] 
**sequence_id** | **UUID** | Sequence identifier | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_sequence_shots_get_data_user_sequences_sequence_id_shots200_response_inner import GetSequenceShotsGetDataUserSequencesSequenceIdShots200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSequenceShotsGetDataUserSequencesSequenceIdShots200ResponseInner from a JSON string
get_sequence_shots_get_data_user_sequences_sequence_id_shots200_response_inner_instance = GetSequenceShotsGetDataUserSequencesSequenceIdShots200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetSequenceShotsGetDataUserSequencesSequenceIdShots200ResponseInner.to_json())

# convert the object into a dict
get_sequence_shots_get_data_user_sequences_sequence_id_shots200_response_inner_dict = get_sequence_shots_get_data_user_sequences_sequence_id_shots200_response_inner_instance.to_dict()
# create an instance of GetSequenceShotsGetDataUserSequencesSequenceIdShots200ResponseInner from a dict
get_sequence_shots_get_data_user_sequences_sequence_id_shots200_response_inner_from_dict = GetSequenceShotsGetDataUserSequencesSequenceIdShots200ResponseInner.from_dict(get_sequence_shots_get_data_user_sequences_sequence_id_shots200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


