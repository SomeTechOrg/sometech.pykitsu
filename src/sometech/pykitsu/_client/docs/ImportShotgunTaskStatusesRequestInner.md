# ImportShotgunTaskStatusesRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the status | [optional] 
**name** | **str** | Status name | [optional] 
**code** | **str** | Status short code | [optional] 
**bg_color** | **str** | Background color in RGB format | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_task_statuses_request_inner import ImportShotgunTaskStatusesRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunTaskStatusesRequestInner from a JSON string
import_shotgun_task_statuses_request_inner_instance = ImportShotgunTaskStatusesRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunTaskStatusesRequestInner.to_json())

# convert the object into a dict
import_shotgun_task_statuses_request_inner_dict = import_shotgun_task_statuses_request_inner_instance.to_dict()
# create an instance of ImportShotgunTaskStatusesRequestInner from a dict
import_shotgun_task_statuses_request_inner_from_dict = ImportShotgunTaskStatusesRequestInner.from_dict(import_shotgun_task_statuses_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


