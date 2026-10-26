# UpdateProjectStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_project_status_request import UpdateProjectStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectStatusRequest from a JSON string
update_project_status_request_instance = UpdateProjectStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProjectStatusRequest.to_json())

# convert the object into a dict
update_project_status_request_dict = update_project_status_request_instance.to_dict()
# create an instance of UpdateProjectStatusRequest from a dict
update_project_status_request_from_dict = UpdateProjectStatusRequest.from_dict(update_project_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


