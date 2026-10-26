# GetAssetInstance200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**asset_id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_asset_instance200_response import GetAssetInstance200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetInstance200Response from a JSON string
get_asset_instance200_response_instance = GetAssetInstance200Response.from_json(json)
# print the JSON string representation of the object
print(GetAssetInstance200Response.to_json())

# convert the object into a dict
get_asset_instance200_response_dict = get_asset_instance200_response_instance.to_dict()
# create an instance of GetAssetInstance200Response from a dict
get_asset_instance200_response_from_dict = GetAssetInstance200Response.from_dict(get_asset_instance200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


