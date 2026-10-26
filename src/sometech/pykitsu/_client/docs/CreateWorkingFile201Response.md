# CreateWorkingFile201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**task_id** | **UUID** |  | [optional] 
**entity_id** | **UUID** |  | [optional] 
**revision** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_working_file201_response import CreateWorkingFile201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkingFile201Response from a JSON string
create_working_file201_response_instance = CreateWorkingFile201Response.from_json(json)
# print the JSON string representation of the object
print(CreateWorkingFile201Response.to_json())

# convert the object into a dict
create_working_file201_response_dict = create_working_file201_response_instance.to_dict()
# create an instance of CreateWorkingFile201Response from a dict
create_working_file201_response_from_dict = CreateWorkingFile201Response.from_dict(create_working_file201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


