# SearchEntitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Search query string (minimum 3 characters) | 
**project_id** | **UUID** | Filter search results by project ID | [optional] 
**limit** | **int** | Maximum number of results per index | [optional] [default to 3]
**offset** | **int** | Number of results to skip | [optional] [default to 0]
**index_names** | **List[str]** | List of index names to search in | [optional] [default to ["assets","shots","persons"]]

## Example

```python
from sometech.pykitsu._client.models.search_entities_request import SearchEntitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchEntitiesRequest from a JSON string
search_entities_request_instance = SearchEntitiesRequest.from_json(json)
# print the JSON string representation of the object
print(SearchEntitiesRequest.to_json())

# convert the object into a dict
search_entities_request_dict = search_entities_request_instance.to_dict()
# create an instance of SearchEntitiesRequest from a dict
search_entities_request_from_dict = SearchEntitiesRequest.from_dict(search_entities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


