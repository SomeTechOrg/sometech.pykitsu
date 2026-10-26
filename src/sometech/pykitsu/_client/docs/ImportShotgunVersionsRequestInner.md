# ImportShotgunVersionsRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the version | [optional] 
**code** | **str** | Version code | [optional] 
**description** | **str** | Version description | [optional] 
**sg_task** | [**ImportShotgunVersionsRequestInnerSgTask**](ImportShotgunVersionsRequestInnerSgTask.md) |  | [optional] 
**user** | [**ImportShotgunVersionsRequestInnerUser**](ImportShotgunVersionsRequestInnerUser.md) |  | [optional] 
**sg_uploaded_movie** | [**ImportShotgunVersionsRequestInnerSgUploadedMovie**](ImportShotgunVersionsRequestInnerSgUploadedMovie.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_versions_request_inner import ImportShotgunVersionsRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunVersionsRequestInner from a JSON string
import_shotgun_versions_request_inner_instance = ImportShotgunVersionsRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunVersionsRequestInner.to_json())

# convert the object into a dict
import_shotgun_versions_request_inner_dict = import_shotgun_versions_request_inner_instance.to_dict()
# create an instance of ImportShotgunVersionsRequestInner from a dict
import_shotgun_versions_request_inner_from_dict = ImportShotgunVersionsRequestInner.from_dict(import_shotgun_versions_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


