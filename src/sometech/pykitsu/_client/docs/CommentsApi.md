# sometech.pykitsu._client.CommentsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_comment**](CommentsApi.md#acknowledge_comment) | **POST** /data/tasks/{task_id}/comments/{comment_id}/ack | Acknowledge comment
[**add_comment_attachments**](CommentsApi.md#add_comment_attachments) | **POST** /actions/tasks/{task_id}/comments/{comment_id}/add-attachment | Add comment attachments
[**add_task_batch_comments**](CommentsApi.md#add_task_batch_comments) | **POST** /actions/tasks/{task_id}/batch-comment | Add task batch comments
[**add_tasks_batch_comments**](CommentsApi.md#add_tasks_batch_comments) | **POST** /actions/tasks/batch-comment | Add tasks batch comments
[**create_multiple_comments**](CommentsApi.md#create_multiple_comments) | **POST** /actions/projects/{project_id}/tasks/comment-many | Create multiple comments
[**create_task_comment**](CommentsApi.md#create_task_comment) | **POST** /actions/tasks/{task_id}/comment | Create task comment
[**delete_comment_attachment**](CommentsApi.md#delete_comment_attachment) | **DELETE** /data/tasks/{task_id}/comments/{comment_id}/attachments/{attachment_id} | Delete comment attachment
[**delete_comment_reply**](CommentsApi.md#delete_comment_reply) | **DELETE** /data/tasks/{task_id}/comments/{comment_id}/reply/{reply_id} | Delete comment reply
[**download_attachment_file_get_data_attachment_files_attachment_file_id_file_file_name**](CommentsApi.md#download_attachment_file_get_data_attachment_files_attachment_file_id_file_file_name) | **GET** /data/attachment-files/{attachment_file_id}/file/{file_name} | Download attachment file
[**get_project_attachment_files**](CommentsApi.md#get_project_attachment_files) | **GET** /data/projects/{project_id}/attachment-files | Get project attachment files
[**get_task_attachment_files**](CommentsApi.md#get_task_attachment_files) | **GET** /data/tasks/{task_id}/attachment-files | Get task attachment files
[**reply_to_comment**](CommentsApi.md#reply_to_comment) | **POST** /data/tasks/{task_id}/comments/{comment_id}/reply | Reply to comment


# **acknowledge_comment**
> AcknowledgeComment200Response acknowledge_comment(task_id, comment_id)

Acknowledge comment

Acknowledge a specific comment. If it's already acknowledged, remove the acknowledgement.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.acknowledge_comment200_response import AcknowledgeComment200Response
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
    api_instance = sometech.pykitsu._client.CommentsApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the task
    comment_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Unique identifier of the comment

    try:
        # Acknowledge comment
        api_response = await api_instance.acknowledge_comment(task_id, comment_id)
        print("The response of CommentsApi->acknowledge_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->acknowledge_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Unique identifier of the task | 
 **comment_id** | **UUID**| Unique identifier of the comment | 

### Return type

[**AcknowledgeComment200Response**](AcknowledgeComment200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comment acknowledgement status successfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_comment_attachments**
> List[AddCommentAttachments201ResponseInner] add_comment_attachments(task_id, comment_id, files, reply_id=reply_id)

Add comment attachments

Add one or more files as attachments to a specific comment. Supports various file types including images and documents.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_comment_attachments201_response_inner import AddCommentAttachments201ResponseInner
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
    api_instance = sometech.pykitsu._client.CommentsApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the task
    comment_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Unique identifier of the comment
    files = None # bytes | Files to attach to the comment
    reply_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Reply identifier (optional) (optional)

    try:
        # Add comment attachments
        api_response = await api_instance.add_comment_attachments(task_id, comment_id, files, reply_id=reply_id)
        print("The response of CommentsApi->add_comment_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->add_comment_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Unique identifier of the task | 
 **comment_id** | **UUID**| Unique identifier of the comment | 
 **files** | **bytes**| Files to attach to the comment | 
 **reply_id** | **UUID**| Reply identifier (optional) | [optional] 

### Return type

[**List[AddCommentAttachments201ResponseInner]**](AddCommentAttachments201ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Files successfully added as attachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_task_batch_comments**
> List[object] add_task_batch_comments(task_id, comments)

Add task batch comments

Creates new comments for given task. Each comment requires a text, a task_status and a person as arguments. Can include preview files and attachments.

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
    api_instance = sometech.pykitsu._client.CommentsApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Task unique identifier
    comments = 'comments_example' # str | JSON string containing array of comments

    try:
        # Add task batch comments
        api_response = await api_instance.add_task_batch_comments(task_id, comments)
        print("The response of CommentsApi->add_task_batch_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->add_task_batch_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Task unique identifier | 
 **comments** | **str**| JSON string containing array of comments | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | New comments created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tasks_batch_comments**
> List[object] add_tasks_batch_comments(comments)

Add tasks batch comments

Creates new comments for given tasks. Each comment requires a task_id, text, a task_status and a person as arguments. Can include preview files and attachments.

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
    api_instance = sometech.pykitsu._client.CommentsApi(api_client)
    comments = 'comments_example' # str | JSON string containing array of comments

    try:
        # Add tasks batch comments
        api_response = await api_instance.add_tasks_batch_comments(comments)
        print("The response of CommentsApi->add_tasks_batch_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->add_tasks_batch_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments** | **str**| JSON string containing array of comments | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | New comments created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple_comments**
> List[CreateMultipleComments201ResponseInner] create_multiple_comments(project_id, create_multiple_comments_request_inner)

Create multiple comments

Create several comments at once for a specific project. Each comment requires a text, a task id, a task_status and a person as arguments. This way, comments keep history of status changes. When the comment is created, it updates the task status with the given task status.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_multiple_comments201_response_inner import CreateMultipleComments201ResponseInner
from sometech.pykitsu._client.models.create_multiple_comments_request_inner import CreateMultipleCommentsRequestInner
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
    api_instance = sometech.pykitsu._client.CommentsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    create_multiple_comments_request_inner = [sometech.pykitsu._client.CreateMultipleCommentsRequestInner()] # List[CreateMultipleCommentsRequestInner] | 

    try:
        # Create multiple comments
        api_response = await api_instance.create_multiple_comments(project_id, create_multiple_comments_request_inner)
        print("The response of CommentsApi->create_multiple_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->create_multiple_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **create_multiple_comments_request_inner** | [**List[CreateMultipleCommentsRequestInner]**](CreateMultipleCommentsRequestInner.md)|  | 

### Return type

[**List[CreateMultipleComments201ResponseInner]**](CreateMultipleComments201ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comments successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task_comment**
> CreateTaskComment201Response create_task_comment(task_id, create_task_comment_request)

Create task comment

Create a new comment for a specific task. It requires a text, a task_status and a person as arguments. This way, comments keep history of status changes. When the comment is created, it updates the task status with the given task status.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_task_comment201_response import CreateTaskComment201Response
from sometech.pykitsu._client.models.create_task_comment_request import CreateTaskCommentRequest
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
    api_instance = sometech.pykitsu._client.CommentsApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the task
    create_task_comment_request = sometech.pykitsu._client.CreateTaskCommentRequest() # CreateTaskCommentRequest | 

    try:
        # Create task comment
        api_response = await api_instance.create_task_comment(task_id, create_task_comment_request)
        print("The response of CommentsApi->create_task_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->create_task_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Unique identifier of the task | 
 **create_task_comment_request** | [**CreateTaskCommentRequest**](CreateTaskCommentRequest.md)|  | 

### Return type

[**CreateTaskComment201Response**](CreateTaskComment201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comment successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment_attachment**
> delete_comment_attachment(task_id, comment_id, attachment_id)

Delete comment attachment

Delete a specific attachment file linked to a comment. Only the comment author or project managers can delete attachments.

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
    api_instance = sometech.pykitsu._client.CommentsApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the task
    comment_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Unique identifier of the comment
    attachment_id = UUID('c46c8gc6-eg97-6887-c292-79675204e47') # UUID | Unique identifier of the attachment

    try:
        # Delete comment attachment
        await api_instance.delete_comment_attachment(task_id, comment_id, attachment_id)
    except Exception as e:
        print("Exception when calling CommentsApi->delete_comment_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Unique identifier of the task | 
 **comment_id** | **UUID**| Unique identifier of the comment | 
 **attachment_id** | **UUID**| Unique identifier of the attachment | 

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
**204** | Attachment successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment_reply**
> delete_comment_reply(task_id, comment_id, reply_id)

Delete comment reply

Delete a specific reply from a comment. Only the reply author or administrators can delete replies.

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
    api_instance = sometech.pykitsu._client.CommentsApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the task
    comment_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Unique identifier of the comment
    reply_id = UUID('c46c8gc6-eg97-6887-c292-79675204e47') # UUID | Unique identifier of the reply

    try:
        # Delete comment reply
        await api_instance.delete_comment_reply(task_id, comment_id, reply_id)
    except Exception as e:
        print("Exception when calling CommentsApi->delete_comment_reply: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Unique identifier of the task | 
 **comment_id** | **UUID**| Unique identifier of the comment | 
 **reply_id** | **UUID**| Unique identifier of the reply | 

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
**200** | Reply successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_attachment_file_get_data_attachment_files_attachment_file_id_file_file_name**
> bytes download_attachment_file_get_data_attachment_files_attachment_file_id_file_file_name(attachment_file_id, file_name)

Download attachment file

Download a specific attachment file from a comment or chat message. Supports various file types including images and documents.

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
    api_instance = sometech.pykitsu._client.CommentsApi(api_client)
    attachment_file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the attachment file
    file_name = 'document.pdf' # str | Name of the file to download

    try:
        # Download attachment file
        api_response = await api_instance.download_attachment_file_get_data_attachment_files_attachment_file_id_file_file_name(attachment_file_id, file_name)
        print("The response of CommentsApi->download_attachment_file_get_data_attachment_files_attachment_file_id_file_file_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->download_attachment_file_get_data_attachment_files_attachment_file_id_file_file_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_file_id** | **UUID**| Unique identifier of the attachment file | 
 **file_name** | **str**| Name of the file to download | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment file successfully downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_attachment_files**
> List[AttachmentFile] get_project_attachment_files(project_id)

Get project attachment files

Retrieve all attachment files related to a specific project. Requires administrator permissions.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.attachment_file import AttachmentFile
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
    api_instance = sometech.pykitsu._client.CommentsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project

    try:
        # Get project attachment files
        api_response = await api_instance.get_project_attachment_files(project_id)
        print("The response of CommentsApi->get_project_attachment_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->get_project_attachment_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 

### Return type

[**List[AttachmentFile]**](AttachmentFile.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project attachment files successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_attachment_files**
> List[GetTaskAttachmentFiles200ResponseInner] get_task_attachment_files(task_id)

Get task attachment files

Retrieve all attachment files related to a specific task. Requires administrator permissions.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_task_attachment_files200_response_inner import GetTaskAttachmentFiles200ResponseInner
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
    api_instance = sometech.pykitsu._client.CommentsApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the task

    try:
        # Get task attachment files
        api_response = await api_instance.get_task_attachment_files(task_id)
        print("The response of CommentsApi->get_task_attachment_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->get_task_attachment_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Unique identifier of the task | 

### Return type

[**List[GetTaskAttachmentFiles200ResponseInner]**](GetTaskAttachmentFiles200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task attachment files successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reply_to_comment**
> ReplyToComment200Response reply_to_comment(task_id, comment_id, text=text)

Reply to comment

Add a reply to a specific comment. The reply will be added to the comment's replies list.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.reply_to_comment200_response import ReplyToComment200Response
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
    api_instance = sometech.pykitsu._client.CommentsApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the task
    comment_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Unique identifier of the comment
    text = 'text_example' # str | Reply text content (optional)

    try:
        # Reply to comment
        api_response = await api_instance.reply_to_comment(task_id, comment_id, text=text)
        print("The response of CommentsApi->reply_to_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->reply_to_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Unique identifier of the task | 
 **comment_id** | **UUID**| Unique identifier of the comment | 
 **text** | **str**| Reply text content | [optional] 

### Return type

[**ReplyToComment200Response**](ReplyToComment200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reply successfully added to comment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

