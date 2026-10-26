# sometech.pykitsu._client.EntitiesApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entity_news**](EntitiesApi.md#get_entity_news) | **GET** /data/entities/{entity_id}/news | Get entity news
[**get_entity_preview_files**](EntitiesApi.md#get_entity_preview_files) | **GET** /data/entities/{entity_id}/preview-files | Get entity preview files
[**get_entity_time_spent**](EntitiesApi.md#get_entity_time_spent) | **GET** /data/entities/{entity_id}/time-spents | Get entity time spent
[**get_linked_entities**](EntitiesApi.md#get_linked_entities) | **GET** /data/entities/{entity_id}/entities-linked/with-tasks | Get linked entities


# **get_entity_news**
> List[News] get_entity_news(entity_id)

Get entity news

Retrieve all news entries that are linked to a specific entity.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.news import News
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
    api_instance = sometech.pykitsu._client.EntitiesApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the entity

    try:
        # Get entity news
        api_response = await api_instance.get_entity_news(entity_id)
        print("The response of EntitiesApi->get_entity_news:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_entity_news: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Unique identifier of the entity | 

### Return type

[**List[News]**](News.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of entity news successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_preview_files**
> List[GetEntityPreviewFiles200ResponseInner] get_entity_preview_files(entity_id)

Get entity preview files

Retrieve all preview files that are linked to a specific entity. This includes images, videos, and other preview media associated with the entity.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_entity_preview_files200_response_inner import GetEntityPreviewFiles200ResponseInner
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
    api_instance = sometech.pykitsu._client.EntitiesApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the entity

    try:
        # Get entity preview files
        api_response = await api_instance.get_entity_preview_files(entity_id)
        print("The response of EntitiesApi->get_entity_preview_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_entity_preview_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Unique identifier of the entity | 

### Return type

[**List[GetEntityPreviewFiles200ResponseInner]**](GetEntityPreviewFiles200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of entity preview files successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_time_spent**
> List[GetEntityTimeSpent200ResponseInner] get_entity_time_spent(entity_id)

Get entity time spent

Retrieve all time spent entries that are linked to a specific entity.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_entity_time_spent200_response_inner import GetEntityTimeSpent200ResponseInner
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
    api_instance = sometech.pykitsu._client.EntitiesApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the entity

    try:
        # Get entity time spent
        api_response = await api_instance.get_entity_time_spent(entity_id)
        print("The response of EntitiesApi->get_entity_time_spent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_entity_time_spent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Unique identifier of the entity | 

### Return type

[**List[GetEntityTimeSpent200ResponseInner]**](GetEntityTimeSpent200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of entity time spent entries successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_entities**
> List[GetLinkedEntities200ResponseInner] get_linked_entities(entity_id)

Get linked entities

Retrieve all entities that are linked to a specific entity along with their associated tasks. This includes related entities, dependencies, and hierarchical relationships.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_linked_entities200_response_inner import GetLinkedEntities200ResponseInner
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
    api_instance = sometech.pykitsu._client.EntitiesApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the entity

    try:
        # Get linked entities
        api_response = await api_instance.get_linked_entities(entity_id)
        print("The response of EntitiesApi->get_linked_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_linked_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Unique identifier of the entity | 

### Return type

[**List[GetLinkedEntities200ResponseInner]**](GetLinkedEntities200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of linked entities successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

