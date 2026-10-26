# sometech.pykitsu._client.IndexApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_a_test_event**](IndexApi.md#generate_a_test_event) | **GET** /status/test-event | Generate a test event
[**get_api_name_and_version**](IndexApi.md#get_api_name_and_version) | **GET** / | Get API name and version
[**get_resource_usage_stats**](IndexApi.md#get_resource_usage_stats) | **GET** /status/resources | Get resource usage stats
[**get_status_of_the_api_services**](IndexApi.md#get_status_of_the_api_services) | **GET** /status | Get status of the API services
[**get_status_of_the_api_services_as_text**](IndexApi.md#get_status_of_the_api_services_as_text) | **GET** /status.txt | Get status of the API services as text
[**get_status_of_the_api_services_for_influxdb**](IndexApi.md#get_status_of_the_api_services_for_influxdb) | **GET** /status/influx | Get status of the API services for InfluxDB
[**get_the_configuration_of_the_kitsu_instance**](IndexApi.md#get_the_configuration_of_the_kitsu_instance) | **GET** /config | Get the configuration of the Kitsu instance
[**get_usage_stats**](IndexApi.md#get_usage_stats) | **GET** /stats | Get usage stats


# **generate_a_test_event**
> GenerateATestEvent200Response generate_a_test_event()

Generate a test event

Generate a `main:test` event to test the event stream with the Python client or similar.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.generate_a_test_event200_response import GenerateATestEvent200Response
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
    api_instance = sometech.pykitsu._client.IndexApi(api_client)

    try:
        # Generate a test event
        api_response = await api_instance.generate_a_test_event()
        print("The response of IndexApi->generate_a_test_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->generate_a_test_event: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GenerateATestEvent200Response**](GenerateATestEvent200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success flag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_name_and_version**
> GetApiNameAndVersion200Response get_api_name_and_version()

Get API name and version

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_api_name_and_version200_response import GetApiNameAndVersion200Response
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
    api_instance = sometech.pykitsu._client.IndexApi(api_client)

    try:
        # Get API name and version
        api_response = await api_instance.get_api_name_and_version()
        print("The response of IndexApi->get_api_name_and_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->get_api_name_and_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetApiNameAndVersion200Response**](GetApiNameAndVersion200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API name and version |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_usage_stats**
> GetResourceUsageStats200Response get_resource_usage_stats()

Get resource usage stats

Get CPU usage for each core, memory repartition and number of jobs in the job queue.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_resource_usage_stats200_response import GetResourceUsageStats200Response
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
    api_instance = sometech.pykitsu._client.IndexApi(api_client)

    try:
        # Get resource usage stats
        api_response = await api_instance.get_resource_usage_stats()
        print("The response of IndexApi->get_resource_usage_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->get_resource_usage_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetResourceUsageStats200Response**](GetResourceUsageStats200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CPU, memory and jobs stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_of_the_api_services**
> GetStatusOfTheApiServices200Response get_status_of_the_api_services()

Get status of the API services

 

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_status_of_the_api_services200_response import GetStatusOfTheApiServices200Response
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
    api_instance = sometech.pykitsu._client.IndexApi(api_client)

    try:
        # Get status of the API services
        api_response = await api_instance.get_status_of_the_api_services()
        print("The response of IndexApi->get_status_of_the_api_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->get_status_of_the_api_services: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetStatusOfTheApiServices200Response**](GetStatusOfTheApiServices200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of the API services |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_of_the_api_services_as_text**
> str get_status_of_the_api_services_as_text()

Get status of the API services as text

Get status of the database, key value store, event stream, job queue, the indexer as a text.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
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
    api_instance = sometech.pykitsu._client.IndexApi(api_client)

    try:
        # Get status of the API services as text
        api_response = await api_instance.get_status_of_the_api_services_as_text()
        print("The response of IndexApi->get_status_of_the_api_services_as_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->get_status_of_the_api_services_as_text: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API name, version and status as txt |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_of_the_api_services_for_influxdb**
> GetStatusOfTheApiServicesForInfluxdb200Response get_status_of_the_api_services_for_influxdb()

Get status of the API services for InfluxDB

Get status of the database, key value store, event stream, job queue, indexer as a JSON object.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_status_of_the_api_services_for_influxdb200_response import GetStatusOfTheApiServicesForInfluxdb200Response
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
    api_instance = sometech.pykitsu._client.IndexApi(api_client)

    try:
        # Get status of the API services for InfluxDB
        api_response = await api_instance.get_status_of_the_api_services_for_influxdb()
        print("The response of IndexApi->get_status_of_the_api_services_for_influxdb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->get_status_of_the_api_services_for_influxdb: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetStatusOfTheApiServicesForInfluxdb200Response**](GetStatusOfTheApiServicesForInfluxdb200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of database, key value, event stream, job queue and time |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_the_configuration_of_the_kitsu_instance**
> GetTheConfigurationOfTheKitsuInstance200Response get_the_configuration_of_the_kitsu_instance()

Get the configuration of the Kitsu instance

The configuration includes self-hosted status, Crisp token, indexer configuration, SAML status, and dark theme status.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_the_configuration_of_the_kitsu_instance200_response import GetTheConfigurationOfTheKitsuInstance200Response
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
    api_instance = sometech.pykitsu._client.IndexApi(api_client)

    try:
        # Get the configuration of the Kitsu instance
        api_response = await api_instance.get_the_configuration_of_the_kitsu_instance()
        print("The response of IndexApi->get_the_configuration_of_the_kitsu_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->get_the_configuration_of_the_kitsu_instance: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTheConfigurationOfTheKitsuInstance200Response**](GetTheConfigurationOfTheKitsuInstance200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_stats**
> GetUsageStats200Response get_usage_stats()

Get usage stats

Get the amount of projects, assets, shots, tasks, and persons.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_usage_stats200_response import GetUsageStats200Response
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
    api_instance = sometech.pykitsu._client.IndexApi(api_client)

    try:
        # Get usage stats
        api_response = await api_instance.get_usage_stats()
        print("The response of IndexApi->get_usage_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexApi->get_usage_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetUsageStats200Response**](GetUsageStats200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Main stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

