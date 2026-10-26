# ImportKitsuCommentsRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Kitsu ID of the comment | [optional] 
**object_id** | **UUID** | Task ID the comment is linked to | [optional] 
**text** | **str** | Comment text | [optional] 
**person_id** | **UUID** | Person who created the comment | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_kitsu_comments_request_inner import ImportKitsuCommentsRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportKitsuCommentsRequestInner from a JSON string
import_kitsu_comments_request_inner_instance = ImportKitsuCommentsRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportKitsuCommentsRequestInner.to_json())

# convert the object into a dict
import_kitsu_comments_request_inner_dict = import_kitsu_comments_request_inner_instance.to_dict()
# create an instance of ImportKitsuCommentsRequestInner from a dict
import_kitsu_comments_request_inner_from_dict = ImportKitsuCommentsRequestInner.from_dict(import_kitsu_comments_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


