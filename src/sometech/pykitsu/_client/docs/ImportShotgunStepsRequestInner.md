# ImportShotgunStepsRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the step | [optional] 
**code** | **str** | Step code (used to extract department) | [optional] 
**short_name** | **str** | Step short name | [optional] 
**color** | **str** | Color in RGB format | [optional] 
**entity_type** | **str** | Entity type this step applies to | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_steps_request_inner import ImportShotgunStepsRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunStepsRequestInner from a JSON string
import_shotgun_steps_request_inner_instance = ImportShotgunStepsRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunStepsRequestInner.to_json())

# convert the object into a dict
import_shotgun_steps_request_inner_dict = import_shotgun_steps_request_inner_instance.to_dict()
# create an instance of ImportShotgunStepsRequestInner from a dict
import_shotgun_steps_request_inner_from_dict = ImportShotgunStepsRequestInner.from_dict(import_shotgun_steps_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


