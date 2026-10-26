# sometech.pykitsu._client.SearchApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_entities**](SearchApi.md#search_entities) | **POST** /data/search | Search entities


# **search_entities**
> SearchEntities200Response search_entities(search_entities_request)

Search entities

Search across indexes for persons, assets and shots. Use optional filters to limit results to a project and specific indexes. Results are paginated with limit and offset.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.search_entities200_response import SearchEntities200Response
from sometech.pykitsu._client.models.search_entities_request import SearchEntitiesRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.SearchApi(api_client)
    search_entities_request = sometech.pykitsu._client.SearchEntitiesRequest() # SearchEntitiesRequest | 

    try:
        # Search entities
        api_response = await api_instance.search_entities(search_entities_request)
        print("The response of SearchApi->search_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_entities_request** | [**SearchEntitiesRequest**](SearchEntitiesRequest.md)|  | 

### Return type

[**SearchEntities200Response**](SearchEntities200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of entities that contain the query |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

