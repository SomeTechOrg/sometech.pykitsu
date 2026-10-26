# ImportKitsuEntityLinksRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Kitsu ID of the entity link | [optional] 
**entity_in_id** | **UUID** | Source entity ID | [optional] 
**entity_out_id** | **UUID** | Target entity ID | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_kitsu_entity_links_request_inner import ImportKitsuEntityLinksRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportKitsuEntityLinksRequestInner from a JSON string
import_kitsu_entity_links_request_inner_instance = ImportKitsuEntityLinksRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportKitsuEntityLinksRequestInner.to_json())

# convert the object into a dict
import_kitsu_entity_links_request_inner_dict = import_kitsu_entity_links_request_inner_instance.to_dict()
# create an instance of ImportKitsuEntityLinksRequestInner from a dict
import_kitsu_entity_links_request_inner_from_dict = ImportKitsuEntityLinksRequestInner.from_dict(import_kitsu_entity_links_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


