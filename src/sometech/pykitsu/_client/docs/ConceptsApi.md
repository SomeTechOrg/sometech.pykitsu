# sometech.pykitsu._client.ConceptsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_concept**](ConceptsApi.md#create_concept) | **POST** /data/projects/{project_id}/concepts | Create concept
[**delete_concept**](ConceptsApi.md#delete_concept) | **DELETE** /data/concepts/{concept_id} | Delete concept
[**get_all_concepts**](ConceptsApi.md#get_all_concepts) | **GET** /data/concepts | Get all concepts
[**get_concept**](ConceptsApi.md#get_concept) | **GET** /data/concepts/{concept_id} | Get concept
[**get_concept_previews**](ConceptsApi.md#get_concept_previews) | **GET** /data/concepts/{concept_id}/preview-files | Get concept previews
[**get_concept_task_types**](ConceptsApi.md#get_concept_task_types) | **GET** /data/concepts/{concept_id}/task-types | Get concept task types
[**get_concept_tasks**](ConceptsApi.md#get_concept_tasks) | **GET** /data/concepts/{concept_id}/tasks | Get concept tasks
[**get_concepts_and_tasks**](ConceptsApi.md#get_concepts_and_tasks) | **GET** /data/concepts/with-tasks | Get concepts and tasks
[**get_project_concepts**](ConceptsApi.md#get_project_concepts) | **GET** /data/projects/{project_id}/concepts | Get project concepts


# **create_concept**
> CreateConcept201Response create_concept(project_id, create_concept_request)

Create concept

Create a new concept for a specific project with name, description, and optional entity concept links.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_concept201_response import CreateConcept201Response
from sometech.pykitsu._client.models.create_concept_request import CreateConceptRequest
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
    api_instance = sometech.pykitsu._client.ConceptsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    create_concept_request = sometech.pykitsu._client.CreateConceptRequest() # CreateConceptRequest | 

    try:
        # Create concept
        api_response = await api_instance.create_concept(project_id, create_concept_request)
        print("The response of ConceptsApi->create_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->create_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **create_concept_request** | [**CreateConceptRequest**](CreateConceptRequest.md)|  | 

### Return type

[**CreateConcept201Response**](CreateConcept201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Concept successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_concept**
> delete_concept(concept_id, force=force)

Delete concept

Permanently remove a concept from the system. Only concept creators or project managers can delete concepts.

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
    api_instance = sometech.pykitsu._client.ConceptsApi(api_client)
    concept_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the concept to delete
    force = false # bool | Force deletion bypassing validation checks (optional)

    try:
        # Delete concept
        await api_instance.delete_concept(concept_id, force=force)
    except Exception as e:
        print("Exception when calling ConceptsApi->delete_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **UUID**| Unique identifier of the concept to delete | 
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
**204** | Concept successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_concepts**
> List[GetAllConcepts200ResponseInner] get_all_concepts(project_id=project_id, parent_id=parent_id)

Get all concepts

Retrieve all concept entries with filtering support. Filters can be specified in the query string to narrow down results by project or parent concept.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_all_concepts200_response_inner import GetAllConcepts200ResponseInner
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
    api_instance = sometech.pykitsu._client.ConceptsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter concepts by specific project (optional)
    parent_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Filter concepts by parent concept (optional)

    try:
        # Get all concepts
        api_response = await api_instance.get_all_concepts(project_id=project_id, parent_id=parent_id)
        print("The response of ConceptsApi->get_all_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->get_all_concepts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Filter concepts by specific project | [optional] 
 **parent_id** | **UUID**| Filter concepts by parent concept | [optional] 

### Return type

[**List[GetAllConcepts200ResponseInner]**](GetAllConcepts200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of concepts successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concept**
> GetConcept200Response get_concept(concept_id)

Get concept

Retrieve detailed information about a specific concept including metadata, project context, and related data.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_concept200_response import GetConcept200Response
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
    api_instance = sometech.pykitsu._client.ConceptsApi(api_client)
    concept_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the concept

    try:
        # Get concept
        api_response = await api_instance.get_concept(concept_id)
        print("The response of ConceptsApi->get_concept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->get_concept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **UUID**| Unique identifier of the concept | 

### Return type

[**GetConcept200Response**](GetConcept200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Concept information successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concept_previews**
> Dict[str, List[GetConceptPreviews200ResponseValueInner]] get_concept_previews(concept_id)

Get concept previews

Retrieve all preview files related to a specific concept. Returns them as a dictionary where keys are related task type IDs and values are arrays of previews for that task type.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_concept_previews200_response_value_inner import GetConceptPreviews200ResponseValueInner
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
    api_instance = sometech.pykitsu._client.ConceptsApi(api_client)
    concept_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the concept

    try:
        # Get concept previews
        api_response = await api_instance.get_concept_previews(concept_id)
        print("The response of ConceptsApi->get_concept_previews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->get_concept_previews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **UUID**| Unique identifier of the concept | 

### Return type

**Dict[str, List[GetConceptPreviews200ResponseValueInner]]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Concept previews successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concept_task_types**
> List[TaskType] get_concept_task_types(concept_id)

Get concept task types

Retrieve all task types that are related to a specific concept.

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
    api_instance = sometech.pykitsu._client.ConceptsApi(api_client)
    concept_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the concept

    try:
        # Get concept task types
        api_response = await api_instance.get_concept_task_types(concept_id)
        print("The response of ConceptsApi->get_concept_task_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->get_concept_task_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **UUID**| Unique identifier of the concept | 

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
**200** | List of concept task types successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concept_tasks**
> List[GetConceptTasks200ResponseInner] get_concept_tasks(concept_id, relations=relations)

Get concept tasks

Retrieve all tasks that are related to a specific concept.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_concept_tasks200_response_inner import GetConceptTasks200ResponseInner
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
    api_instance = sometech.pykitsu._client.ConceptsApi(api_client)
    concept_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the concept
    relations = true # bool | Include related entity information (optional)

    try:
        # Get concept tasks
        api_response = await api_instance.get_concept_tasks(concept_id, relations=relations)
        print("The response of ConceptsApi->get_concept_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->get_concept_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **UUID**| Unique identifier of the concept | 
 **relations** | **bool**| Include related entity information | [optional] 

### Return type

[**List[GetConceptTasks200ResponseInner]**](GetConceptTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of concept tasks successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concepts_and_tasks**
> List[GetConceptsAndTasks200ResponseInner] get_concepts_and_tasks(project_id=project_id)

Get concepts and tasks

Retrieve all concepts and all related tasks included in the response.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_concepts_and_tasks200_response_inner import GetConceptsAndTasks200ResponseInner
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
    api_instance = sometech.pykitsu._client.ConceptsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter concepts by specific project (optional)

    try:
        # Get concepts and tasks
        api_response = await api_instance.get_concepts_and_tasks(project_id=project_id)
        print("The response of ConceptsApi->get_concepts_and_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->get_concepts_and_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Filter concepts by specific project | [optional] 

### Return type

[**List[GetConceptsAndTasks200ResponseInner]**](GetConceptsAndTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Concepts with tasks successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_concepts**
> List[GetConcept200Response] get_project_concepts(project_id)

Get project concepts

Retrieve all concepts that are related to a specific project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_concept200_response import GetConcept200Response
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
    api_instance = sometech.pykitsu._client.ConceptsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project

    try:
        # Get project concepts
        api_response = await api_instance.get_project_concepts(project_id)
        print("The response of ConceptsApi->get_project_concepts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptsApi->get_project_concepts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 

### Return type

[**List[GetConcept200Response]**](GetConcept200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of project concepts successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

