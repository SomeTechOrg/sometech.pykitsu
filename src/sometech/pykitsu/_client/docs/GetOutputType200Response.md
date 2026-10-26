# GetOutputType200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_output_type200_response import GetOutputType200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOutputType200Response from a JSON string
get_output_type200_response_instance = GetOutputType200Response.from_json(json)
# print the JSON string representation of the object
print(GetOutputType200Response.to_json())

# convert the object into a dict
get_output_type200_response_dict = get_output_type200_response_instance.to_dict()
# create an instance of GetOutputType200Response from a dict
get_output_type200_response_from_dict = GetOutputType200Response.from_dict(get_output_type200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


