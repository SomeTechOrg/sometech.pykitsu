# CreateConceptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Concept name | 
**description** | **str** | Concept description | [optional] 
**data** | **object** | Additional concept data | [optional] 
**entity_concept_links** | **List[UUID]** | List of entity concept link identifiers | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_concept_request import CreateConceptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConceptRequest from a JSON string
create_concept_request_instance = CreateConceptRequest.from_json(json)
# print the JSON string representation of the object
print(CreateConceptRequest.to_json())

# convert the object into a dict
create_concept_request_dict = create_concept_request_instance.to_dict()
# create an instance of CreateConceptRequest from a dict
create_concept_request_from_dict = CreateConceptRequest.from_dict(create_concept_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


