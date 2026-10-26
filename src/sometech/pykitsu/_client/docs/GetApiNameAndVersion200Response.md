# GetApiNameAndVersion200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_api_name_and_version200_response import GetApiNameAndVersion200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiNameAndVersion200Response from a JSON string
get_api_name_and_version200_response_instance = GetApiNameAndVersion200Response.from_json(json)
# print the JSON string representation of the object
print(GetApiNameAndVersion200Response.to_json())

# convert the object into a dict
get_api_name_and_version200_response_dict = get_api_name_and_version200_response_instance.to_dict()
# create an instance of GetApiNameAndVersion200Response from a dict
get_api_name_and_version200_response_from_dict = GetApiNameAndVersion200Response.from_dict(get_api_name_and_version200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


