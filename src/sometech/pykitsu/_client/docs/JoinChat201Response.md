# JoinChat201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Chat unique identifier | [optional] 
**entity_id** | **UUID** | Entity identifier | [optional] 
**entity_type** | **str** | Entity type | [optional] 
**participants** | **List[UUID]** | List of participant person identifiers | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.join_chat201_response import JoinChat201Response

# TODO update the JSON string below
json = "{}"
# create an instance of JoinChat201Response from a JSON string
join_chat201_response_instance = JoinChat201Response.from_json(json)
# print the JSON string representation of the object
print(JoinChat201Response.to_json())

# convert the object into a dict
join_chat201_response_dict = join_chat201_response_instance.to_dict()
# create an instance of JoinChat201Response from a dict
join_chat201_response_from_dict = JoinChat201Response.from_dict(join_chat201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


