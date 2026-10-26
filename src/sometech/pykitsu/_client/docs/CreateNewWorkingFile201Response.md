# CreateNewWorkingFile201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Working file unique identifier | [optional] 
**name** | **str** | Working file name | [optional] 
**path** | **str** | Working file path | [optional] 
**revision** | **int** | Working file revision | [optional] 
**task_id** | **UUID** | Task identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_new_working_file201_response import CreateNewWorkingFile201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewWorkingFile201Response from a JSON string
create_new_working_file201_response_instance = CreateNewWorkingFile201Response.from_json(json)
# print the JSON string representation of the object
print(CreateNewWorkingFile201Response.to_json())

# convert the object into a dict
create_new_working_file201_response_dict = create_new_working_file201_response_instance.to_dict()
# create an instance of CreateNewWorkingFile201Response from a dict
create_new_working_file201_response_from_dict = CreateNewWorkingFile201Response.from_dict(create_new_working_file201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


