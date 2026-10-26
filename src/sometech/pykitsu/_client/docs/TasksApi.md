# sometech.pykitsu._client.TasksApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_preview_to_comment**](TasksApi.md#add_preview_to_comment) | **POST** /actions/tasks/{task_id}/comments/{comment_id}/preview-files/{preview_file_id} | Add preview to comment
[**add_task_preview**](TasksApi.md#add_task_preview) | **POST** /actions/tasks/{task_id}/comments/{comment_id}/add-preview | Add task preview
[**add_time_spent**](TasksApi.md#add_time_spent) | **POST** /actions/tasks/{task_id}/time-spents/{date}/persons/{person_id}/add | Add time spent
[**assign_task_to_person**](TasksApi.md#assign_task_to_person) | **PUT** /actions/tasks/{task_id}/assign | Assign task to person
[**assign_tasks_to_person**](TasksApi.md#assign_tasks_to_person) | **PUT** /actions/persons/{person_id}/assign | Assign tasks to person
[**clear_task_assignations**](TasksApi.md#clear_task_assignations) | **PUT** /actions/tasks/clear-assignation | Clear task assignations
[**create_asset_tasks**](TasksApi.md#create_asset_tasks) | **POST** /actions/projects/{project_id}/task-types/{task_type_id}/assets/create-tasks | Create asset tasks
[**create_concept_tasks**](TasksApi.md#create_concept_tasks) | **POST** /actions/projects/{project_id}/task-types/{task_type_id}/concepts/create-tasks | Create concept tasks
[**create_edit_tasks**](TasksApi.md#create_edit_tasks) | **POST** /actions/projects/{project_id}/task-types/{task_type_id}/edits/create-tasks | Create edit tasks
[**create_entity_tasks**](TasksApi.md#create_entity_tasks) | **POST** /actions/projects/{project_id}/task-types/{task_type_id}/create-tasks/{entity_type}/ | Create entity tasks
[**create_shot_tasks**](TasksApi.md#create_shot_tasks) | **POST** /actions/projects/{project_id}/task-types/{task_type_id}/shots/create-tasks | Create shot tasks
[**delete_comment_delete_data_tasks_task_id_comments_comment_id**](TasksApi.md#delete_comment_delete_data_tasks_task_id_comments_comment_id) | **DELETE** /data/tasks/{task_id}/comments/{comment_id} | Delete comment
[**delete_preview_from_comment**](TasksApi.md#delete_preview_from_comment) | **DELETE** /actions/tasks/{task_id}/comments/{comment_id}/preview-files/{preview_file_id} | Delete preview from comment
[**delete_tasks_batch**](TasksApi.md#delete_tasks_batch) | **POST** /actions/projects/{project_id}/delete-tasks | Delete tasks batch
[**delete_tasks_for_type**](TasksApi.md#delete_tasks_for_type) | **DELETE** /actions/projects/{project_id}/task-types/{task_type_id}/delete-tasks | Delete tasks for type
[**delete_time_spent_delete_actions_tasks_task_id_time_spents_date_persons_person_id**](TasksApi.md#delete_time_spent_delete_actions_tasks_task_id_time_spents_date_persons_person_id) | **DELETE** /actions/tasks/{task_id}/time-spents/{date}/persons/{person_id} | Delete time spent
[**get_comment_get_data_tasks_task_id_comments_comment_id**](TasksApi.md#get_comment_get_data_tasks_task_id_comments_comment_id) | **GET** /data/tasks/{task_id}/comments/{comment_id} | Get comment
[**get_open_tasks**](TasksApi.md#get_open_tasks) | **GET** /data/tasks/open-tasks | Get open tasks
[**get_open_tasks_stats**](TasksApi.md#get_open_tasks_stats) | **GET** /data/tasks/open-tasks/stats | Get open tasks stats
[**get_person_done_tasks**](TasksApi.md#get_person_done_tasks) | **GET** /data/persons/{person_id}/done-tasks | Get person done tasks
[**get_person_open_tasks**](TasksApi.md#get_person_open_tasks) | **GET** /data/persons/{person_id}/tasks | Get person open tasks
[**get_person_tasks_for_type**](TasksApi.md#get_person_tasks_for_type) | **GET** /data/persons/{person_id}/related-tasks/{task_type_id} | Get person tasks for type
[**get_persons_tasks_dates**](TasksApi.md#get_persons_tasks_dates) | **GET** /data/persons/task-dates | Get persons tasks dates
[**get_project_comments**](TasksApi.md#get_project_comments) | **GET** /data/projects/{project_id}/comments | Get project comments
[**get_project_notifications**](TasksApi.md#get_project_notifications) | **GET** /data/projects/{project_id}/notifications | Get project notifications
[**get_project_preview_files**](TasksApi.md#get_project_preview_files) | **GET** /data/projects/{project_id}/preview-files | Get project preview files
[**get_project_subscriptions**](TasksApi.md#get_project_subscriptions) | **GET** /data/projects/{project_id}/subscriptions | Get project subscriptions
[**get_project_tasks**](TasksApi.md#get_project_tasks) | **GET** /data/projects/{project_id}/tasks | Get project tasks
[**get_task_comments**](TasksApi.md#get_task_comments) | **GET** /data/tasks/{task_id}/comments | Get task comments
[**get_task_full**](TasksApi.md#get_task_full) | **GET** /data/tasks/{task_id}/full | Get task full
[**get_task_previews**](TasksApi.md#get_task_previews) | **GET** /data/tasks/{task_id}/previews | Get task previews
[**get_task_time_spent_for_date**](TasksApi.md#get_task_time_spent_for_date) | **GET** /actions/tasks/{task_id}/time-spents/{date} | Get task time spent for date
[**get_task_time_spent_get_actions_tasks_task_id_time_spents**](TasksApi.md#get_task_time_spent_get_actions_tasks_task_id_time_spents) | **GET** /actions/tasks/{task_id}/time-spents | Get task time spent
[**get_tasks_for_entity_and_type**](TasksApi.md#get_tasks_for_entity_and_type) | **GET** /data/entities/{entity_id}/task-types/{task_type_id}/tasks | Get tasks for entity and type
[**set_main_preview_from_task**](TasksApi.md#set_main_preview_from_task) | **PUT** /actions/tasks/{task_id}/set-main-preview | Set main preview from task
[**set_task_to_review**](TasksApi.md#set_task_to_review) | **PUT** /actions/tasks/{task_id}/to-review | Set task to review
[**set_time_spent**](TasksApi.md#set_time_spent) | **POST** /actions/tasks/{task_id}/time-spents/{date}/persons/{person_id} | Set time spent


# **add_preview_to_comment**
> AddPreviewToComment201Response add_preview_to_comment(task_id, comment_id, preview_file_id, file=file)

Add preview to comment

Add a preview to a comment by uploading a file in multipart form data.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_preview_to_comment201_response import AddPreviewToComment201Response
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    comment_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    preview_file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    file = None # bytes | Preview file to upload (optional)

    try:
        # Add preview to comment
        api_response = await api_instance.add_preview_to_comment(task_id, comment_id, preview_file_id, file=file)
        print("The response of TasksApi->add_preview_to_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->add_preview_to_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 
 **comment_id** | **UUID**|  | 
 **preview_file_id** | **UUID**|  | 
 **file** | **bytes**| Preview file to upload | [optional] 

### Return type

[**AddPreviewToComment201Response**](AddPreviewToComment201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Preview added to comment |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_task_preview**
> AddTaskPreview201Response add_task_preview(task_id, comment_id, add_task_preview_request)

Add task preview

Add preview metadata to a task. The preview file is uploaded after. Revision is auto set to last + 1. It can also be set manually.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_task_preview201_response import AddTaskPreview201Response
from sometech.pykitsu._client.models.add_task_preview_request import AddTaskPreviewRequest
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    comment_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    add_task_preview_request = sometech.pykitsu._client.AddTaskPreviewRequest() # AddTaskPreviewRequest | 

    try:
        # Add task preview
        api_response = await api_instance.add_task_preview(task_id, comment_id, add_task_preview_request)
        print("The response of TasksApi->add_task_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->add_task_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 
 **comment_id** | **UUID**|  | 
 **add_task_preview_request** | [**AddTaskPreviewRequest**](AddTaskPreviewRequest.md)|  | 

### Return type

[**AddTaskPreview201Response**](AddTaskPreview201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Preview metadata added to task |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_time_spent**
> TimeSpent add_time_spent(task_id, var_date, person_id, add_time_spent_request)

Add time spent

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_time_spent_request import AddTimeSpentRequest
from sometech.pykitsu._client.models.time_spent import TimeSpent
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    var_date = '2022-07-12' # date | 
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    add_time_spent_request = sometech.pykitsu._client.AddTimeSpentRequest() # AddTimeSpentRequest | 

    try:
        # Add time spent
        api_response = await api_instance.add_time_spent(task_id, var_date, person_id, add_time_spent_request)
        print("The response of TasksApi->add_time_spent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->add_time_spent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 
 **var_date** | **date**|  | 
 **person_id** | **UUID**|  | 
 **add_time_spent_request** | [**AddTimeSpentRequest**](AddTimeSpentRequest.md)|  | 

### Return type

[**TimeSpent**](TimeSpent.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Timeframe added to time spent |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_task_to_person**
> Task assign_task_to_person(task_id, assign_task_to_person_request)

Assign task to person

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.assign_task_to_person_request import AssignTaskToPersonRequest
from sometech.pykitsu._client.models.task import Task
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    assign_task_to_person_request = sometech.pykitsu._client.AssignTaskToPersonRequest() # AssignTaskToPersonRequest | 

    try:
        # Assign task to person
        api_response = await api_instance.assign_task_to_person(task_id, assign_task_to_person_request)
        print("The response of TasksApi->assign_task_to_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->assign_task_to_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 
 **assign_task_to_person_request** | [**AssignTaskToPersonRequest**](AssignTaskToPersonRequest.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task assigned to person |  -  |
**400** | Assignee does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_tasks_to_person**
> List[Task] assign_tasks_to_person(person_id, assign_tasks_to_person_request)

Assign tasks to person

Assign a list of tasks to a person. Unknown task ids are ignored.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.assign_tasks_to_person_request import AssignTasksToPersonRequest
from sometech.pykitsu._client.models.task import Task
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    assign_tasks_to_person_request = sometech.pykitsu._client.AssignTasksToPersonRequest() # AssignTasksToPersonRequest | 

    try:
        # Assign tasks to person
        api_response = await api_instance.assign_tasks_to_person(person_id, assign_tasks_to_person_request)
        print("The response of TasksApi->assign_tasks_to_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->assign_tasks_to_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**|  | 
 **assign_tasks_to_person_request** | [**AssignTasksToPersonRequest**](AssignTasksToPersonRequest.md)|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tasks assigned to person |  -  |
**400** | Assignee does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_task_assignations**
> List[UUID] clear_task_assignations(clear_task_assignations_request)

Clear task assignations

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.clear_task_assignations_request import ClearTaskAssignationsRequest
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    clear_task_assignations_request = sometech.pykitsu._client.ClearTaskAssignationsRequest() # ClearTaskAssignationsRequest | 

    try:
        # Clear task assignations
        api_response = await api_instance.clear_task_assignations(clear_task_assignations_request)
        print("The response of TasksApi->clear_task_assignations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->clear_task_assignations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clear_task_assignations_request** | [**ClearTaskAssignationsRequest**](ClearTaskAssignationsRequest.md)|  | 

### Return type

**List[UUID]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assignations removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_tasks**
> List[Task] create_asset_tasks(project_id, task_type_id, request_body)

Create asset tasks

Create tasks for assets. Provide a list of asset IDs in the JSON body, or omit for all assets in the project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.task import Task
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    request_body = ["b24a6ea4-ce75-4665-a070-57453082c25"] # List[UUID] | 

    try:
        # Create asset tasks
        api_response = await api_instance.create_asset_tasks(project_id, task_type_id, request_body)
        print("The response of TasksApi->create_asset_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->create_asset_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **task_type_id** | **UUID**|  | 
 **request_body** | [**List[UUID]**](UUID.md)|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tasks created for assets |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_concept_tasks**
> List[Task] create_concept_tasks(project_id, task_type_id, request_body)

Create concept tasks

Create tasks for concepts. Provide a list of concept IDs in the JSON body, or omit for all concepts in the project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.task import Task
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    request_body = ["b24a6ea4-ce75-4665-a070-57453082c25"] # List[UUID] | 

    try:
        # Create concept tasks
        api_response = await api_instance.create_concept_tasks(project_id, task_type_id, request_body)
        print("The response of TasksApi->create_concept_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->create_concept_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **task_type_id** | **UUID**|  | 
 **request_body** | [**List[UUID]**](UUID.md)|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tasks created for concepts |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_edit_tasks**
> List[Task] create_edit_tasks(project_id, task_type_id, request_body)

Create edit tasks

Create tasks for edits. Provide a list of edit IDs in the JSON body, or omit for all edits in the project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.task import Task
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    request_body = ["b24a6ea4-ce75-4665-a070-57453082c25"] # List[UUID] | 

    try:
        # Create edit tasks
        api_response = await api_instance.create_edit_tasks(project_id, task_type_id, request_body)
        print("The response of TasksApi->create_edit_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->create_edit_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **task_type_id** | **UUID**|  | 
 **request_body** | [**List[UUID]**](UUID.md)|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tasks created for edits |  -  |
**400** | Wrong criterions format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entity_tasks**
> List[Task] create_entity_tasks(project_id, entity_type, task_type_id, request_body)

Create entity tasks

Create tasks for entities of a given type. Provide entity IDs in the JSON body, or omit for all entities in the project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.task import Task
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    entity_type = 'Asset' # str | Entity type name (Asset, Sequence, etc.)
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    request_body = ["b24a6ea4-ce75-4665-a070-57453082c25"] # List[UUID] | 

    try:
        # Create entity tasks
        api_response = await api_instance.create_entity_tasks(project_id, entity_type, task_type_id, request_body)
        print("The response of TasksApi->create_entity_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->create_entity_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **entity_type** | **str**| Entity type name (Asset, Sequence, etc.) | 
 **task_type_id** | **UUID**|  | 
 **request_body** | [**List[UUID]**](UUID.md)|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tasks created for entities |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_shot_tasks**
> List[Task] create_shot_tasks(project_id, task_type_id, request_body)

Create shot tasks

Create tasks for shots. Provide a list of shot IDs in the JSON body, or omit for all shots in the project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.task import Task
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    request_body = ["b24a6ea4-ce75-4665-a070-57453082c25"] # List[UUID] | 

    try:
        # Create shot tasks
        api_response = await api_instance.create_shot_tasks(project_id, task_type_id, request_body)
        print("The response of TasksApi->create_shot_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->create_shot_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **task_type_id** | **UUID**|  | 
 **request_body** | [**List[UUID]**](UUID.md)|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tasks created for shots |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment_delete_data_tasks_task_id_comments_comment_id**
> delete_comment_delete_data_tasks_task_id_comments_comment_id(task_id, comment_id)

Delete comment

Delete a comment by id for a task.

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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    comment_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Delete comment
        await api_instance.delete_comment_delete_data_tasks_task_id_comments_comment_id(task_id, comment_id)
    except Exception as e:
        print("Exception when calling TasksApi->delete_comment_delete_data_tasks_task_id_comments_comment_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 
 **comment_id** | **UUID**|  | 

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
**204** | Comment deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_preview_from_comment**
> delete_preview_from_comment(task_id, comment_id, preview_file_id, force=force)

Delete preview from comment

Delete a preview from a comment. Use force query to delete even if there are dependencies.

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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    comment_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    preview_file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    force = False # bool | Force deletion even if preview has dependencies (optional) (default to False)

    try:
        # Delete preview from comment
        await api_instance.delete_preview_from_comment(task_id, comment_id, preview_file_id, force=force)
    except Exception as e:
        print("Exception when calling TasksApi->delete_preview_from_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 
 **comment_id** | **UUID**|  | 
 **preview_file_id** | **UUID**|  | 
 **force** | **bool**| Force deletion even if preview has dependencies | [optional] [default to False]

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
**204** | Preview deleted from comment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tasks_batch**
> List[UUID] delete_tasks_batch(project_id)

Delete tasks batch

Delete tasks given by id list. Useful for batch deletions.

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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Delete tasks batch
        api_response = await api_instance.delete_tasks_batch(project_id)
        print("The response of TasksApi->delete_tasks_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->delete_tasks_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 

### Return type

**List[UUID]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tasks matching id list given in parameter deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tasks_for_type**
> delete_tasks_for_type(project_id, task_type_id)

Delete tasks for type

Delete all tasks for a task type in a project. Useful when tasks were created by mistake at project start.

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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Delete tasks for type
        await api_instance.delete_tasks_for_type(project_id, task_type_id)
    except Exception as e:
        print("Exception when calling TasksApi->delete_tasks_for_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **task_type_id** | **UUID**|  | 

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
**204** | All tasks for given task type and project deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_time_spent_delete_actions_tasks_task_id_time_spents_date_persons_person_id**
> TimeSpent delete_time_spent_delete_actions_tasks_task_id_time_spents_date_persons_person_id(task_id, var_date, person_id)

Delete time spent

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.time_spent import TimeSpent
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    var_date = '2022-07-12' # date | 
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Delete time spent
        api_response = await api_instance.delete_time_spent_delete_actions_tasks_task_id_time_spents_date_persons_person_id(task_id, var_date, person_id)
        print("The response of TasksApi->delete_time_spent_delete_actions_tasks_task_id_time_spents_date_persons_person_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->delete_time_spent_delete_actions_tasks_task_id_time_spents_date_persons_person_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 
 **var_date** | **date**|  | 
 **person_id** | **UUID**|  | 

### Return type

[**TimeSpent**](TimeSpent.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Time spent removed for the person on the task |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment_get_data_tasks_task_id_comments_comment_id**
> GetCommentGetDataTasksTaskIdCommentsCommentId200Response get_comment_get_data_tasks_task_id_comments_comment_id(task_id, comment_id)

Get comment

Get a comment by id for a task.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_comment_get_data_tasks_task_id_comments_comment_id200_response import GetCommentGetDataTasksTaskIdCommentsCommentId200Response
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    comment_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get comment
        api_response = await api_instance.get_comment_get_data_tasks_task_id_comments_comment_id(task_id, comment_id)
        print("The response of TasksApi->get_comment_get_data_tasks_task_id_comments_comment_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_comment_get_data_tasks_task_id_comments_comment_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 
 **comment_id** | **UUID**|  | 

### Return type

[**GetCommentGetDataTasksTaskIdCommentsCommentId200Response**](GetCommentGetDataTasksTaskIdCommentsCommentId200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comment found and returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_tasks**
> GetOpenTasks200Response get_open_tasks(project_id=project_id, task_status_id=task_status_id, task_type_id=task_type_id, person_id=person_id, start_date=start_date, due_date=due_date, priority=priority, page=page, limit=limit)

Get open tasks

Return tasks for open projects with optional filters and pagination. Includes statistics.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_open_tasks200_response import GetOpenTasks200Response
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter tasks on given project ID (optional)
    task_status_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter tasks on given task status ID (optional)
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter tasks on given task type ID (optional)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter tasks on given person ID (optional)
    start_date = '2022-07-12' # date | Filter tasks posterior to given start date (optional)
    due_date = '2022-07-12' # date | Filter tasks anterior to given due date (optional)
    priority = 3 # int | Filter tasks on given priority (optional)
    page = 1 # int | Page number (optional) (default to 1)
    limit = 100 # int | Number of tasks per page (optional) (default to 100)

    try:
        # Get open tasks
        api_response = await api_instance.get_open_tasks(project_id=project_id, task_status_id=task_status_id, task_type_id=task_type_id, person_id=person_id, start_date=start_date, due_date=due_date, priority=priority, page=page, limit=limit)
        print("The response of TasksApi->get_open_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_open_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Filter tasks on given project ID | [optional] 
 **task_status_id** | **UUID**| Filter tasks on given task status ID | [optional] 
 **task_type_id** | **UUID**| Filter tasks on given task type ID | [optional] 
 **person_id** | **UUID**| Filter tasks on given person ID | [optional] 
 **start_date** | **date**| Filter tasks posterior to given start date | [optional] 
 **due_date** | **date**| Filter tasks anterior to given due date | [optional] 
 **priority** | **int**| Filter tasks on given priority | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Number of tasks per page | [optional] [default to 100]

### Return type

[**GetOpenTasks200Response**](GetOpenTasks200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tasks with pagination and statistics |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_tasks_stats**
> Dict[str, GetOpenTasksStats200ResponseValue] get_open_tasks_stats()

Get open tasks stats

Return totals and aggregates by status and task type per project for open projects.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_open_tasks_stats200_response_value import GetOpenTasksStats200ResponseValue
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)

    try:
        # Get open tasks stats
        api_response = await api_instance.get_open_tasks_stats()
        print("The response of TasksApi->get_open_tasks_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_open_tasks_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dict[str, GetOpenTasksStats200ResponseValue]**](GetOpenTasksStats200ResponseValue.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A dict by project with results for each task type and status pair |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_done_tasks**
> List[Task] get_person_done_tasks(person_id)

Get person done tasks

Return tasks assigned to the person that are done. Only tasks in open projects are returned.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.task import Task
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get person done tasks
        api_response = await api_instance.get_person_done_tasks(person_id)
        print("The response of TasksApi->get_person_done_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_person_done_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tasks assigned to user that are done |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_open_tasks**
> List[Task] get_person_open_tasks(person_id)

Get person open tasks

List tasks assigned to a person where the status is not done.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.task import Task
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get person open tasks
        api_response = await api_instance.get_person_open_tasks(person_id)
        print("The response of TasksApi->get_person_open_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_person_open_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tasks assigned to user that are not done |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_tasks_for_type**
> List[Task] get_person_tasks_for_type(person_id, task_type_id)

Get person tasks for type

For all entities assigned to the person, return tasks for the given task type.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.task import Task
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get person tasks for type
        api_response = await api_instance.get_person_tasks_for_type(person_id, task_type_id)
        print("The response of TasksApi->get_person_tasks_for_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_person_tasks_for_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**|  | 
 **task_type_id** | **UUID**|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All tasks for the given task type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_persons_tasks_dates**
> List[GetPersonsTasksDates200ResponseInner] get_persons_tasks_dates(project_id=project_id)

Get persons tasks dates

For each active person, return the first start date of all tasks assigned to them and the last end date. Useful for schedule planning.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_persons_tasks_dates200_response_inner import GetPersonsTasksDates200ResponseInner
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter by project ID (optional)

    try:
        # Get persons tasks dates
        api_response = await api_instance.get_persons_tasks_dates(project_id=project_id)
        print("The response of TasksApi->get_persons_tasks_dates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_persons_tasks_dates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Filter by project ID | [optional] 

### Return type

[**List[GetPersonsTasksDates200ResponseInner]**](GetPersonsTasksDates200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | First start date and last end date for tasks per person |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_comments**
> List[GetProjectComments200ResponseInner] get_project_comments(project_id, limit=limit)

Get project comments

Retrieve comments for tasks related to a project. Useful for sync.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_comments200_response_inner import GetProjectComments200ResponseInner
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get project comments
        api_response = await api_instance.get_project_comments(project_id, limit=limit)
        print("The response of TasksApi->get_project_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_project_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[GetProjectComments200ResponseInner]**](GetProjectComments200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All comments to tasks related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_notifications**
> GetProjectNotifications200Response get_project_notifications(project_id)

Get project notifications

Retrieve notifications for tasks related to a project. Useful for sync.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_notifications200_response import GetProjectNotifications200Response
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get project notifications
        api_response = await api_instance.get_project_notifications(project_id)
        print("The response of TasksApi->get_project_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_project_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 

### Return type

[**GetProjectNotifications200Response**](GetProjectNotifications200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All notifications to tasks related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_preview_files**
> GetProjectPreviewFiles200Response get_project_preview_files(project_id)

Get project preview files

Retrieve all preview files that are linked to a specific project. This includes images, videos, and other preview media associated with the project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_preview_files200_response import GetProjectPreviewFiles200Response
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get project preview files
        api_response = await api_instance.get_project_preview_files(project_id)
        print("The response of TasksApi->get_project_preview_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_project_preview_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 

### Return type

[**GetProjectPreviewFiles200Response**](GetProjectPreviewFiles200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preview files related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_subscriptions**
> List[GetProjectSubscriptions200ResponseInner] get_project_subscriptions(project_id)

Get project subscriptions

Retrieve all subscriptions to tasks related to a project. Useful for sync.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_subscriptions200_response_inner import GetProjectSubscriptions200ResponseInner
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get project subscriptions
        api_response = await api_instance.get_project_subscriptions(project_id)
        print("The response of TasksApi->get_project_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_project_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 

### Return type

[**List[GetProjectSubscriptions200ResponseInner]**](GetProjectSubscriptions200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All subcriptions to tasks related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tasks**
> GetProjectTasks200Response get_project_tasks(project_id, page=page, task_type_id=task_type_id, episode_id=episode_id)

Get project tasks

Retrieve tasks related to a project. Useful for sync.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_tasks200_response import GetProjectTasks200Response
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    page = 1 # int |  (optional)
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)

    try:
        # Get project tasks
        api_response = await api_instance.get_project_tasks(project_id, page=page, task_type_id=task_type_id, episode_id=episode_id)
        print("The response of TasksApi->get_project_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_project_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **page** | **int**|  | [optional] 
 **task_type_id** | **UUID**|  | [optional] 
 **episode_id** | **UUID**|  | [optional] 

### Return type

[**GetProjectTasks200Response**](GetProjectTasks200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All tasks related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_comments**
> List[GetTaskComments200ResponseInner] get_task_comments(task_id)

Get task comments

Return comments linked to a task.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_task_comments200_response_inner import GetTaskComments200ResponseInner
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get task comments
        api_response = await api_instance.get_task_comments(task_id)
        print("The response of TasksApi->get_task_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 

### Return type

[**List[GetTaskComments200ResponseInner]**](GetTaskComments200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comments linked to task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_full**
> GetTaskFull200Response get_task_full(task_id)

Get task full

Return a task with many information. Includes full details for assignees, task type, and task status.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_task_full200_response import GetTaskFull200Response
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get task full
        api_response = await api_instance.get_task_full(task_id)
        print("The response of TasksApi->get_task_full:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_full: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 

### Return type

[**GetTaskFull200Response**](GetTaskFull200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task with full information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_previews**
> List[GetTaskPreviews200ResponseInner] get_task_previews(task_id)

Get task previews

Return previews linked to a task.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_task_previews200_response_inner import GetTaskPreviews200ResponseInner
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get task previews
        api_response = await api_instance.get_task_previews(task_id)
        print("The response of TasksApi->get_task_previews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_previews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 

### Return type

[**List[GetTaskPreviews200ResponseInner]**](GetTaskPreviews200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Previews linked to task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_time_spent_for_date**
> List[TimeSpent] get_task_time_spent_for_date(task_id, var_date)

Get task time spent for date

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.time_spent import TimeSpent
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    var_date = '2022-07-12' # date | 

    try:
        # Get task time spent for date
        api_response = await api_instance.get_task_time_spent_for_date(task_id, var_date)
        print("The response of TasksApi->get_task_time_spent_for_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_time_spent_for_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 
 **var_date** | **date**|  | 

### Return type

[**List[TimeSpent]**](TimeSpent.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time spent on the task for the date |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_time_spent_get_actions_tasks_task_id_time_spents**
> List[TimeSpent] get_task_time_spent_get_actions_tasks_task_id_time_spents(task_id)

Get task time spent

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.time_spent import TimeSpent
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get task time spent
        api_response = await api_instance.get_task_time_spent_get_actions_tasks_task_id_time_spents(task_id)
        print("The response of TasksApi->get_task_time_spent_get_actions_tasks_task_id_time_spents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_time_spent_get_actions_tasks_task_id_time_spents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 

### Return type

[**List[TimeSpent]**](TimeSpent.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time spent on the task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_for_entity_and_type**
> List[Task] get_tasks_for_entity_and_type(entity_id, task_type_id)

Get tasks for entity and type

Return tasks related to the entity (asset, episode, sequence, shot, or scene) for a task type.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.task import Task
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get tasks for entity and type
        api_response = await api_instance.get_tasks_for_entity_and_type(entity_id, task_type_id)
        print("The response of TasksApi->get_tasks_for_entity_and_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_tasks_for_entity_and_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**|  | 
 **task_type_id** | **UUID**|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tasks related to the entity and task type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_main_preview_from_task**
> SetMainPreviewFromTask200Response set_main_preview_from_task(task_id)

Set main preview from task

Set the last preview of a task as the main preview of the related entity.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.set_main_preview_from_task200_response import SetMainPreviewFromTask200Response
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Set main preview from task
        api_response = await api_instance.set_main_preview_from_task(task_id)
        print("The response of TasksApi->set_main_preview_from_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->set_main_preview_from_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 

### Return type

[**SetMainPreviewFromTask200Response**](SetMainPreviewFromTask200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preview set as main preview |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_task_to_review**
> Task set_task_to_review(task_id, set_task_to_review_request)

Set task to review

Create a new preview file entry and set the path from the disk. Optionally change the task status.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.set_task_to_review_request import SetTaskToReviewRequest
from sometech.pykitsu._client.models.task import Task
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    set_task_to_review_request = sometech.pykitsu._client.SetTaskToReviewRequest() # SetTaskToReviewRequest | 

    try:
        # Set task to review
        api_response = await api_instance.set_task_to_review(task_id, set_task_to_review_request)
        print("The response of TasksApi->set_task_to_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->set_task_to_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 
 **set_task_to_review_request** | [**SetTaskToReviewRequest**](SetTaskToReviewRequest.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task set to review and preview created |  -  |
**400** | Invalid person or parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_time_spent**
> TimeSpent set_time_spent(task_id, var_date, person_id, set_time_spent_request)

Set time spent

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.set_time_spent_request import SetTimeSpentRequest
from sometech.pykitsu._client.models.time_spent import TimeSpent
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
    api_instance = sometech.pykitsu._client.TasksApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    var_date = '2022-07-12' # date | 
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    set_time_spent_request = sometech.pykitsu._client.SetTimeSpentRequest() # SetTimeSpentRequest | 

    try:
        # Set time spent
        api_response = await api_instance.set_time_spent(task_id, var_date, person_id, set_time_spent_request)
        print("The response of TasksApi->set_time_spent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->set_time_spent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**|  | 
 **var_date** | **date**|  | 
 **person_id** | **UUID**|  | 
 **set_time_spent_request** | [**SetTimeSpentRequest**](SetTimeSpentRequest.md)|  | 

### Return type

[**TimeSpent**](TimeSpent.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Time spent set for the person on the task and day |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

