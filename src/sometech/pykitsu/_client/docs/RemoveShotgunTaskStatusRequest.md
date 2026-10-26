# RemoveShotgunTaskStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the task status to remove | 

## Example

```python
from sometech.pykitsu._client.models.remove_shotgun_task_status_request import RemoveShotgunTaskStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveShotgunTaskStatusRequest from a JSON string
remove_shotgun_task_status_request_instance = RemoveShotgunTaskStatusRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveShotgunTaskStatusRequest.to_json())

# convert the object into a dict
remove_shotgun_task_status_request_dict = remove_shotgun_task_status_request_instance.to_dict()
# create an instance of RemoveShotgunTaskStatusRequest from a dict
remove_shotgun_task_status_request_from_dict = RemoveShotgunTaskStatusRequest.from_dict(remove_shotgun_task_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


