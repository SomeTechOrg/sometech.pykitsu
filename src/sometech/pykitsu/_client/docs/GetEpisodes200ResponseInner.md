# GetEpisodes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_episodes200_response_inner import GetEpisodes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEpisodes200ResponseInner from a JSON string
get_episodes200_response_inner_instance = GetEpisodes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetEpisodes200ResponseInner.to_json())

# convert the object into a dict
get_episodes200_response_inner_dict = get_episodes200_response_inner_instance.to_dict()
# create an instance of GetEpisodes200ResponseInner from a dict
get_episodes200_response_inner_from_dict = GetEpisodes200ResponseInner.from_dict(get_episodes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


