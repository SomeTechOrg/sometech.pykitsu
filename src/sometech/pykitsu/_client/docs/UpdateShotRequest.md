# UpdateShotRequest

Data to update on the shot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**nb_frames** | **int** |  | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_shot_request import UpdateShotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShotRequest from a JSON string
update_shot_request_instance = UpdateShotRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateShotRequest.to_json())

# convert the object into a dict
update_shot_request_dict = update_shot_request_instance.to_dict()
# create an instance of UpdateShotRequest from a dict
update_shot_request_from_dict = UpdateShotRequest.from_dict(update_shot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


