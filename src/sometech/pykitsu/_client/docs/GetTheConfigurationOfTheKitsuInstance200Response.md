# GetTheConfigurationOfTheKitsuInstance200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_self_hosted** | **bool** |  | [optional] 
**crisp_token** | **str** |  | [optional] 
**dark_theme_by_default** | **bool** |  | [optional] 
**indexer_configured** | **bool** |  | [optional] 
**saml_enabled** | **bool** |  | [optional] 
**saml_idp_name** | **str** |  | [optional] 
**default_locale** | **str** |  | [optional] 
**default_timezone** | **str** |  | [optional] 
**sentry** | [**GetTheConfigurationOfTheKitsuInstance200ResponseSentry**](GetTheConfigurationOfTheKitsuInstance200ResponseSentry.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_the_configuration_of_the_kitsu_instance200_response import GetTheConfigurationOfTheKitsuInstance200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTheConfigurationOfTheKitsuInstance200Response from a JSON string
get_the_configuration_of_the_kitsu_instance200_response_instance = GetTheConfigurationOfTheKitsuInstance200Response.from_json(json)
# print the JSON string representation of the object
print(GetTheConfigurationOfTheKitsuInstance200Response.to_json())

# convert the object into a dict
get_the_configuration_of_the_kitsu_instance200_response_dict = get_the_configuration_of_the_kitsu_instance200_response_instance.to_dict()
# create an instance of GetTheConfigurationOfTheKitsuInstance200Response from a dict
get_the_configuration_of_the_kitsu_instance200_response_from_dict = GetTheConfigurationOfTheKitsuInstance200Response.from_dict(get_the_configuration_of_the_kitsu_instance200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


