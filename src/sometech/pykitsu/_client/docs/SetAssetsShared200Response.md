# SetAssetsShared200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_count** | **int** | Number of assets updated | [optional] 
**asset_ids** | **List[UUID]** | List of updated asset IDs | [optional] 

## Example

```python
from sometech.pykitsu._client.models.set_assets_shared200_response import SetAssetsShared200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetAssetsShared200Response from a JSON string
set_assets_shared200_response_instance = SetAssetsShared200Response.from_json(json)
# print the JSON string representation of the object
print(SetAssetsShared200Response.to_json())

# convert the object into a dict
set_assets_shared200_response_dict = set_assets_shared200_response_instance.to_dict()
# create an instance of SetAssetsShared200Response from a dict
set_assets_shared200_response_from_dict = SetAssetsShared200Response.from_dict(set_assets_shared200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


