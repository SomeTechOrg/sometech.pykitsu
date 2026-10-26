# GetShotsCastingAsset200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Shot unique identifier | [optional] 
**name** | **str** | Shot name | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**sequence_id** | **UUID** | Sequence identifier | [optional] 
**frame_in** | **int** | Frame in | [optional] 
**frame_out** | **int** | Frame out | [optional] 
**duration** | **int** | Shot duration in frames | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_shots_casting_asset200_response_inner import GetShotsCastingAsset200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetShotsCastingAsset200ResponseInner from a JSON string
get_shots_casting_asset200_response_inner_instance = GetShotsCastingAsset200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetShotsCastingAsset200ResponseInner.to_json())

# convert the object into a dict
get_shots_casting_asset200_response_inner_dict = get_shots_casting_asset200_response_inner_instance.to_dict()
# create an instance of GetShotsCastingAsset200ResponseInner from a dict
get_shots_casting_asset200_response_inner_from_dict = GetShotsCastingAsset200ResponseInner.from_dict(get_shots_casting_asset200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


