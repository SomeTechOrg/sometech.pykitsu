# ImportShotgunTaskStatuses200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Task status unique identifier | [optional] 
**name** | **str** | Status name | [optional] 
**short_name** | **str** | Status short code | [optional] 
**color** | **str** | Status color in hex format | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_task_statuses200_response_inner import ImportShotgunTaskStatuses200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunTaskStatuses200ResponseInner from a JSON string
import_shotgun_task_statuses200_response_inner_instance = ImportShotgunTaskStatuses200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunTaskStatuses200ResponseInner.to_json())

# convert the object into a dict
import_shotgun_task_statuses200_response_inner_dict = import_shotgun_task_statuses200_response_inner_instance.to_dict()
# create an instance of ImportShotgunTaskStatuses200ResponseInner from a dict
import_shotgun_task_statuses200_response_inner_from_dict = ImportShotgunTaskStatuses200ResponseInner.from_dict(import_shotgun_task_statuses200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


