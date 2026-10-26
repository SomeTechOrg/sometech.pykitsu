# CreateProjectShotRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**sequence_id** | **UUID** |  | [optional] 
**nb_frames** | **int** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_project_shot_request import CreateProjectShotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectShotRequest from a JSON string
create_project_shot_request_instance = CreateProjectShotRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectShotRequest.to_json())

# convert the object into a dict
create_project_shot_request_dict = create_project_shot_request_instance.to_dict()
# create an instance of CreateProjectShotRequest from a dict
create_project_shot_request_from_dict = CreateProjectShotRequest.from_dict(create_project_shot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


