# CreateDepartmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**color** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_department_request import CreateDepartmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDepartmentRequest from a JSON string
create_department_request_instance = CreateDepartmentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDepartmentRequest.to_json())

# convert the object into a dict
create_department_request_dict = create_department_request_instance.to_dict()
# create an instance of CreateDepartmentRequest from a dict
create_department_request_from_dict = CreateDepartmentRequest.from_dict(create_department_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


