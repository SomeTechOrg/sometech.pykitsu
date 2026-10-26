# sometech.pykitsu._client.EventsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events_get_data_events_last**](EventsApi.md#get_events_get_data_events_last) | **GET** /data/events/last | Get events
[**get_login_logs**](EventsApi.md#get_login_logs) | **GET** /data/events/login-logs/last | Get login logs


# **get_events_get_data_events_last**
> List[GetEventsGetDataEventsLast200ResponseInner] get_events_get_data_events_last(after=after, before=before, only_files=only_files, cursor_event_id=cursor_event_id, limit=limit, project_id=project_id, name=name)

Get events

Retrieve last events with filtering support. Filters can be specified in the query string to narrow down results by date range, project, or other criteria.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_events_get_data_events_last200_response_inner import GetEventsGetDataEventsLast200ResponseInner
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
    api_instance = sometech.pykitsu._client.EventsApi(api_client)
    after = '2022-07-12' # date | Filter events after this date (optional)
    before = '2022-07-12' # date | Filter events before this date (optional)
    only_files = False # bool | Return only file-related events (optional) (default to False)
    cursor_event_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | ID of the last event from previous page for cursor-based pagination (optional)
    limit = 100 # int | Maximum number of events to return (optional) (default to 100)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter events by specific project (optional)
    name = 'user_login' # str | Filter events by event name (optional)

    try:
        # Get events
        api_response = await api_instance.get_events_get_data_events_last(after=after, before=before, only_files=only_files, cursor_event_id=cursor_event_id, limit=limit, project_id=project_id, name=name)
        print("The response of EventsApi->get_events_get_data_events_last:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_events_get_data_events_last: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **date**| Filter events after this date | [optional] 
 **before** | **date**| Filter events before this date | [optional] 
 **only_files** | **bool**| Return only file-related events | [optional] [default to False]
 **cursor_event_id** | **UUID**| ID of the last event from previous page for cursor-based pagination | [optional] 
 **limit** | **int**| Maximum number of events to return | [optional] [default to 100]
 **project_id** | **UUID**| Filter events by specific project | [optional] 
 **name** | **str**| Filter events by event name | [optional] 

### Return type

[**List[GetEventsGetDataEventsLast200ResponseInner]**](GetEventsGetDataEventsLast200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of events successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_logs**
> List[LoginLog] get_login_logs(after=after, before=before, cursor_login_log_id=cursor_login_log_id, limit=limit)

Get login logs

Retrieve all login logs with filtering support. Filters can be specified in the query string to narrow down results by date range and limit.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.login_log import LoginLog
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
    api_instance = sometech.pykitsu._client.EventsApi(api_client)
    after = '2022-07-12' # date | Filter logs after this date (optional)
    before = '2022-07-12' # date | Filter logs before this date (optional)
    cursor_login_log_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | ID of the last login log from previous page for cursor-based pagination (optional)
    limit = 100 # int | Maximum number of login logs to return (optional) (default to 100)

    try:
        # Get login logs
        api_response = await api_instance.get_login_logs(after=after, before=before, cursor_login_log_id=cursor_login_log_id, limit=limit)
        print("The response of EventsApi->get_login_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_login_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **date**| Filter logs after this date | [optional] 
 **before** | **date**| Filter logs before this date | [optional] 
 **cursor_login_log_id** | **UUID**| ID of the last login log from previous page for cursor-based pagination | [optional] 
 **limit** | **int**| Maximum number of login logs to return | [optional] [default to 100]

### Return type

[**List[LoginLog]**](LoginLog.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of login logs successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

