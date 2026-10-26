# GetProjectLatestNews200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetProjectLatestNews200ResponseDataInner]**](GetProjectLatestNews200ResponseDataInner.md) |  | [optional] 
**stats** | [**GetProjectLatestNews200ResponseStats**](GetProjectLatestNews200ResponseStats.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_project_latest_news200_response import GetProjectLatestNews200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectLatestNews200Response from a JSON string
get_project_latest_news200_response_instance = GetProjectLatestNews200Response.from_json(json)
# print the JSON string representation of the object
print(GetProjectLatestNews200Response.to_json())

# convert the object into a dict
get_project_latest_news200_response_dict = get_project_latest_news200_response_instance.to_dict()
# create an instance of GetProjectLatestNews200Response from a dict
get_project_latest_news200_response_from_dict = GetProjectLatestNews200Response.from_dict(get_project_latest_news200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


