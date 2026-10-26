# GetOpenProjectsNews200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** | Array of news items | [optional] 
**stats** | **object** | News statistics | [optional] 
**total** | **int** | Total number of news items | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_open_projects_news200_response import GetOpenProjectsNews200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenProjectsNews200Response from a JSON string
get_open_projects_news200_response_instance = GetOpenProjectsNews200Response.from_json(json)
# print the JSON string representation of the object
print(GetOpenProjectsNews200Response.to_json())

# convert the object into a dict
get_open_projects_news200_response_dict = get_open_projects_news200_response_instance.to_dict()
# create an instance of GetOpenProjectsNews200Response from a dict
get_open_projects_news200_response_from_dict = GetOpenProjectsNews200Response.from_dict(get_open_projects_news200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


