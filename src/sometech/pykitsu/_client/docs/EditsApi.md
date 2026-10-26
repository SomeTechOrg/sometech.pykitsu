# sometech.pykitsu._client.EditsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_edit**](EditsApi.md#create_edit) | **POST** /data/projects/{project_id}/edits | Create edit
[**delete_edit**](EditsApi.md#delete_edit) | **DELETE** /data/edits/{edit_id} | Delete edit
[**get_all_edits**](EditsApi.md#get_all_edits) | **GET** /data/edits | Get all edits
[**get_edit**](EditsApi.md#get_edit) | **GET** /data/edits/{edit_id} | Get edit
[**get_edit_previews**](EditsApi.md#get_edit_previews) | **GET** /data/edits/{edit_id}/preview-files | Get edit previews
[**get_edit_task_types**](EditsApi.md#get_edit_task_types) | **GET** /data/edits/{edit_id}/task-types | Get edit task types
[**get_edit_tasks**](EditsApi.md#get_edit_tasks) | **GET** /data/edits/{edit_id}/tasks | Get edit tasks
[**get_edit_versions**](EditsApi.md#get_edit_versions) | **GET** /data/edits/{edit_id}/versions | Get edit versions
[**get_edits**](EditsApi.md#get_edits) | **GET** /data/edits/all | Get edits
[**get_edits_and_tasks**](EditsApi.md#get_edits_and_tasks) | **GET** /data/edits/with-tasks | Get edits and tasks
[**get_episode_edit_tasks**](EditsApi.md#get_episode_edit_tasks) | **GET** /data/episodes/{episode_id}/edit-tasks | Get episode edit tasks
[**get_episode_edits**](EditsApi.md#get_episode_edits) | **GET** /data/episodes/{episode_id}/edits | Get episode edits
[**get_project_edits**](EditsApi.md#get_project_edits) | **GET** /data/projects/{project_id}/edits | Get project edits


# **create_edit**
> CreateEdit201Response create_edit(project_id, create_edit_request)

Create edit

Create a new edit for a specific project with name, description, and optional episode association.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_edit201_response import CreateEdit201Response
from sometech.pykitsu._client.models.create_edit_request import CreateEditRequest
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
    api_instance = sometech.pykitsu._client.EditsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    create_edit_request = sometech.pykitsu._client.CreateEditRequest() # CreateEditRequest | 

    try:
        # Create edit
        api_response = await api_instance.create_edit(project_id, create_edit_request)
        print("The response of EditsApi->create_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditsApi->create_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **create_edit_request** | [**CreateEditRequest**](CreateEditRequest.md)|  | 

### Return type

[**CreateEdit201Response**](CreateEdit201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Edit successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_edit**
> delete_edit(edit_id, force=force)

Delete edit

Permanently remove an edit from the system. Only edit creators or project managers can delete edits.

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
    api_instance = sometech.pykitsu._client.EditsApi(api_client)
    edit_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the edit to delete
    force = false # bool | Force deletion bypassing validation checks (optional)

    try:
        # Delete edit
        await api_instance.delete_edit(edit_id, force=force)
    except Exception as e:
        print("Exception when calling EditsApi->delete_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_id** | **UUID**| Unique identifier of the edit to delete | 
 **force** | **bool**| Force deletion bypassing validation checks | [optional] 

### Return type

void (empty response body)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Edit successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_edits**
> List[GetAllEdits200ResponseInner] get_all_edits(project_id=project_id, name=name, force=force)

Get all edits

Retrieve all edit entries with filtering support. Filters can be specified in the query string.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_all_edits200_response_inner import GetAllEdits200ResponseInner
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
    api_instance = sometech.pykitsu._client.EditsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter edits by specific project (optional)
    name = 'Opening Sequence' # str | Filter edits by name (optional)
    force = False # bool | Force parameter for additional filtering (optional) (default to False)

    try:
        # Get all edits
        api_response = await api_instance.get_all_edits(project_id=project_id, name=name, force=force)
        print("The response of EditsApi->get_all_edits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditsApi->get_all_edits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Filter edits by specific project | [optional] 
 **name** | **str**| Filter edits by name | [optional] 
 **force** | **bool**| Force parameter for additional filtering | [optional] [default to False]

### Return type

[**List[GetAllEdits200ResponseInner]**](GetAllEdits200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all edits successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edit**
> GetAllEdits200ResponseInner get_edit(edit_id)

Get edit

Retrieve detailed information about a specific edit.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_all_edits200_response_inner import GetAllEdits200ResponseInner
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
    api_instance = sometech.pykitsu._client.EditsApi(api_client)
    edit_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the edit

    try:
        # Get edit
        api_response = await api_instance.get_edit(edit_id)
        print("The response of EditsApi->get_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditsApi->get_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_id** | **UUID**| Unique identifier of the edit | 

### Return type

[**GetAllEdits200ResponseInner**](GetAllEdits200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit information successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edit_previews**
> Dict[str, List[GetEditPreviews200ResponseValueInner]] get_edit_previews(edit_id)

Get edit previews

Retrieve all preview files related to a specific edit. Returns them as a dictionary where keys are related task type IDs and values are arrays of previews for that task type.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_edit_previews200_response_value_inner import GetEditPreviews200ResponseValueInner
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
    api_instance = sometech.pykitsu._client.EditsApi(api_client)
    edit_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the edit

    try:
        # Get edit previews
        api_response = await api_instance.get_edit_previews(edit_id)
        print("The response of EditsApi->get_edit_previews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditsApi->get_edit_previews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_id** | **UUID**| Unique identifier of the edit | 

### Return type

**Dict[str, List[GetEditPreviews200ResponseValueInner]]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit previews successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edit_task_types**
> List[TaskType] get_edit_task_types(edit_id)

Get edit task types

Retrieve all task types that are related to a specific edit.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.task_type import TaskType
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
    api_instance = sometech.pykitsu._client.EditsApi(api_client)
    edit_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the edit

    try:
        # Get edit task types
        api_response = await api_instance.get_edit_task_types(edit_id)
        print("The response of EditsApi->get_edit_task_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditsApi->get_edit_task_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_id** | **UUID**| Unique identifier of the edit | 

### Return type

[**List[TaskType]**](TaskType.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of edit task types successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edit_tasks**
> List[GetEditTasks200ResponseInner] get_edit_tasks(edit_id, relations=relations)

Get edit tasks

Retrieve all tasks that are related to a specific edit.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_edit_tasks200_response_inner import GetEditTasks200ResponseInner
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
    api_instance = sometech.pykitsu._client.EditsApi(api_client)
    edit_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the edit
    relations = true # bool | Include related entity information (optional)

    try:
        # Get edit tasks
        api_response = await api_instance.get_edit_tasks(edit_id, relations=relations)
        print("The response of EditsApi->get_edit_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditsApi->get_edit_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_id** | **UUID**| Unique identifier of the edit | 
 **relations** | **bool**| Include related entity information | [optional] 

### Return type

[**List[GetEditTasks200ResponseInner]**](GetEditTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of edit tasks successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edit_versions**
> List[GetEditVersions200ResponseInner] get_edit_versions(edit_id)

Get edit versions

Retrieve all data versions of a specific edit. This includes historical versions and metadata about changes over time.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_edit_versions200_response_inner import GetEditVersions200ResponseInner
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
    api_instance = sometech.pykitsu._client.EditsApi(api_client)
    edit_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the edit

    try:
        # Get edit versions
        api_response = await api_instance.get_edit_versions(edit_id)
        print("The response of EditsApi->get_edit_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditsApi->get_edit_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_id** | **UUID**| Unique identifier of the edit | 

### Return type

[**List[GetEditVersions200ResponseInner]**](GetEditVersions200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit versions successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edits**
> List[GetAllEdits200ResponseInner] get_edits(project_id=project_id, name=name, force=force)

Get edits

Retrieve all edit entries with filtering support. Filters can be specified in the query string.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_all_edits200_response_inner import GetAllEdits200ResponseInner
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
    api_instance = sometech.pykitsu._client.EditsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter edits by specific project (optional)
    name = 'Opening Sequence' # str | Filter edits by name (optional)
    force = False # bool | Force parameter for additional filtering (optional) (default to False)

    try:
        # Get edits
        api_response = await api_instance.get_edits(project_id=project_id, name=name, force=force)
        print("The response of EditsApi->get_edits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditsApi->get_edits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Filter edits by specific project | [optional] 
 **name** | **str**| Filter edits by name | [optional] 
 **force** | **bool**| Force parameter for additional filtering | [optional] [default to False]

### Return type

[**List[GetAllEdits200ResponseInner]**](GetAllEdits200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of edits successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edits_and_tasks**
> List[GetEditsAndTasks200ResponseInner] get_edits_and_tasks(project_id=project_id, name=name, force=force)

Get edits and tasks

Retrieve all edits with project name and all related tasks.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_edits_and_tasks200_response_inner import GetEditsAndTasks200ResponseInner
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
    api_instance = sometech.pykitsu._client.EditsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter edits by specific project (optional)
    name = 'Opening Sequence' # str | Filter edits by name (optional)
    force = False # bool | Force parameter for additional filtering (optional) (default to False)

    try:
        # Get edits and tasks
        api_response = await api_instance.get_edits_and_tasks(project_id=project_id, name=name, force=force)
        print("The response of EditsApi->get_edits_and_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditsApi->get_edits_and_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Filter edits by specific project | [optional] 
 **name** | **str**| Filter edits by name | [optional] 
 **force** | **bool**| Force parameter for additional filtering | [optional] [default to False]

### Return type

[**List[GetEditsAndTasks200ResponseInner]**](GetEditsAndTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edits with tasks successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episode_edit_tasks**
> List[GetEpisodeEditTasks200ResponseInner] get_episode_edit_tasks(episode_id, relations=relations)

Get episode edit tasks

Retrieve all tasks that are related to a specific episode.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_episode_edit_tasks200_response_inner import GetEpisodeEditTasks200ResponseInner
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
    api_instance = sometech.pykitsu._client.EditsApi(api_client)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the episode
    relations = true # bool | Include related entity information (optional)

    try:
        # Get episode edit tasks
        api_response = await api_instance.get_episode_edit_tasks(episode_id, relations=relations)
        print("The response of EditsApi->get_episode_edit_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditsApi->get_episode_edit_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_id** | **UUID**| Unique identifier of the episode | 
 **relations** | **bool**| Include related entity information | [optional] 

### Return type

[**List[GetEpisodeEditTasks200ResponseInner]**](GetEpisodeEditTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of episode edit tasks successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episode_edits**
> List[GetEpisodeEdits200ResponseInner] get_episode_edits(episode_id, relations=relations)

Get episode edits

Retrieve all edits that are related to a specific episode.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_episode_edits200_response_inner import GetEpisodeEdits200ResponseInner
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
    api_instance = sometech.pykitsu._client.EditsApi(api_client)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the episode
    relations = true # bool | Include related entity information (optional)

    try:
        # Get episode edits
        api_response = await api_instance.get_episode_edits(episode_id, relations=relations)
        print("The response of EditsApi->get_episode_edits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditsApi->get_episode_edits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_id** | **UUID**| Unique identifier of the episode | 
 **relations** | **bool**| Include related entity information | [optional] 

### Return type

[**List[GetEpisodeEdits200ResponseInner]**](GetEpisodeEdits200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of episode edits successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_edits**
> List[GetAllEdits200ResponseInner] get_project_edits(project_id)

Get project edits

Retrieve all edits that are related to a specific project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_all_edits200_response_inner import GetAllEdits200ResponseInner
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
    api_instance = sometech.pykitsu._client.EditsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project

    try:
        # Get project edits
        api_response = await api_instance.get_project_edits(project_id)
        print("The response of EditsApi->get_project_edits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditsApi->get_project_edits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 

### Return type

[**List[GetAllEdits200ResponseInner]**](GetAllEdits200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of project edits successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

