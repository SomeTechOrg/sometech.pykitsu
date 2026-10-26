# ImportKitsuProjectsRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Kitsu ID of the project | [optional] 
**name** | **str** | Project name | [optional] 
**production_type** | **str** | Production type | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_kitsu_projects_request_inner import ImportKitsuProjectsRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportKitsuProjectsRequestInner from a JSON string
import_kitsu_projects_request_inner_instance = ImportKitsuProjectsRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportKitsuProjectsRequestInner.to_json())

# convert the object into a dict
import_kitsu_projects_request_inner_dict = import_kitsu_projects_request_inner_instance.to_dict()
# create an instance of ImportKitsuProjectsRequestInner from a dict
import_kitsu_projects_request_inner_from_dict = ImportKitsuProjectsRequestInner.from_dict(import_kitsu_projects_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


