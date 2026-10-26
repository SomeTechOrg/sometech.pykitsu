# GetStatusOfTheApiServices200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**database_up** | **bool** |  | [optional] 
**key_value_store_up** | **bool** |  | [optional] 
**event_stream_up** | **bool** |  | [optional] 
**job_queue_up** | **bool** |  | [optional] 
**indexer_up** | **bool** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_status_of_the_api_services200_response import GetStatusOfTheApiServices200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusOfTheApiServices200Response from a JSON string
get_status_of_the_api_services200_response_instance = GetStatusOfTheApiServices200Response.from_json(json)
# print the JSON string representation of the object
print(GetStatusOfTheApiServices200Response.to_json())

# convert the object into a dict
get_status_of_the_api_services200_response_dict = get_status_of_the_api_services200_response_instance.to_dict()
# create an instance of GetStatusOfTheApiServices200Response from a dict
get_status_of_the_api_services200_response_from_dict = GetStatusOfTheApiServices200Response.from_dict(get_status_of_the_api_services200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


