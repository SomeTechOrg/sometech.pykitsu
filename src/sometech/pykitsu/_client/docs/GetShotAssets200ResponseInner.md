# GetShotAssets200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**entity_type_id** | **UUID** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_shot_assets200_response_inner import GetShotAssets200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetShotAssets200ResponseInner from a JSON string
get_shot_assets200_response_inner_instance = GetShotAssets200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetShotAssets200ResponseInner.to_json())

# convert the object into a dict
get_shot_assets200_response_inner_dict = get_shot_assets200_response_inner_instance.to_dict()
# create an instance of GetShotAssets200ResponseInner from a dict
get_shot_assets200_response_inner_from_dict = GetShotAssets200ResponseInner.from_dict(get_shot_assets200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


