# SetMainPreview200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Entity unique identifier | [optional] 
**preview_file_id** | **UUID** | Preview file unique identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.set_main_preview200_response import SetMainPreview200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetMainPreview200Response from a JSON string
set_main_preview200_response_instance = SetMainPreview200Response.from_json(json)
# print the JSON string representation of the object
print(SetMainPreview200Response.to_json())

# convert the object into a dict
set_main_preview200_response_dict = set_main_preview200_response_instance.to_dict()
# create an instance of SetMainPreview200Response from a dict
set_main_preview200_response_from_dict = SetMainPreview200Response.from_dict(set_main_preview200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


