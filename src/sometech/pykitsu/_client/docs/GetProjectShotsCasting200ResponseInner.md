# GetProjectShotsCasting200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shot_id** | **UUID** | Shot unique identifier | [optional] 
**shot_name** | **str** | Shot name | [optional] 
**sequence_id** | **UUID** | Sequence identifier | [optional] 
**sequence_name** | **str** | Sequence name | [optional] 
**casting** | [**List[GetEpisodesCasting200ResponseInnerCastingInner]**](GetEpisodesCasting200ResponseInnerCastingInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_project_shots_casting200_response_inner import GetProjectShotsCasting200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectShotsCasting200ResponseInner from a JSON string
get_project_shots_casting200_response_inner_instance = GetProjectShotsCasting200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectShotsCasting200ResponseInner.to_json())

# convert the object into a dict
get_project_shots_casting200_response_inner_dict = get_project_shots_casting200_response_inner_instance.to_dict()
# create an instance of GetProjectShotsCasting200ResponseInner from a dict
get_project_shots_casting200_response_inner_from_dict = GetProjectShotsCasting200ResponseInner.from_dict(get_project_shots_casting200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


