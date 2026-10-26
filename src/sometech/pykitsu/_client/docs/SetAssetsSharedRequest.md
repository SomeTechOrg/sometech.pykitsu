# SetAssetsSharedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_ids** | **List[UUID]** | List of asset IDs to update | 
**is_shared** | **bool** | Whether to share or unshare the assets | [optional] 

## Example

```python
from sometech.pykitsu._client.models.set_assets_shared_request import SetAssetsSharedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetAssetsSharedRequest from a JSON string
set_assets_shared_request_instance = SetAssetsSharedRequest.from_json(json)
# print the JSON string representation of the object
print(SetAssetsSharedRequest.to_json())

# convert the object into a dict
set_assets_shared_request_dict = set_assets_shared_request_instance.to_dict()
# create an instance of SetAssetsSharedRequest from a dict
set_assets_shared_request_from_dict = SetAssetsSharedRequest.from_dict(set_assets_shared_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


