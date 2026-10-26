# ImportShotgunSteps200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Task type unique identifier | [optional] 
**name** | **str** | Task type name | [optional] 
**short_name** | **str** | Task type short name | [optional] 
**color** | **str** | Task type color in hex format | [optional] 
**for_entity** | **str** | Entity type | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_steps200_response_inner import ImportShotgunSteps200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunSteps200ResponseInner from a JSON string
import_shotgun_steps200_response_inner_instance = ImportShotgunSteps200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunSteps200ResponseInner.to_json())

# convert the object into a dict
import_shotgun_steps200_response_inner_dict = import_shotgun_steps200_response_inner_instance.to_dict()
# create an instance of ImportShotgunSteps200ResponseInner from a dict
import_shotgun_steps200_response_inner_from_dict = ImportShotgunSteps200ResponseInner.from_dict(import_shotgun_steps200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


