# GetAssetOk200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Asset unique identifier | [optional] 
**name** | **str** | Asset name | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**entity_type_id** | **UUID** | Asset type identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_asset_ok200_response import GetAssetOk200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetOk200Response from a JSON string
get_asset_ok200_response_instance = GetAssetOk200Response.from_json(json)
# print the JSON string representation of the object
print(GetAssetOk200Response.to_json())

# convert the object into a dict
get_asset_ok200_response_dict = get_asset_ok200_response_instance.to_dict()
# create an instance of GetAssetOk200Response from a dict
get_asset_ok200_response_from_dict = GetAssetOk200Response.from_dict(get_asset_ok200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


