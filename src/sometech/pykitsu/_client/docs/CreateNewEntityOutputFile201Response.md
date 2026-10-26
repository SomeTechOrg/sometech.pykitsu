# CreateNewEntityOutputFile201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Output file unique identifier | [optional] 
**name** | **str** | Output file name | [optional] 
**path** | **str** | Output file path | [optional] 
**revision** | **int** | Output file revision | [optional] 
**entity_id** | **UUID** | Entity identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_new_entity_output_file201_response import CreateNewEntityOutputFile201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewEntityOutputFile201Response from a JSON string
create_new_entity_output_file201_response_instance = CreateNewEntityOutputFile201Response.from_json(json)
# print the JSON string representation of the object
print(CreateNewEntityOutputFile201Response.to_json())

# convert the object into a dict
create_new_entity_output_file201_response_dict = create_new_entity_output_file201_response_instance.to_dict()
# create an instance of CreateNewEntityOutputFile201Response from a dict
create_new_entity_output_file201_response_from_dict = CreateNewEntityOutputFile201Response.from_dict(create_new_entity_output_file201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


