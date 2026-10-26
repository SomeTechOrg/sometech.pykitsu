# GetConcept200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Concept unique identifier | [optional] 
**name** | **str** | Concept name | [optional] 
**description** | **str** | Concept description | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_concept200_response import GetConcept200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetConcept200Response from a JSON string
get_concept200_response_instance = GetConcept200Response.from_json(json)
# print the JSON string representation of the object
print(GetConcept200Response.to_json())

# convert the object into a dict
get_concept200_response_dict = get_concept200_response_instance.to_dict()
# create an instance of GetConcept200Response from a dict
get_concept200_response_from_dict = GetConcept200Response.from_dict(get_concept200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


