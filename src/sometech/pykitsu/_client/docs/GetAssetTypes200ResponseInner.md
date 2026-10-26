# GetAssetTypes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Asset type unique identifier | [optional] 
**name** | **str** | Asset type name | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_asset_types200_response_inner import GetAssetTypes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetTypes200ResponseInner from a JSON string
get_asset_types200_response_inner_instance = GetAssetTypes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetAssetTypes200ResponseInner.to_json())

# convert the object into a dict
get_asset_types200_response_inner_dict = get_asset_types200_response_inner_instance.to_dict()
# create an instance of GetAssetTypes200ResponseInner from a dict
get_asset_types200_response_inner_from_dict = GetAssetTypes200ResponseInner.from_dict(get_asset_types200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


