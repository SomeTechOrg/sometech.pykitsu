# SetShotsFramesRequestShotsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shot_id** | **UUID** |  | [optional] 
**nb_frames** | **int** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.set_shots_frames_request_shots_inner import SetShotsFramesRequestShotsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SetShotsFramesRequestShotsInner from a JSON string
set_shots_frames_request_shots_inner_instance = SetShotsFramesRequestShotsInner.from_json(json)
# print the JSON string representation of the object
print(SetShotsFramesRequestShotsInner.to_json())

# convert the object into a dict
set_shots_frames_request_shots_inner_dict = set_shots_frames_request_shots_inner_instance.to_dict()
# create an instance of SetShotsFramesRequestShotsInner from a dict
set_shots_frames_request_shots_inner_from_dict = SetShotsFramesRequestShotsInner.from_dict(set_shots_frames_request_shots_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


