# SetProjectAssetsSharedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_shared** | **bool** | Whether to share or unshare the assets | [optional] 
**asset_ids** | **List[UUID]** | Specific asset IDs to update. | [optional] 

## Example

```python
from sometech.pykitsu._client.models.set_project_assets_shared_request import SetProjectAssetsSharedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetProjectAssetsSharedRequest from a JSON string
set_project_assets_shared_request_instance = SetProjectAssetsSharedRequest.from_json(json)
# print the JSON string representation of the object
print(SetProjectAssetsSharedRequest.to_json())

# convert the object into a dict
set_project_assets_shared_request_dict = set_project_assets_shared_request_instance.to_dict()
# create an instance of SetProjectAssetsSharedRequest from a dict
set_project_assets_shared_request_from_dict = SetProjectAssetsSharedRequest.from_dict(set_project_assets_shared_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


