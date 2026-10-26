# ImportAssetsCsv201ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**entity_type_id** | **UUID** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_assets_csv201_response_inner import ImportAssetsCsv201ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportAssetsCsv201ResponseInner from a JSON string
import_assets_csv201_response_inner_instance = ImportAssetsCsv201ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ImportAssetsCsv201ResponseInner.to_json())

# convert the object into a dict
import_assets_csv201_response_inner_dict = import_assets_csv201_response_inner_instance.to_dict()
# create an instance of ImportAssetsCsv201ResponseInner from a dict
import_assets_csv201_response_inner_from_dict = ImportAssetsCsv201ResponseInner.from_dict(import_assets_csv201_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


