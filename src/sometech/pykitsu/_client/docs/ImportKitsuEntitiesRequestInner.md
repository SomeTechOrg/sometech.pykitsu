# ImportKitsuEntitiesRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Kitsu ID of the entity | [optional] 
**name** | **str** | Entity name | [optional] 
**project_id** | **UUID** | Project ID | [optional] 
**entity_type_id** | **UUID** | Entity type ID | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_kitsu_entities_request_inner import ImportKitsuEntitiesRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportKitsuEntitiesRequestInner from a JSON string
import_kitsu_entities_request_inner_instance = ImportKitsuEntitiesRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportKitsuEntitiesRequestInner.to_json())

# convert the object into a dict
import_kitsu_entities_request_inner_dict = import_kitsu_entities_request_inner_instance.to_dict()
# create an instance of ImportKitsuEntitiesRequestInner from a dict
import_kitsu_entities_request_inner_from_dict = ImportKitsuEntitiesRequestInner.from_dict(import_kitsu_entities_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


