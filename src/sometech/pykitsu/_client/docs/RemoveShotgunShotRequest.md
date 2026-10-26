# RemoveShotgunShotRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the shot to remove | 

## Example

```python
from sometech.pykitsu._client.models.remove_shotgun_shot_request import RemoveShotgunShotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveShotgunShotRequest from a JSON string
remove_shotgun_shot_request_instance = RemoveShotgunShotRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveShotgunShotRequest.to_json())

# convert the object into a dict
remove_shotgun_shot_request_dict = remove_shotgun_shot_request_instance.to_dict()
# create an instance of RemoveShotgunShotRequest from a dict
remove_shotgun_shot_request_from_dict = RemoveShotgunShotRequest.from_dict(remove_shotgun_shot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


