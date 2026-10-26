# CreateTaskComment201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Comment unique identifier | [optional] 
**task_id** | **UUID** | Task identifier | [optional] 
**person_id** | **UUID** | Person identifier | [optional] 
**comment** | **str** | Comment text content | [optional] 
**task_status_id** | **UUID** | Task status identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_task_comment201_response import CreateTaskComment201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaskComment201Response from a JSON string
create_task_comment201_response_instance = CreateTaskComment201Response.from_json(json)
# print the JSON string representation of the object
print(CreateTaskComment201Response.to_json())

# convert the object into a dict
create_task_comment201_response_dict = create_task_comment201_response_instance.to_dict()
# create an instance of CreateTaskComment201Response from a dict
create_task_comment201_response_from_dict = CreateTaskComment201Response.from_dict(create_task_comment201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


