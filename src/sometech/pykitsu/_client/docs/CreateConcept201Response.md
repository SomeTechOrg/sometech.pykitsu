# CreateConcept201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Concept unique identifier | [optional] 
**name** | **str** | Concept name | [optional] 
**description** | **str** | Concept description | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**data** | **object** | Additional concept data | [optional] 
**created_by** | **UUID** | Creator person identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_concept201_response import CreateConcept201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConcept201Response from a JSON string
create_concept201_response_instance = CreateConcept201Response.from_json(json)
# print the JSON string representation of the object
print(CreateConcept201Response.to_json())

# convert the object into a dict
create_concept201_response_dict = create_concept201_response_instance.to_dict()
# create an instance of CreateConcept201Response from a dict
create_concept201_response_from_dict = CreateConcept201Response.from_dict(create_concept201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


