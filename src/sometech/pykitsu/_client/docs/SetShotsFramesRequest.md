# SetShotsFramesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shots** | [**List[SetShotsFramesRequestShotsInner]**](SetShotsFramesRequestShotsInner.md) |  | 

## Example

```python
from sometech.pykitsu._client.models.set_shots_frames_request import SetShotsFramesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetShotsFramesRequest from a JSON string
set_shots_frames_request_instance = SetShotsFramesRequest.from_json(json)
# print the JSON string representation of the object
print(SetShotsFramesRequest.to_json())

# convert the object into a dict
set_shots_frames_request_dict = set_shots_frames_request_instance.to_dict()
# create an instance of SetShotsFramesRequest from a dict
set_shots_frames_request_from_dict = SetShotsFramesRequest.from_dict(set_shots_frames_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


