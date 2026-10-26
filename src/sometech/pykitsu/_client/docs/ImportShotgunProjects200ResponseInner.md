# ImportShotgunProjects200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Project unique identifier | [optional] 
**name** | **str** | Project name | [optional] 
**data** | **object** | Custom project data | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_projects200_response_inner import ImportShotgunProjects200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunProjects200ResponseInner from a JSON string
import_shotgun_projects200_response_inner_instance = ImportShotgunProjects200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunProjects200ResponseInner.to_json())

# convert the object into a dict
import_shotgun_projects200_response_inner_dict = import_shotgun_projects200_response_inner_instance.to_dict()
# create an instance of ImportShotgunProjects200ResponseInner from a dict
import_shotgun_projects200_response_inner_from_dict = ImportShotgunProjects200ResponseInner.from_dict(import_shotgun_projects200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


