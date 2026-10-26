# ImportShotgunProjectsRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the project | [optional] 
**name** | **str** | Project name | [optional] 
**sg_status** | **str** | Project status | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_projects_request_inner import ImportShotgunProjectsRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunProjectsRequestInner from a JSON string
import_shotgun_projects_request_inner_instance = ImportShotgunProjectsRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunProjectsRequestInner.to_json())

# convert the object into a dict
import_shotgun_projects_request_inner_dict = import_shotgun_projects_request_inner_instance.to_dict()
# create an instance of ImportShotgunProjectsRequestInner from a dict
import_shotgun_projects_request_inner_from_dict = ImportShotgunProjectsRequestInner.from_dict(import_shotgun_projects_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


