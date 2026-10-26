# GetProjectPreviewFiles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetProjectPreviewFiles200ResponseDataInner]**](GetProjectPreviewFiles200ResponseDataInner.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**is_more** | **bool** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_project_preview_files200_response import GetProjectPreviewFiles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectPreviewFiles200Response from a JSON string
get_project_preview_files200_response_instance = GetProjectPreviewFiles200Response.from_json(json)
# print the JSON string representation of the object
print(GetProjectPreviewFiles200Response.to_json())

# convert the object into a dict
get_project_preview_files200_response_dict = get_project_preview_files200_response_instance.to_dict()
# create an instance of GetProjectPreviewFiles200Response from a dict
get_project_preview_files200_response_from_dict = GetProjectPreviewFiles200Response.from_dict(get_project_preview_files200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


