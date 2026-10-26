# GetStatusOfTheApiServicesForInfluxdb200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_up** | **int** |  | [optional] 
**key_value_store_up** | **int** |  | [optional] 
**event_stream_up** | **int** |  | [optional] 
**job_queue_up** | **int** |  | [optional] 
**indexer_up** | **int** |  | [optional] 
**time** | **float** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_status_of_the_api_services_for_influxdb200_response import GetStatusOfTheApiServicesForInfluxdb200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusOfTheApiServicesForInfluxdb200Response from a JSON string
get_status_of_the_api_services_for_influxdb200_response_instance = GetStatusOfTheApiServicesForInfluxdb200Response.from_json(json)
# print the JSON string representation of the object
print(GetStatusOfTheApiServicesForInfluxdb200Response.to_json())

# convert the object into a dict
get_status_of_the_api_services_for_influxdb200_response_dict = get_status_of_the_api_services_for_influxdb200_response_instance.to_dict()
# create an instance of GetStatusOfTheApiServicesForInfluxdb200Response from a dict
get_status_of_the_api_services_for_influxdb200_response_from_dict = GetStatusOfTheApiServicesForInfluxdb200Response.from_dict(get_status_of_the_api_services_for_influxdb200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


