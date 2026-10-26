# ImportKitsuComments200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Comment unique identifier | [optional] 
**text** | **str** | Comment text | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_kitsu_comments200_response_inner import ImportKitsuComments200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportKitsuComments200ResponseInner from a JSON string
import_kitsu_comments200_response_inner_instance = ImportKitsuComments200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ImportKitsuComments200ResponseInner.to_json())

# convert the object into a dict
import_kitsu_comments200_response_inner_dict = import_kitsu_comments200_response_inner_instance.to_dict()
# create an instance of ImportKitsuComments200ResponseInner from a dict
import_kitsu_comments200_response_inner_from_dict = ImportKitsuComments200ResponseInner.from_dict(import_kitsu_comments200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


