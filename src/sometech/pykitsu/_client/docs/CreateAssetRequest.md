# CreateAssetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Asset name | 
**description** | **str** | Asset description | 
**data** | **object** | Asset metadata and custom data | 
**is_shared** | **bool** | Whether the asset is shared across projects | 
**source_id** | **UUID** | Source asset identifier for duplication | 
**episode_id** | **UUID** | Episode identifier for episodic assets | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_asset_request import CreateAssetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetRequest from a JSON string
create_asset_request_instance = CreateAssetRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAssetRequest.to_json())

# convert the object into a dict
create_asset_request_dict = create_asset_request_instance.to_dict()
# create an instance of CreateAssetRequest from a dict
create_asset_request_from_dict = CreateAssetRequest.from_dict(create_asset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


