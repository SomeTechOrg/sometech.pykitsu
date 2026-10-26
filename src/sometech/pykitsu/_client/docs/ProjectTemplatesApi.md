# sometech.pykitsu._client.ProjectTemplatesApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_a_project_template_to_an_existing_project_admin_only**](ProjectTemplatesApi.md#apply_a_project_template_to_an_existing_project_admin_only) | **POST** /data/projects/{project_id}/apply-template/{template_id} | Apply a project template to an existing project. Admin only.
[**attach_a_preview_background_file_to_a_project_template**](ProjectTemplatesApi.md#attach_a_preview_background_file_to_a_project_template) | **POST** /data/project-templates/{template_id}/preview-background-files | Attach a preview background file to a project template.
[**attach_a_status_automation_to_a_project_template**](ProjectTemplatesApi.md#attach_a_status_automation_to_a_project_template) | **POST** /data/project-templates/{template_id}/status-automations | Attach a status automation to a project template.
[**attach_a_task_status_to_a_project_template**](ProjectTemplatesApi.md#attach_a_task_status_to_a_project_template) | **POST** /data/project-templates/{template_id}/task-statuses | Attach a task status to a project template.
[**attach_a_task_type_to_a_project_template**](ProjectTemplatesApi.md#attach_a_task_type_to_a_project_template) | **POST** /data/project-templates/{template_id}/task-types | Attach a task type to a project template.
[**attach_an_asset_type_to_a_project_template**](ProjectTemplatesApi.md#attach_an_asset_type_to_a_project_template) | **POST** /data/project-templates/{template_id}/asset-types | Attach an asset type to a project template.
[**create_a_new_project_template_from_an_existing_project_s**](ProjectTemplatesApi.md#create_a_new_project_template_from_an_existing_project_s) | **POST** /data/project-templates/from-project/{project_id} | Create a new project template from an existing project&#39;s
[**detach_a_preview_background_file_from_a_project_template**](ProjectTemplatesApi.md#detach_a_preview_background_file_from_a_project_template) | **DELETE** /data/project-templates/{template_id}/preview-background-files/{preview_background_file_id} | Detach a preview background file from a project template.
[**detach_a_status_automation_from_a_project_template**](ProjectTemplatesApi.md#detach_a_status_automation_from_a_project_template) | **DELETE** /data/project-templates/{template_id}/status-automations/{status_automation_id} | Detach a status automation from a project template.
[**detach_a_task_status_from_a_project_template**](ProjectTemplatesApi.md#detach_a_task_status_from_a_project_template) | **DELETE** /data/project-templates/{template_id}/task-statuses/{task_status_id} | Detach a task status from a project template.
[**detach_a_task_type_from_a_project_template**](ProjectTemplatesApi.md#detach_a_task_type_from_a_project_template) | **DELETE** /data/project-templates/{template_id}/task-types/{task_type_id} | Detach a task type from a project template.
[**detach_an_asset_type_from_a_project_template**](ProjectTemplatesApi.md#detach_an_asset_type_from_a_project_template) | **DELETE** /data/project-templates/{template_id}/asset-types/{asset_type_id} | Detach an asset type from a project template.
[**list_asset_types_attached_to_a_project_template**](ProjectTemplatesApi.md#list_asset_types_attached_to_a_project_template) | **GET** /data/project-templates/{template_id}/asset-types | List asset types attached to a project template.
[**list_preview_background_files_attached_to_a_project_template**](ProjectTemplatesApi.md#list_preview_background_files_attached_to_a_project_template) | **GET** /data/project-templates/{template_id}/preview-background-files | List preview background files attached to a project template.
[**list_status_automations_attached_to_a_project_template**](ProjectTemplatesApi.md#list_status_automations_attached_to_a_project_template) | **GET** /data/project-templates/{template_id}/status-automations | List status automations attached to a project template.
[**list_task_statuses_attached_to_a_project_template**](ProjectTemplatesApi.md#list_task_statuses_attached_to_a_project_template) | **GET** /data/project-templates/{template_id}/task-statuses | List task statuses attached to a project template.
[**list_task_types_attached_to_a_project_template**](ProjectTemplatesApi.md#list_task_types_attached_to_a_project_template) | **GET** /data/project-templates/{template_id}/task-types | List task types attached to a project template.
[**replace_the_jsonb_metadata_descriptors_snapshot_on_a_project**](ProjectTemplatesApi.md#replace_the_jsonb_metadata_descriptors_snapshot_on_a_project) | **PUT** /data/project-templates/{template_id}/metadata-descriptors | Replace the JSONB metadata descriptors snapshot on a project
[**set_the_default_preview_background_file_for_a_project_template**](ProjectTemplatesApi.md#set_the_default_preview_background_file_for_a_project_template) | **PUT** /data/project-templates/{template_id}/default-preview-background-file | Set the default preview background file for a project template.


# **apply_a_project_template_to_an_existing_project_admin_only**
> apply_a_project_template_to_an_existing_project_admin_only(project_id, template_id)

Apply a project template to an existing project. Admin only.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    project_id = 'project_id_example' # str | 
    template_id = 'template_id_example' # str | 

    try:
        # Apply a project template to an existing project. Admin only.
        await api_instance.apply_a_project_template_to_an_existing_project_admin_only(project_id, template_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->apply_a_project_template_to_an_existing_project_admin_only: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **template_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_a_preview_background_file_to_a_project_template**
> attach_a_preview_background_file_to_a_project_template(template_id)

Attach a preview background file to a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # Attach a preview background file to a project template.
        await api_instance.attach_a_preview_background_file_to_a_project_template(template_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->attach_a_preview_background_file_to_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_a_status_automation_to_a_project_template**
> attach_a_status_automation_to_a_project_template(template_id)

Attach a status automation to a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # Attach a status automation to a project template.
        await api_instance.attach_a_status_automation_to_a_project_template(template_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->attach_a_status_automation_to_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_a_task_status_to_a_project_template**
> attach_a_task_status_to_a_project_template(template_id)

Attach a task status to a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # Attach a task status to a project template.
        await api_instance.attach_a_task_status_to_a_project_template(template_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->attach_a_task_status_to_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_a_task_type_to_a_project_template**
> attach_a_task_type_to_a_project_template(template_id)

Attach a task type to a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # Attach a task type to a project template.
        await api_instance.attach_a_task_type_to_a_project_template(template_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->attach_a_task_type_to_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_an_asset_type_to_a_project_template**
> attach_an_asset_type_to_a_project_template(template_id)

Attach an asset type to a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # Attach an asset type to a project template.
        await api_instance.attach_an_asset_type_to_a_project_template(template_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->attach_an_asset_type_to_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_a_new_project_template_from_an_existing_project_s**
> create_a_new_project_template_from_an_existing_project_s(project_id)

Create a new project template from an existing project's

configuration. Admin only.<br/>

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Create a new project template from an existing project's
        await api_instance.create_a_new_project_template_from_an_existing_project_s(project_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->create_a_new_project_template_from_an_existing_project_s: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_a_preview_background_file_from_a_project_template**
> detach_a_preview_background_file_from_a_project_template(template_id, preview_background_file_id)

Detach a preview background file from a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 
    preview_background_file_id = 'preview_background_file_id_example' # str | 

    try:
        # Detach a preview background file from a project template.
        await api_instance.detach_a_preview_background_file_from_a_project_template(template_id, preview_background_file_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->detach_a_preview_background_file_from_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **preview_background_file_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_a_status_automation_from_a_project_template**
> detach_a_status_automation_from_a_project_template(template_id, status_automation_id)

Detach a status automation from a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 
    status_automation_id = 'status_automation_id_example' # str | 

    try:
        # Detach a status automation from a project template.
        await api_instance.detach_a_status_automation_from_a_project_template(template_id, status_automation_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->detach_a_status_automation_from_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **status_automation_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_a_task_status_from_a_project_template**
> detach_a_task_status_from_a_project_template(template_id, task_status_id)

Detach a task status from a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 
    task_status_id = 'task_status_id_example' # str | 

    try:
        # Detach a task status from a project template.
        await api_instance.detach_a_task_status_from_a_project_template(template_id, task_status_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->detach_a_task_status_from_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **task_status_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_a_task_type_from_a_project_template**
> detach_a_task_type_from_a_project_template(template_id, task_type_id)

Detach a task type from a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 
    task_type_id = 'task_type_id_example' # str | 

    try:
        # Detach a task type from a project template.
        await api_instance.detach_a_task_type_from_a_project_template(template_id, task_type_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->detach_a_task_type_from_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **task_type_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_an_asset_type_from_a_project_template**
> detach_an_asset_type_from_a_project_template(template_id, asset_type_id)

Detach an asset type from a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 
    asset_type_id = 'asset_type_id_example' # str | 

    try:
        # Detach an asset type from a project template.
        await api_instance.detach_an_asset_type_from_a_project_template(template_id, asset_type_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->detach_an_asset_type_from_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **asset_type_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_asset_types_attached_to_a_project_template**
> list_asset_types_attached_to_a_project_template(template_id)

List asset types attached to a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # List asset types attached to a project template.
        await api_instance.list_asset_types_attached_to_a_project_template(template_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->list_asset_types_attached_to_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_preview_background_files_attached_to_a_project_template**
> list_preview_background_files_attached_to_a_project_template(template_id)

List preview background files attached to a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # List preview background files attached to a project template.
        await api_instance.list_preview_background_files_attached_to_a_project_template(template_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->list_preview_background_files_attached_to_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_status_automations_attached_to_a_project_template**
> list_status_automations_attached_to_a_project_template(template_id)

List status automations attached to a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # List status automations attached to a project template.
        await api_instance.list_status_automations_attached_to_a_project_template(template_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->list_status_automations_attached_to_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_task_statuses_attached_to_a_project_template**
> list_task_statuses_attached_to_a_project_template(template_id)

List task statuses attached to a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # List task statuses attached to a project template.
        await api_instance.list_task_statuses_attached_to_a_project_template(template_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->list_task_statuses_attached_to_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_task_types_attached_to_a_project_template**
> list_task_types_attached_to_a_project_template(template_id)

List task types attached to a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # List task types attached to a project template.
        await api_instance.list_task_types_attached_to_a_project_template(template_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->list_task_types_attached_to_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_the_jsonb_metadata_descriptors_snapshot_on_a_project**
> replace_the_jsonb_metadata_descriptors_snapshot_on_a_project(template_id)

Replace the JSONB metadata descriptors snapshot on a project

template. Admin only.<br/>

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # Replace the JSONB metadata descriptors snapshot on a project
        await api_instance.replace_the_jsonb_metadata_descriptors_snapshot_on_a_project(template_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->replace_the_jsonb_metadata_descriptors_snapshot_on_a_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_the_default_preview_background_file_for_a_project_template**
> set_the_default_preview_background_file_for_a_project_template(template_id)

Set the default preview background file for a project template.

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
    api_instance = sometech.pykitsu._client.ProjectTemplatesApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # Set the default preview background file for a project template.
        await api_instance.set_the_default_preview_background_file_for_a_project_template(template_id)
    except Exception as e:
        print("Exception when calling ProjectTemplatesApi->set_the_default_preview_background_file_for_a_project_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

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
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

