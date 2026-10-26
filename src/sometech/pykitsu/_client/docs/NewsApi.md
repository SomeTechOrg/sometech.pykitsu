# sometech.pykitsu._client.NewsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_news_item**](NewsApi.md#get_news_item) | **GET** /data/projects/{project_id}/news/{news_id} | Get news item
[**get_open_projects_news**](NewsApi.md#get_open_projects_news) | **GET** /data/projects/news | Get open projects news
[**get_project_latest_news**](NewsApi.md#get_project_latest_news) | **GET** /data/projects/{project_id}/news | Get project latest news


# **get_news_item**
> GetNewsItem200Response get_news_item(project_id, news_id)

Get news item

Retrieves detailed information about a specific news item from a givenproject.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_news_item200_response import GetNewsItem200Response
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
    api_instance = sometech.pykitsu._client.NewsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    news_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the news item

    try:
        # Get news item
        api_response = await api_instance.get_news_item(project_id, news_id)
        print("The response of NewsApi->get_news_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewsApi->get_news_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **news_id** | **UUID**| Unique identifier of the news item | 

### Return type

[**GetNewsItem200Response**](GetNewsItem200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | News item successfully retrieved |  -  |
**404** | News item or project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_projects_news**
> GetOpenProjectsNews200Response get_open_projects_news(project_id=project_id, before=before, after=after, page=page, limit=limit, person_id=person_id, task_type_id=task_type_id, task_status_id=task_status_id, episode_id=episode_id, only_preview=only_preview)

Get open projects news

Returns the latest news and activity feed from all projects the user has access to.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_open_projects_news200_response import GetOpenProjectsNews200Response
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
    api_instance = sometech.pykitsu._client.NewsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter news by specific project (optional)
    before = '2022-07-12' # date | Filter news before this date (optional)
    after = '2022-07-12' # date | Filter news after this date (optional)
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 50 # int | Number of news items per page (optional) (default to 50)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter news by specific team member (optional)
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter news by task type (optional)
    task_status_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter news by task status (optional)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter news by specific episode (optional)
    only_preview = False # bool | Show only news related to preview uploads (optional) (default to False)

    try:
        # Get open projects news
        api_response = await api_instance.get_open_projects_news(project_id=project_id, before=before, after=after, page=page, limit=limit, person_id=person_id, task_type_id=task_type_id, task_status_id=task_status_id, episode_id=episode_id, only_preview=only_preview)
        print("The response of NewsApi->get_open_projects_news:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewsApi->get_open_projects_news: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Filter news by specific project | [optional] 
 **before** | **date**| Filter news before this date | [optional] 
 **after** | **date**| Filter news after this date | [optional] 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of news items per page | [optional] [default to 50]
 **person_id** | **UUID**| Filter news by specific team member | [optional] 
 **task_type_id** | **UUID**| Filter news by task type | [optional] 
 **task_status_id** | **UUID**| Filter news by task status | [optional] 
 **episode_id** | **UUID**| Filter news by specific episode | [optional] 
 **only_preview** | **bool**| Show only news related to preview uploads | [optional] [default to False]

### Return type

[**GetOpenProjectsNews200Response**](GetOpenProjectsNews200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | News feed successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_latest_news**
> GetProjectLatestNews200Response get_project_latest_news(project_id, before=before, after=after, page=page, limit=limit, person_id=person_id, task_type_id=task_type_id, task_status_id=task_status_id, episode_id=episode_id, only_preview=only_preview)

Get project latest news

Get the 50 latest news object (activity feed) for a project

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_latest_news200_response import GetProjectLatestNews200Response
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
    api_instance = sometech.pykitsu._client.NewsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    before = '2022-07-12' # date | Filter news before this date (optional)
    after = '2022-07-12' # date | Filter news after this date (optional)
    page = 1 # int | Page number for pagination (optional) (default to 1)
    limit = 50 # int | Number of news items per page (optional) (default to 50)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter news by specific team member (optional)
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter news by task type (optional)
    task_status_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter news by task status (optional)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter news by specific episode (optional)
    only_preview = False # bool | Show only news related to preview uploads (optional) (default to False)

    try:
        # Get project latest news
        api_response = await api_instance.get_project_latest_news(project_id, before=before, after=after, page=page, limit=limit, person_id=person_id, task_type_id=task_type_id, task_status_id=task_status_id, episode_id=episode_id, only_preview=only_preview)
        print("The response of NewsApi->get_project_latest_news:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NewsApi->get_project_latest_news: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **before** | **date**| Filter news before this date | [optional] 
 **after** | **date**| Filter news after this date | [optional] 
 **page** | **int**| Page number for pagination | [optional] [default to 1]
 **limit** | **int**| Number of news items per page | [optional] [default to 50]
 **person_id** | **UUID**| Filter news by specific team member | [optional] 
 **task_type_id** | **UUID**| Filter news by task type | [optional] 
 **task_status_id** | **UUID**| Filter news by task status | [optional] 
 **episode_id** | **UUID**| Filter news by specific episode | [optional] 
 **only_preview** | **bool**| Show only news related to preview uploads | [optional] [default to False]

### Return type

[**GetProjectLatestNews200Response**](GetProjectLatestNews200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All news related to given project |  -  |
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

