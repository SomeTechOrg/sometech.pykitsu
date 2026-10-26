# GetBuildJob200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Build job unique identifier | [optional] 
**status** | **str** | Build job status | [optional] 
**created_at** | **datetime** | Build job creation timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_build_job200_response import GetBuildJob200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBuildJob200Response from a JSON string
get_build_job200_response_instance = GetBuildJob200Response.from_json(json)
# print the JSON string representation of the object
print(GetBuildJob200Response.to_json())

# convert the object into a dict
get_build_job200_response_dict = get_build_job200_response_instance.to_dict()
# create an instance of GetBuildJob200Response from a dict
get_build_job200_response_from_dict = GetBuildJob200Response.from_dict(get_build_job200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


