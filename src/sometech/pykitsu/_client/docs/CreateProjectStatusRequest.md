# CreateProjectStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**color** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_project_status_request import CreateProjectStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectStatusRequest from a JSON string
create_project_status_request_instance = CreateProjectStatusRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectStatusRequest.to_json())

# convert the object into a dict
create_project_status_request_dict = create_project_status_request_instance.to_dict()
# create an instance of CreateProjectStatusRequest from a dict
create_project_status_request_from_dict = CreateProjectStatusRequest.from_dict(create_project_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


