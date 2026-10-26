# ImportShotgunAssetsRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the asset | [optional] 
**code** | **str** | Asset code | [optional] 
**description** | **str** | Asset description | [optional] 
**sg_asset_type** | **str** | Asset type name | [optional] 
**project** | [**ImportShotgunAssetsRequestInnerProject**](ImportShotgunAssetsRequestInnerProject.md) |  | [optional] 
**parents** | [**List[ImportShotgunAssetsRequestInnerParentsInner]**](ImportShotgunAssetsRequestInnerParentsInner.md) | Parent assets | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_assets_request_inner import ImportShotgunAssetsRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunAssetsRequestInner from a JSON string
import_shotgun_assets_request_inner_instance = ImportShotgunAssetsRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunAssetsRequestInner.to_json())

# convert the object into a dict
import_shotgun_assets_request_inner_dict = import_shotgun_assets_request_inner_instance.to_dict()
# create an instance of ImportShotgunAssetsRequestInner from a dict
import_shotgun_assets_request_inner_from_dict = ImportShotgunAssetsRequestInner.from_dict(import_shotgun_assets_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


