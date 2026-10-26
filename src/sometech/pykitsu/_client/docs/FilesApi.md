# sometech.pykitsu._client.FilesApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_entity_output_file**](FilesApi.md#create_new_entity_output_file) | **POST** /data/entities/{entity_id}/output-files/new | Create new entity output file
[**create_new_instance_output_file**](FilesApi.md#create_new_instance_output_file) | **POST** /data/asset-instances/{asset_instance_id}/entities/{temporal_entity_id}/output-files/new | Create new instance output file
[**create_new_working_file**](FilesApi.md#create_new_working_file) | **POST** /data/tasks/{task_id}/working-files/new | Create new working file
[**download_working_file**](FilesApi.md#download_working_file) | **GET** /data/working-files/{working_file_id}/file | Download working file
[**generate_entity_output_file_path**](FilesApi.md#generate_entity_output_file_path) | **POST** /data/entities/{entity_id}/output-file-path | Generate entity output file path
[**generate_instance_output_file_path**](FilesApi.md#generate_instance_output_file_path) | **POST** /data/asset-instances/{asset_instance_id}/entities/{temporal_entity_id}/output-file-path | Generate instance output file path
[**generate_working_file_path**](FilesApi.md#generate_working_file_path) | **POST** /data/tasks/{task_id}/working-file-path | Generate working file path
[**get_entity_output_files**](FilesApi.md#get_entity_output_files) | **GET** /data/entities/{entity_id}/output-files | Get entity output files
[**get_entity_output_type_files**](FilesApi.md#get_entity_output_type_files) | **GET** /data/entities/{entity_id}/output-types/{output_type_id}/output-files | Get entity output type files
[**get_entity_output_types**](FilesApi.md#get_entity_output_types) | **GET** /data/entities/{entity_id}/output-types | Get entity output types
[**get_entity_working_files**](FilesApi.md#get_entity_working_files) | **GET** /data/entities/{entity_id}/working-files | Get entity working files
[**get_file_information**](FilesApi.md#get_file_information) | **GET** /data/files/{file_id} | Get file information
[**get_instance_output_files**](FilesApi.md#get_instance_output_files) | **GET** /data/asset-instances/{asset_instance_id}/output-files | Get instance output files
[**get_instance_output_type_files**](FilesApi.md#get_instance_output_type_files) | **GET** /data/asset-instances/{asset_instance_id}/entities/{temporal_entity_id}/output-types/{output_type_id}/output-files | Get instance output type files
[**get_instance_output_types**](FilesApi.md#get_instance_output_types) | **GET** /data/asset-instances/{asset_instance_id}/entities/{temporal_entity_id}/output-types | Get instance output types
[**get_last_entity_output_files**](FilesApi.md#get_last_entity_output_files) | **GET** /data/entities/{entity_id}/output-files/last-revisions | Get last entity output files
[**get_last_instance_output_files**](FilesApi.md#get_last_instance_output_files) | **GET** /data/asset-instances/{asset_instance_id}/entities/{temporal_entity_id}/output-files/last-revisions | Get last instance output files
[**get_last_working_files**](FilesApi.md#get_last_working_files) | **GET** /data/tasks/{task_id}/working-files/last-revisions | Get last working files
[**get_next_entity_output_file_revision**](FilesApi.md#get_next_entity_output_file_revision) | **POST** /data/entities/{entity_id}/output-files/next-revision | Get next entity output file revision
[**get_next_instance_output_file_revision**](FilesApi.md#get_next_instance_output_file_revision) | **POST** /data/asset-instances/{asset_instance_id}/entities/{temporal_entity_id}/output-files/next-revision | Get next instance output file revision
[**get_project_output_files**](FilesApi.md#get_project_output_files) | **GET** /data/projects/{project_id}/output-files | Get project output files
[**get_task_working_files**](FilesApi.md#get_task_working_files) | **GET** /data/tasks/{task_id}/working-files | Get task working files
[**guess_file_tree_template**](FilesApi.md#guess_file_tree_template) | **POST** /data/entities/guess_from_path | Guess file tree template
[**set_project_file_tree**](FilesApi.md#set_project_file_tree) | **POST** /actions/projects/{project_id}/set-file-tree | Set project file tree
[**store_working_file**](FilesApi.md#store_working_file) | **POST** /data/working-files/{working_file_id}/file | Store working file
[**update_working_file_comment**](FilesApi.md#update_working_file_comment) | **PUT** /actions/working-files/{working_file_id}/comment | Update working file comment
[**update_working_file_modification_date**](FilesApi.md#update_working_file_modification_date) | **PUT** /actions/working-files/{working_file_id}/modified | Update working file modification date


# **create_new_entity_output_file**
> CreateNewEntityOutputFile201Response create_new_entity_output_file(entity_id, create_new_entity_output_file_request)

Create new entity output file

Create a new output file linked to a specific entity. Output files are created when artists are satisfied with their working files. They track the source working file and require output type and task type for categorization. An output type is required for better categorization (textures, caches, ...). A task type can be set too to give the department related to the output file. The revision is automatically set.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_new_entity_output_file201_response import CreateNewEntityOutputFile201Response
from sometech.pykitsu._client.models.create_new_entity_output_file_request import CreateNewEntityOutputFileRequest
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Entity unique identifier
    create_new_entity_output_file_request = sometech.pykitsu._client.CreateNewEntityOutputFileRequest() # CreateNewEntityOutputFileRequest | 

    try:
        # Create new entity output file
        api_response = await api_instance.create_new_entity_output_file(entity_id, create_new_entity_output_file_request)
        print("The response of FilesApi->create_new_entity_output_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_new_entity_output_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Entity unique identifier | 
 **create_new_entity_output_file_request** | [**CreateNewEntityOutputFileRequest**](CreateNewEntityOutputFileRequest.md)|  | 

### Return type

[**CreateNewEntityOutputFile201Response**](CreateNewEntityOutputFile201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | New output file created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_instance_output_file**
> OutputFile create_new_instance_output_file(asset_instance_id, temporal_entity_id, create_new_instance_output_file_request)

Create new instance output file

Create a new output file linked to an asset instance for a specific shot. Output files track the source working file and require output type and task type for categorization.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_new_instance_output_file_request import CreateNewInstanceOutputFileRequest
from sometech.pykitsu._client.models.output_file import OutputFile
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    asset_instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Asset instance unique identifier
    temporal_entity_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Temporal entity unique identifier
    create_new_instance_output_file_request = sometech.pykitsu._client.CreateNewInstanceOutputFileRequest() # CreateNewInstanceOutputFileRequest | 

    try:
        # Create new instance output file
        api_response = await api_instance.create_new_instance_output_file(asset_instance_id, temporal_entity_id, create_new_instance_output_file_request)
        print("The response of FilesApi->create_new_instance_output_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_new_instance_output_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_instance_id** | **UUID**| Asset instance unique identifier | 
 **temporal_entity_id** | **UUID**| Temporal entity unique identifier | 
 **create_new_instance_output_file_request** | [**CreateNewInstanceOutputFileRequest**](CreateNewInstanceOutputFileRequest.md)|  | 

### Return type

[**OutputFile**](OutputFile.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | New output file created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_working_file**
> CreateNewWorkingFile201Response create_new_working_file(task_id, create_new_working_file_request)

Create new working file

Create a new working file for a task. Working files are versioned files used by artists to produce output files. Each file requires a comment and generates a path based on file tree template.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_new_working_file201_response import CreateNewWorkingFile201Response
from sometech.pykitsu._client.models.create_new_working_file_request import CreateNewWorkingFileRequest
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Task unique identifier
    create_new_working_file_request = sometech.pykitsu._client.CreateNewWorkingFileRequest() # CreateNewWorkingFileRequest | 

    try:
        # Create new working file
        api_response = await api_instance.create_new_working_file(task_id, create_new_working_file_request)
        print("The response of FilesApi->create_new_working_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_new_working_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Task unique identifier | 
 **create_new_working_file_request** | [**CreateNewWorkingFileRequest**](CreateNewWorkingFileRequest.md)|  | 

### Return type

[**CreateNewWorkingFile201Response**](CreateNewWorkingFile201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | New working file created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_working_file**
> bytes download_working_file(working_file_id)

Download working file

Download a working file from storage. Returns the file content with appropriate headers for caching and attachment.

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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    working_file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Working file unique identifier

    try:
        # Download working file
        api_response = await api_instance.download_working_file(working_file_id)
        print("The response of FilesApi->download_working_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->download_working_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working_file_id** | **UUID**| Working file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, image/jpg, image/gif, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Working file downloaded successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_entity_output_file_path**
> GenerateEntityOutputFilePath200Response generate_entity_output_file_path(entity_id, generate_entity_output_file_path_request)

Generate entity output file path

Generate an output file path from file tree template based on entity parameters. Revision can be computed automatically if not provided.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.generate_entity_output_file_path200_response import GenerateEntityOutputFilePath200Response
from sometech.pykitsu._client.models.generate_entity_output_file_path_request import GenerateEntityOutputFilePathRequest
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Entity unique identifier
    generate_entity_output_file_path_request = sometech.pykitsu._client.GenerateEntityOutputFilePathRequest() # GenerateEntityOutputFilePathRequest | 

    try:
        # Generate entity output file path
        api_response = await api_instance.generate_entity_output_file_path(entity_id, generate_entity_output_file_path_request)
        print("The response of FilesApi->generate_entity_output_file_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->generate_entity_output_file_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Entity unique identifier | 
 **generate_entity_output_file_path_request** | [**GenerateEntityOutputFilePathRequest**](GenerateEntityOutputFilePathRequest.md)|  | 

### Return type

[**GenerateEntityOutputFilePath200Response**](GenerateEntityOutputFilePath200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Output file path generated successfully |  -  |
**400** | Malformed file tree |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_instance_output_file_path**
> GenerateInstanceOutputFilePath200Response generate_instance_output_file_path(asset_instance_id, temporal_entity_id, generate_instance_output_file_path_request)

Generate instance output file path

Generate an output file path from file tree template based on asset instance parameters. Revision can be computed automatically if not provided.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.generate_instance_output_file_path200_response import GenerateInstanceOutputFilePath200Response
from sometech.pykitsu._client.models.generate_instance_output_file_path_request import GenerateInstanceOutputFilePathRequest
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    asset_instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Asset instance unique identifier
    temporal_entity_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Temporal entity unique identifier
    generate_instance_output_file_path_request = sometech.pykitsu._client.GenerateInstanceOutputFilePathRequest() # GenerateInstanceOutputFilePathRequest | 

    try:
        # Generate instance output file path
        api_response = await api_instance.generate_instance_output_file_path(asset_instance_id, temporal_entity_id, generate_instance_output_file_path_request)
        print("The response of FilesApi->generate_instance_output_file_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->generate_instance_output_file_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_instance_id** | **UUID**| Asset instance unique identifier | 
 **temporal_entity_id** | **UUID**| Temporal entity unique identifier | 
 **generate_instance_output_file_path_request** | [**GenerateInstanceOutputFilePathRequest**](GenerateInstanceOutputFilePathRequest.md)|  | 

### Return type

[**GenerateInstanceOutputFilePath200Response**](GenerateInstanceOutputFilePath200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Output file path generated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_working_file_path**
> GenerateWorkingFilePath200Response generate_working_file_path(task_id, generate_working_file_path_request)

Generate working file path

Generate a working file path from file tree template based on task parameters. Revision can be computed automatically if not provided.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.generate_working_file_path200_response import GenerateWorkingFilePath200Response
from sometech.pykitsu._client.models.generate_working_file_path_request import GenerateWorkingFilePathRequest
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Task unique identifier
    generate_working_file_path_request = sometech.pykitsu._client.GenerateWorkingFilePathRequest() # GenerateWorkingFilePathRequest | 

    try:
        # Generate working file path
        api_response = await api_instance.generate_working_file_path(task_id, generate_working_file_path_request)
        print("The response of FilesApi->generate_working_file_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->generate_working_file_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Task unique identifier | 
 **generate_working_file_path_request** | [**GenerateWorkingFilePathRequest**](GenerateWorkingFilePathRequest.md)|  | 

### Return type

[**GenerateWorkingFilePath200Response**](GenerateWorkingFilePath200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Working file path generated successfully |  -  |
**400** | Malformed file tree |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_output_files**
> List[OutputFile] get_entity_output_files(entity_id, output_type_id=output_type_id, task_type_id=task_type_id, file_status_id=file_status_id, representation=representation, name=name)

Get entity output files

Retrieve all output files for a given entity with optional filtering by output type, task type, representation, file status, and name.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.output_file import OutputFile
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Entity unique identifier
    output_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Filter by output type (optional)
    task_type_id = UUID('c46c8gc6-eg97-6887-c292-79675204e47') # UUID | Filter by task type (optional)
    file_status_id = UUID('d57d9hd7-fh08-7998-d403-80786315f58') # UUID | Filter by file status (optional)
    representation = 'cache' # str | Filter by representation (optional)
    name = 'main' # str | Filter by file name (optional)

    try:
        # Get entity output files
        api_response = await api_instance.get_entity_output_files(entity_id, output_type_id=output_type_id, task_type_id=task_type_id, file_status_id=file_status_id, representation=representation, name=name)
        print("The response of FilesApi->get_entity_output_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_entity_output_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Entity unique identifier | 
 **output_type_id** | **UUID**| Filter by output type | [optional] 
 **task_type_id** | **UUID**| Filter by task type | [optional] 
 **file_status_id** | **UUID**| Filter by file status | [optional] 
 **representation** | **str**| Filter by representation | [optional] 
 **name** | **str**| Filter by file name | [optional] 

### Return type

[**List[OutputFile]**](OutputFile.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All output files for the entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_output_type_files**
> List[OutputFile] get_entity_output_type_files(entity_id, output_type_id, representation=representation)

Get entity output type files

Retrieve all output files for a given entity and output type. Optionally filter by representation.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.output_file import OutputFile
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Entity unique identifier
    output_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Output type unique identifier
    representation = 'mp4' # str | Filter by representation (optional)

    try:
        # Get entity output type files
        api_response = await api_instance.get_entity_output_type_files(entity_id, output_type_id, representation=representation)
        print("The response of FilesApi->get_entity_output_type_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_entity_output_type_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Entity unique identifier | 
 **output_type_id** | **UUID**| Output type unique identifier | 
 **representation** | **str**| Filter by representation | [optional] 

### Return type

[**List[OutputFile]**](OutputFile.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All output files for the entity and output type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_output_types**
> List[GetEntityOutputTypes200ResponseInner] get_entity_output_types(entity_id)

Get entity output types

Retrieve all types of output files generated for a given entity. Returns list of output types available for the entity.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_entity_output_types200_response_inner import GetEntityOutputTypes200ResponseInner
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Entity unique identifier

    try:
        # Get entity output types
        api_response = await api_instance.get_entity_output_types(entity_id)
        print("The response of FilesApi->get_entity_output_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_entity_output_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Entity unique identifier | 

### Return type

[**List[GetEntityOutputTypes200ResponseInner]**](GetEntityOutputTypes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All types of output files generated for the entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_working_files**
> List[WorkingFile] get_entity_working_files(entity_id, task_id=task_id, name=name)

Get entity working files

Retrieve all working files for a given entity with optional filtering by task and name. Returns complete list of working files with their revisions.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.working_file import WorkingFile
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Entity unique identifier
    task_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Filter by task (optional)
    name = 'main' # str | Filter by file name (optional)

    try:
        # Get entity working files
        api_response = await api_instance.get_entity_working_files(entity_id, task_id=task_id, name=name)
        print("The response of FilesApi->get_entity_working_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_entity_working_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Entity unique identifier | 
 **task_id** | **UUID**| Filter by task | [optional] 
 **name** | **str**| Filter by file name | [optional] 

### Return type

[**List[WorkingFile]**](WorkingFile.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All working files for the entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_information**
> GetFileInformation200Response get_file_information(file_id)

Get file information

Retrieve information about a file that could be either a working file or an output file. Returns detailed file metadata and properties.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_file_information200_response import GetFileInformation200Response
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | File unique identifier

    try:
        # Get file information
        api_response = await api_instance.get_file_information(file_id)
        print("The response of FilesApi->get_file_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **UUID**| File unique identifier | 

### Return type

[**GetFileInformation200Response**](GetFileInformation200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File information retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_output_files**
> List[OutputFile] get_instance_output_files(asset_instance_id, temporal_entity_id=temporal_entity_id, output_type_id=output_type_id, task_type_id=task_type_id, file_status_id=file_status_id, representation=representation, name=name)

Get instance output files

Retrieve all output files for a given asset instance and temporal entity with optional filtering by output type, task type, representation, file status, and name.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.output_file import OutputFile
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    asset_instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Asset instance unique identifier
    temporal_entity_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Filter by temporal entity (optional)
    output_type_id = UUID('c46c8gc6-eg97-6887-c292-79675204e47') # UUID | Filter by output type (optional)
    task_type_id = UUID('d57d9hd7-fh08-7998-d403-80786315f58') # UUID | Filter by task type (optional)
    file_status_id = UUID('e68e0ie8-gi19-8009-e514-91897426g69') # UUID | Filter by file status (optional)
    representation = 'cache' # str | Filter by representation (optional)
    name = 'main' # str | Filter by file name (optional)

    try:
        # Get instance output files
        api_response = await api_instance.get_instance_output_files(asset_instance_id, temporal_entity_id=temporal_entity_id, output_type_id=output_type_id, task_type_id=task_type_id, file_status_id=file_status_id, representation=representation, name=name)
        print("The response of FilesApi->get_instance_output_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_instance_output_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_instance_id** | **UUID**| Asset instance unique identifier | 
 **temporal_entity_id** | **UUID**| Filter by temporal entity | [optional] 
 **output_type_id** | **UUID**| Filter by output type | [optional] 
 **task_type_id** | **UUID**| Filter by task type | [optional] 
 **file_status_id** | **UUID**| Filter by file status | [optional] 
 **representation** | **str**| Filter by representation | [optional] 
 **name** | **str**| Filter by file name | [optional] 

### Return type

[**List[OutputFile]**](OutputFile.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All output files for the asset instance and temporal entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_output_type_files**
> List[OutputFile] get_instance_output_type_files(asset_instance_id, temporal_entity_id, output_type_id, representation=representation)

Get instance output type files

Retrieve all output files for a given asset instance, temporal entity, and output type. Optionally filter by representation.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.output_file import OutputFile
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    asset_instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Asset instance unique identifier
    temporal_entity_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Temporal entity unique identifier
    output_type_id = UUID('c46c8gc6-eg97-6887-c292-79675204e47') # UUID | Output type unique identifier
    representation = 'mp4' # str | Filter by representation (optional)

    try:
        # Get instance output type files
        api_response = await api_instance.get_instance_output_type_files(asset_instance_id, temporal_entity_id, output_type_id, representation=representation)
        print("The response of FilesApi->get_instance_output_type_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_instance_output_type_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_instance_id** | **UUID**| Asset instance unique identifier | 
 **temporal_entity_id** | **UUID**| Temporal entity unique identifier | 
 **output_type_id** | **UUID**| Output type unique identifier | 
 **representation** | **str**| Filter by representation | [optional] 

### Return type

[**List[OutputFile]**](OutputFile.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All output files for the asset instance and output type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_output_types**
> List[GetInstanceOutputTypes200ResponseInner] get_instance_output_types(asset_instance_id, temporal_entity_id)

Get instance output types

Retrieve all types of output files generated for a given asset instance and temporal entity. Returns list of output types available for the instance.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_instance_output_types200_response_inner import GetInstanceOutputTypes200ResponseInner
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    asset_instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Asset instance unique identifier
    temporal_entity_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Temporal entity unique identifier

    try:
        # Get instance output types
        api_response = await api_instance.get_instance_output_types(asset_instance_id, temporal_entity_id)
        print("The response of FilesApi->get_instance_output_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_instance_output_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_instance_id** | **UUID**| Asset instance unique identifier | 
 **temporal_entity_id** | **UUID**| Temporal entity unique identifier | 

### Return type

[**List[GetInstanceOutputTypes200ResponseInner]**](GetInstanceOutputTypes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All types of output files generated for the instance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_entity_output_files**
> Dict[str, GetLastEntityOutputFiles200ResponseValue] get_last_entity_output_files(entity_id, output_type_id=output_type_id, task_type_id=task_type_id, representation=representation, file_status_id=file_status_id, name=name)

Get last entity output files

Retrieve the last revisions of output files for a given entity grouped by output type and file name. Returns the most recent version of each output file.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_last_entity_output_files200_response_value import GetLastEntityOutputFiles200ResponseValue
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Entity unique identifier
    output_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Filter by output type (optional)
    task_type_id = UUID('c46c8gc6-eg97-6887-c292-79675204e47') # UUID | Filter by task type (optional)
    representation = 'mp4' # str | Filter by representation (optional)
    file_status_id = UUID('d57d9hd7-fh08-7998-d403-80786315f58') # UUID | Filter by file status (optional)
    name = 'main' # str | Filter by file name (optional)

    try:
        # Get last entity output files
        api_response = await api_instance.get_last_entity_output_files(entity_id, output_type_id=output_type_id, task_type_id=task_type_id, representation=representation, file_status_id=file_status_id, name=name)
        print("The response of FilesApi->get_last_entity_output_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_last_entity_output_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Entity unique identifier | 
 **output_type_id** | **UUID**| Filter by output type | [optional] 
 **task_type_id** | **UUID**| Filter by task type | [optional] 
 **representation** | **str**| Filter by representation | [optional] 
 **file_status_id** | **UUID**| Filter by file status | [optional] 
 **name** | **str**| Filter by file name | [optional] 

### Return type

[**Dict[str, GetLastEntityOutputFiles200ResponseValue]**](GetLastEntityOutputFiles200ResponseValue.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Last revisions of output files grouped by output type and file name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_instance_output_files**
> Dict[str, GetLastInstanceOutputFiles200ResponseValue] get_last_instance_output_files(asset_instance_id, temporal_entity_id, output_type_id=output_type_id, task_type_id=task_type_id, file_status_id=file_status_id, representation=representation, name=name)

Get last instance output files

Retrieve the last revisions of output files for a given instance grouped by output type and file name. Returns the most recent version of each output file.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_last_instance_output_files200_response_value import GetLastInstanceOutputFiles200ResponseValue
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    asset_instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Asset instance unique identifier
    temporal_entity_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Temporal entity unique identifier
    output_type_id = UUID('c46c8gc6-eg97-6887-c292-79675204e47') # UUID | Filter by output type (optional)
    task_type_id = UUID('d57d9hd7-fh08-7998-d403-80786315f58') # UUID | Filter by task type (optional)
    file_status_id = UUID('e68e0ie8-gi19-8009-e514-91897426g69') # UUID | Filter by file status (optional)
    representation = 'cache' # str | Filter by representation (optional)
    name = 'main' # str | Filter by file name (optional)

    try:
        # Get last instance output files
        api_response = await api_instance.get_last_instance_output_files(asset_instance_id, temporal_entity_id, output_type_id=output_type_id, task_type_id=task_type_id, file_status_id=file_status_id, representation=representation, name=name)
        print("The response of FilesApi->get_last_instance_output_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_last_instance_output_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_instance_id** | **UUID**| Asset instance unique identifier | 
 **temporal_entity_id** | **UUID**| Temporal entity unique identifier | 
 **output_type_id** | **UUID**| Filter by output type | [optional] 
 **task_type_id** | **UUID**| Filter by task type | [optional] 
 **file_status_id** | **UUID**| Filter by file status | [optional] 
 **representation** | **str**| Filter by representation | [optional] 
 **name** | **str**| Filter by file name | [optional] 

### Return type

[**Dict[str, GetLastInstanceOutputFiles200ResponseValue]**](GetLastInstanceOutputFiles200ResponseValue.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Last revisions of output files grouped by output type and file name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_working_files**
> Dict[str, GetLastWorkingFiles200ResponseValue] get_last_working_files(task_id)

Get last working files

Retrieve the last working file revisions for each file name for a given task. Returns the most recent version of each working file.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_last_working_files200_response_value import GetLastWorkingFiles200ResponseValue
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Task unique identifier

    try:
        # Get last working files
        api_response = await api_instance.get_last_working_files(task_id)
        print("The response of FilesApi->get_last_working_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_last_working_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Task unique identifier | 

### Return type

[**Dict[str, GetLastWorkingFiles200ResponseValue]**](GetLastWorkingFiles200ResponseValue.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Last working file revisions for each file name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_next_entity_output_file_revision**
> GetNextEntityOutputFileRevision200Response get_next_entity_output_file_revision(entity_id, get_next_instance_output_file_revision_request)

Get next entity output file revision

Get the next revision number for an output file based on entity, output type, task type, and name. Used for automatic revision numbering.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_next_entity_output_file_revision200_response import GetNextEntityOutputFileRevision200Response
from sometech.pykitsu._client.models.get_next_instance_output_file_revision_request import GetNextInstanceOutputFileRevisionRequest
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Entity unique identifier
    get_next_instance_output_file_revision_request = sometech.pykitsu._client.GetNextInstanceOutputFileRevisionRequest() # GetNextInstanceOutputFileRevisionRequest | 

    try:
        # Get next entity output file revision
        api_response = await api_instance.get_next_entity_output_file_revision(entity_id, get_next_instance_output_file_revision_request)
        print("The response of FilesApi->get_next_entity_output_file_revision:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_next_entity_output_file_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Entity unique identifier | 
 **get_next_instance_output_file_revision_request** | [**GetNextInstanceOutputFileRevisionRequest**](GetNextInstanceOutputFileRevisionRequest.md)|  | 

### Return type

[**GetNextEntityOutputFileRevision200Response**](GetNextEntityOutputFileRevision200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Next revision number for the output file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_next_instance_output_file_revision**
> GetNextInstanceOutputFileRevision200Response get_next_instance_output_file_revision(asset_instance_id, temporal_entity_id, get_next_instance_output_file_revision_request)

Get next instance output file revision

Get the next revision number for an output file based on asset instance, output type, task type, and name. Used for automatic revision numbering.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_next_instance_output_file_revision200_response import GetNextInstanceOutputFileRevision200Response
from sometech.pykitsu._client.models.get_next_instance_output_file_revision_request import GetNextInstanceOutputFileRevisionRequest
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    asset_instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Asset instance unique identifier
    temporal_entity_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Temporal entity unique identifier
    get_next_instance_output_file_revision_request = sometech.pykitsu._client.GetNextInstanceOutputFileRevisionRequest() # GetNextInstanceOutputFileRevisionRequest | 

    try:
        # Get next instance output file revision
        api_response = await api_instance.get_next_instance_output_file_revision(asset_instance_id, temporal_entity_id, get_next_instance_output_file_revision_request)
        print("The response of FilesApi->get_next_instance_output_file_revision:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_next_instance_output_file_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_instance_id** | **UUID**| Asset instance unique identifier | 
 **temporal_entity_id** | **UUID**| Temporal entity unique identifier | 
 **get_next_instance_output_file_revision_request** | [**GetNextInstanceOutputFileRevisionRequest**](GetNextInstanceOutputFileRevisionRequest.md)|  | 

### Return type

[**GetNextInstanceOutputFileRevision200Response**](GetNextInstanceOutputFileRevision200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Next revision number for the instance output file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_output_files**
> List[GetProjectOutputFiles200ResponseInner] get_project_output_files(project_id, output_type_id=output_type_id, task_type_id=task_type_id, file_status_id=file_status_id, representation=representation, name=name)

Get project output files

Retrieve all output files for a given project with optional filtering by output type, task type, representation, file status, and name.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_output_files200_response_inner import GetProjectOutputFiles200ResponseInner
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    output_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Filter by output type (optional)
    task_type_id = UUID('c46c8gc6-eg97-6887-c292-79675204e47') # UUID | Filter by task type (optional)
    file_status_id = UUID('d57d9hd7-fh08-7998-d403-80786315f58') # UUID | Filter by file status (optional)
    representation = 'cache' # str | Filter by representation (optional)
    name = 'main' # str | Filter by file name (optional)

    try:
        # Get project output files
        api_response = await api_instance.get_project_output_files(project_id, output_type_id=output_type_id, task_type_id=task_type_id, file_status_id=file_status_id, representation=representation, name=name)
        print("The response of FilesApi->get_project_output_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_project_output_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **output_type_id** | **UUID**| Filter by output type | [optional] 
 **task_type_id** | **UUID**| Filter by task type | [optional] 
 **file_status_id** | **UUID**| Filter by file status | [optional] 
 **representation** | **str**| Filter by representation | [optional] 
 **name** | **str**| Filter by file name | [optional] 

### Return type

[**List[GetProjectOutputFiles200ResponseInner]**](GetProjectOutputFiles200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All output files for the project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_working_files**
> List[WorkingFile] get_task_working_files(task_id)

Get task working files

Retrieve all working file revisions for a given task. Returns complete list of working files with their revisions.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.working_file import WorkingFile
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Task unique identifier

    try:
        # Get task working files
        api_response = await api_instance.get_task_working_files(task_id)
        print("The response of FilesApi->get_task_working_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_task_working_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Task unique identifier | 

### Return type

[**List[WorkingFile]**](WorkingFile.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All working file revisions for given task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guess_file_tree_template**
> GuessFileTreeTemplate200Response guess_file_tree_template(guess_file_tree_template_request)

Guess file tree template

Get list of possible project file tree templates matching a file path and data ids corresponding to template tokens.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.guess_file_tree_template200_response import GuessFileTreeTemplate200Response
from sometech.pykitsu._client.models.guess_file_tree_template_request import GuessFileTreeTemplateRequest
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    guess_file_tree_template_request = sometech.pykitsu._client.GuessFileTreeTemplateRequest() # GuessFileTreeTemplateRequest | 

    try:
        # Guess file tree template
        api_response = await api_instance.guess_file_tree_template(guess_file_tree_template_request)
        print("The response of FilesApi->guess_file_tree_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->guess_file_tree_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guess_file_tree_template_request** | [**GuessFileTreeTemplateRequest**](GuessFileTreeTemplateRequest.md)|  | 

### Return type

[**GuessFileTreeTemplate200Response**](GuessFileTreeTemplate200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of possible project file tree templates matching the file path |  -  |
**400** | Invalid project ID or file path |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_file_tree**
> SetProjectFileTree200Response set_project_file_tree(project_id, set_project_file_tree_request)

Set project file tree

Define a template file to use for a given project. Template files are located on the server side and each template has a name for selection.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.set_project_file_tree200_response import SetProjectFileTree200Response
from sometech.pykitsu._client.models.set_project_file_tree_request import SetProjectFileTreeRequest
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    set_project_file_tree_request = sometech.pykitsu._client.SetProjectFileTreeRequest() # SetProjectFileTreeRequest | 

    try:
        # Set project file tree
        api_response = await api_instance.set_project_file_tree(project_id, set_project_file_tree_request)
        print("The response of FilesApi->set_project_file_tree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->set_project_file_tree: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **set_project_file_tree_request** | [**SetProjectFileTreeRequest**](SetProjectFileTreeRequest.md)|  | 

### Return type

[**SetProjectFileTree200Response**](SetProjectFileTree200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File tree template set successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_working_file**
> StoreWorkingFile201Response store_working_file(working_file_id, file)

Store working file

Store a working file in the file storage system. Uploads the file content and associates it with the working file record.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.store_working_file201_response import StoreWorkingFile201Response
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    working_file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Working file unique identifier
    file = None # bytes | Working file to upload

    try:
        # Store working file
        api_response = await api_instance.store_working_file(working_file_id, file)
        print("The response of FilesApi->store_working_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->store_working_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working_file_id** | **UUID**| Working file unique identifier | 
 **file** | **bytes**| Working file to upload | 

### Return type

[**StoreWorkingFile201Response**](StoreWorkingFile201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Working file stored successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_working_file_comment**
> UpdateWorkingFileComment200Response update_working_file_comment(working_file_id, update_working_file_comment_request)

Update working file comment

Update the comment on a specific working file. Comments provide context about changes made to the working file.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.update_working_file_comment200_response import UpdateWorkingFileComment200Response
from sometech.pykitsu._client.models.update_working_file_comment_request import UpdateWorkingFileCommentRequest
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    working_file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Working file unique identifier
    update_working_file_comment_request = sometech.pykitsu._client.UpdateWorkingFileCommentRequest() # UpdateWorkingFileCommentRequest | 

    try:
        # Update working file comment
        api_response = await api_instance.update_working_file_comment(working_file_id, update_working_file_comment_request)
        print("The response of FilesApi->update_working_file_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->update_working_file_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working_file_id** | **UUID**| Working file unique identifier | 
 **update_working_file_comment_request** | [**UpdateWorkingFileCommentRequest**](UpdateWorkingFileCommentRequest.md)|  | 

### Return type

[**UpdateWorkingFileComment200Response**](UpdateWorkingFileComment200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Working file comment updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_working_file_modification_date**
> UpdateWorkingFileModificationDate200Response update_working_file_modification_date(working_file_id)

Update working file modification date

Update the modification date of a working file to the current timestamp. Used to track when the file was last modified.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.update_working_file_modification_date200_response import UpdateWorkingFileModificationDate200Response
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
    api_instance = sometech.pykitsu._client.FilesApi(api_client)
    working_file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Working file unique identifier

    try:
        # Update working file modification date
        api_response = await api_instance.update_working_file_modification_date(working_file_id)
        print("The response of FilesApi->update_working_file_modification_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->update_working_file_modification_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **working_file_id** | **UUID**| Working file unique identifier | 

### Return type

[**UpdateWorkingFileModificationDate200Response**](UpdateWorkingFileModificationDate200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Working file modification date updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

