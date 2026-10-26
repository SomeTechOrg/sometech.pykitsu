# GetEpisodeRetakeStats200ResponseValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_retake_count** | **int** |  | [optional] 
**evolution** | [**Dict[str, GetEpisodeRetakeStats200ResponseValueEvolutionValue]**](GetEpisodeRetakeStats200ResponseValueEvolutionValue.md) |  | [optional] 
**done** | [**GetEpisodeRetakeStats200ResponseValueDone**](GetEpisodeRetakeStats200ResponseValueDone.md) |  | [optional] 
**retake** | [**GetEpisodeRetakeStats200ResponseValueRetake**](GetEpisodeRetakeStats200ResponseValueRetake.md) |  | [optional] 
**other** | [**GetEpisodeRetakeStats200ResponseValueOther**](GetEpisodeRetakeStats200ResponseValueOther.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_episode_retake_stats200_response_value import GetEpisodeRetakeStats200ResponseValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetEpisodeRetakeStats200ResponseValue from a JSON string
get_episode_retake_stats200_response_value_instance = GetEpisodeRetakeStats200ResponseValue.from_json(json)
# print the JSON string representation of the object
print(GetEpisodeRetakeStats200ResponseValue.to_json())

# convert the object into a dict
get_episode_retake_stats200_response_value_dict = get_episode_retake_stats200_response_value_instance.to_dict()
# create an instance of GetEpisodeRetakeStats200ResponseValue from a dict
get_episode_retake_stats200_response_value_from_dict = GetEpisodeRetakeStats200ResponseValue.from_dict(get_episode_retake_stats200_response_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


