# CreateProjectStatus201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_project_status201_response import CreateProjectStatus201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectStatus201Response from a JSON string
create_project_status201_response_instance = CreateProjectStatus201Response.from_json(json)
# print the JSON string representation of the object
print(CreateProjectStatus201Response.to_json())

# convert the object into a dict
create_project_status201_response_dict = create_project_status201_response_instance.to_dict()
# create an instance of CreateProjectStatus201Response from a dict
create_project_status201_response_from_dict = CreateProjectStatus201Response.from_dict(create_project_status201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


