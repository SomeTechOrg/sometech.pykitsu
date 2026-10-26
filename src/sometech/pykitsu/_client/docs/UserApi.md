# sometech.pykitsu._client.UserApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_sequence_subscription**](UserApi.md#check_sequence_subscription) | **GET** /data/user/entities/{sequence_id}/task-types/{task_type_id}/subscribed | Check sequence subscription
[**check_task_subscription**](UserApi.md#check_task_subscription) | **GET** /data/user/tasks/{task_id}/subscribed | Check task subscription
[**clear_avatar**](UserApi.md#clear_avatar) | **DELETE** /actions/user/clear-avatar | Clear avatar
[**create_desktop_login_log_post_data_user_desktop_login_logs**](UserApi.md#create_desktop_login_log_post_data_user_desktop_login_logs) | **POST** /data/user/desktop-login-logs | Create desktop login log
[**create_filter**](UserApi.md#create_filter) | **POST** /data/user/filters | Create filter
[**create_filter_group**](UserApi.md#create_filter_group) | **POST** /data/user/filter-groups | Create filter group
[**delete_filter**](UserApi.md#delete_filter) | **DELETE** /data/user/filters/{filter_id} | Delete filter
[**delete_filter_group**](UserApi.md#delete_filter_group) | **DELETE** /data/user/filter-groups/{filter_group_id} | Delete filter group
[**get_asset_task_types_get_data_user_assets_asset_id_task_types**](UserApi.md#get_asset_task_types_get_data_user_assets_asset_id_task_types) | **GET** /data/user/assets/{asset_id}/task-types | Get asset task types
[**get_asset_tasks_get_data_user_assets_asset_id_tasks**](UserApi.md#get_asset_tasks_get_data_user_assets_asset_id_tasks) | **GET** /data/user/assets/{asset_id}/tasks | Get asset tasks
[**get_chats_get_data_user_chats**](UserApi.md#get_chats_get_data_user_chats) | **GET** /data/user/chats | Get chats
[**get_context**](UserApi.md#get_context) | **GET** /data/user/context | Get context
[**get_day_off_get_data_user_day_offs_date**](UserApi.md#get_day_off_get_data_user_day_offs_date) | **GET** /data/user/day-offs/{date} | Get day off
[**get_desktop_login_logs_get_data_user_desktop_login_logs**](UserApi.md#get_desktop_login_logs_get_data_user_desktop_login_logs) | **GET** /data/user/desktop-login-logs | Get desktop login logs
[**get_done_tasks**](UserApi.md#get_done_tasks) | **GET** /data/user/done-tasks | Get done tasks
[**get_filter_group**](UserApi.md#get_filter_group) | **GET** /data/user/filter-groups/{filter_group_id} | Get filter group
[**get_filter_groups**](UserApi.md#get_filter_groups) | **GET** /data/user/filter-groups | Get filter groups
[**get_filters**](UserApi.md#get_filters) | **GET** /data/user/filters | Get filters
[**get_my_tasks**](UserApi.md#get_my_tasks) | **GET** /data/user/tasks | Get my tasks
[**get_notification_get_data_user_notifications_notification_id**](UserApi.md#get_notification_get_data_user_notifications_notification_id) | **GET** /data/user/notifications/{notification_id} | Get notification
[**get_notifications_get_data_user_notifications**](UserApi.md#get_notifications_get_data_user_notifications) | **GET** /data/user/notifications | Get notifications
[**get_open_projects_get_data_user_projects_open**](UserApi.md#get_open_projects_get_data_user_projects_open) | **GET** /data/user/projects/open | Get open projects
[**get_project_asset_types_get_data_user_projects_project_id_asset_types**](UserApi.md#get_project_asset_types_get_data_user_projects_project_id_asset_types) | **GET** /data/user/projects/{project_id}/asset-types | Get project asset types
[**get_project_assets_get_data_user_projects_project_id_asset_types_asset_type_id_assets**](UserApi.md#get_project_assets_get_data_user_projects_project_id_asset_types_asset_type_id_assets) | **GET** /data/user/projects/{project_id}/asset-types/{asset_type_id}/assets | Get project assets
[**get_project_episodes_get_data_user_projects_project_id_episodes**](UserApi.md#get_project_episodes_get_data_user_projects_project_id_episodes) | **GET** /data/user/projects/{project_id}/episodes | Get project episodes
[**get_project_sequences_get_data_user_projects_project_id_sequences**](UserApi.md#get_project_sequences_get_data_user_projects_project_id_sequences) | **GET** /data/user/projects/{project_id}/sequences | Get project sequences
[**get_scene_task_types_get_data_user_scenes_scene_id_task_types**](UserApi.md#get_scene_task_types_get_data_user_scenes_scene_id_task_types) | **GET** /data/user/scenes/{scene_id}/task-types | Get scene task types
[**get_scene_tasks_get_data_user_scenes_scene_id_tasks**](UserApi.md#get_scene_tasks_get_data_user_scenes_scene_id_tasks) | **GET** /data/user/scenes/{scene_id}/tasks | Get scene tasks
[**get_sequence_scenes_get_data_user_sequences_sequence_id_scenes**](UserApi.md#get_sequence_scenes_get_data_user_sequences_sequence_id_scenes) | **GET** /data/user/sequences/{sequence_id}/scenes | Get sequence scenes
[**get_sequence_shots_get_data_user_sequences_sequence_id_shots**](UserApi.md#get_sequence_shots_get_data_user_sequences_sequence_id_shots) | **GET** /data/user/sequences/{sequence_id}/shots | Get sequence shots
[**get_sequence_subscriptions**](UserApi.md#get_sequence_subscriptions) | **GET** /data/user/projects/{project_id}/task-types/{task_type_id}/sequence-subscriptions | Get sequence subscriptions
[**get_sequence_task_types_get_data_user_sequences_sequence_id_task_types**](UserApi.md#get_sequence_task_types_get_data_user_sequences_sequence_id_task_types) | **GET** /data/user/sequences/{sequence_id}/task-types | Get sequence task types
[**get_sequence_tasks_get_data_user_sequences_sequence_id_tasks**](UserApi.md#get_sequence_tasks_get_data_user_sequences_sequence_id_tasks) | **GET** /data/user/sequences/{sequence_id}/tasks | Get sequence tasks
[**get_shot_task_types_get_data_user_shots_shot_id_task_types**](UserApi.md#get_shot_task_types_get_data_user_shots_shot_id_task_types) | **GET** /data/user/shots/{shot_id}/task-types | Get shot task types
[**get_shot_tasks_get_data_user_shots_shot_id_tasks**](UserApi.md#get_shot_tasks_get_data_user_shots_shot_id_tasks) | **GET** /data/user/shots/{shot_id}/tasks | Get shot tasks
[**get_task_time_spent_get_data_user_tasks_task_id_time_spents_date**](UserApi.md#get_task_time_spent_get_data_user_tasks_task_id_time_spents_date) | **GET** /data/user/tasks/{task_id}/time-spents/{date} | Get task time spent
[**get_tasks_requiring_feedback**](UserApi.md#get_tasks_requiring_feedback) | **GET** /data/user/tasks-to-check | Get tasks requiring feedback
[**get_time_spents_by_date**](UserApi.md#get_time_spents_by_date) | **GET** /data/user/time-spents/{date} | Get time spents by date
[**get_time_spents_get_data_user_time_spents**](UserApi.md#get_time_spents_get_data_user_time_spents) | **GET** /data/user/time-spents | Get time spents
[**join_chat**](UserApi.md#join_chat) | **POST** /actions/user/chats/{entity_id}/join | Join chat
[**leave_chat**](UserApi.md#leave_chat) | **DELETE** /actions/user/chats/{entity_id}/join | Leave chat
[**mark_all_notifications_as_read**](UserApi.md#mark_all_notifications_as_read) | **POST** /actions/user/notifications/mark-all-as-read | Mark all notifications as read
[**subscribe_to_sequence**](UserApi.md#subscribe_to_sequence) | **POST** /actions/user/sequences/{sequence_id}/task-types/{task_type_id}/subscribe | Subscribe to sequence
[**subscribe_to_task**](UserApi.md#subscribe_to_task) | **POST** /actions/user/tasks/{task_id}/subscribe | Subscribe to task
[**unsubscribe_from_sequence**](UserApi.md#unsubscribe_from_sequence) | **DELETE** /actions/user/sequences/{sequence_id}/task-types/{task_type_id}/unsubscribe | Unsubscribe from sequence
[**unsubscribe_from_task**](UserApi.md#unsubscribe_from_task) | **DELETE** /actions/user/tasks/{task_id}/unsubscribe | Unsubscribe from task
[**update_filter**](UserApi.md#update_filter) | **PUT** /data/user/filters/{filter_id} | Update filter
[**update_filter_group**](UserApi.md#update_filter_group) | **PUT** /data/user/filter-groups/{filter_group_id} | Update filter group
[**update_notification_put_data_user_notifications_notification_id**](UserApi.md#update_notification_put_data_user_notifications_notification_id) | **PUT** /data/user/notifications/{notification_id} | Update notification


# **check_sequence_subscription**
> bool check_sequence_subscription(sequence_id, task_type_id)

Check sequence subscription

Check if the current user has subscribed to a specific sequence and task type combination. Returns true if subscribed.

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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Sequence unique identifier
    task_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Task type unique identifier

    try:
        # Check sequence subscription
        api_response = await api_instance.check_sequence_subscription(sequence_id, task_type_id)
        print("The response of UserApi->check_sequence_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->check_sequence_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**| Sequence unique identifier | 
 **task_type_id** | **UUID**| Task type unique identifier | 

### Return type

**bool**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription status for the sequence and task type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_task_subscription**
> bool check_task_subscription(task_id)

Check task subscription

Check if the current user has subscribed to a specific task.

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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Task unique identifier

    try:
        # Check task subscription
        api_response = await api_instance.check_task_subscription(task_id)
        print("The response of UserApi->check_task_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->check_task_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Task unique identifier | 

### Return type

**bool**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription status for the task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_avatar**
> clear_avatar()

Clear avatar

Set the has_avatar flag to false for the current user and remove the avatar file from storage. This action cannot be undone.

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
    api_instance = sometech.pykitsu._client.UserApi(api_client)

    try:
        # Clear avatar
        await api_instance.clear_avatar()
    except Exception as e:
        print("Exception when calling UserApi->clear_avatar: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | Avatar file deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_desktop_login_log_post_data_user_desktop_login_logs**
> GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner create_desktop_login_log_post_data_user_desktop_login_logs(create_desktop_login_log_post_data_user_desktop_login_logs_request)

Create desktop login log

Create a desktop login log entry for the current user.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_desktop_login_log_post_data_user_desktop_login_logs_request import CreateDesktopLoginLogPostDataUserDesktopLoginLogsRequest
from sometech.pykitsu._client.models.get_desktop_login_logs_get_data_user_desktop_login_logs200_response_inner import GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    create_desktop_login_log_post_data_user_desktop_login_logs_request = sometech.pykitsu._client.CreateDesktopLoginLogPostDataUserDesktopLoginLogsRequest() # CreateDesktopLoginLogPostDataUserDesktopLoginLogsRequest | 

    try:
        # Create desktop login log
        api_response = await api_instance.create_desktop_login_log_post_data_user_desktop_login_logs(create_desktop_login_log_post_data_user_desktop_login_logs_request)
        print("The response of UserApi->create_desktop_login_log_post_data_user_desktop_login_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_desktop_login_log_post_data_user_desktop_login_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_desktop_login_log_post_data_user_desktop_login_logs_request** | [**CreateDesktopLoginLogPostDataUserDesktopLoginLogsRequest**](CreateDesktopLoginLogPostDataUserDesktopLoginLogsRequest.md)|  | 

### Return type

[**GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner**](GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Desktop login log created successfully |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_filter**
> CreateFilter201Response create_filter(create_filter_request)

Create filter

Create a new filter for the current user limited to open projects only.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_filter201_response import CreateFilter201Response
from sometech.pykitsu._client.models.create_filter_request import CreateFilterRequest
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    create_filter_request = sometech.pykitsu._client.CreateFilterRequest() # CreateFilterRequest | 

    try:
        # Create filter
        api_response = await api_instance.create_filter(create_filter_request)
        print("The response of UserApi->create_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_filter_request** | [**CreateFilterRequest**](CreateFilterRequest.md)|  | 

### Return type

[**CreateFilter201Response**](CreateFilter201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Filter created successfully |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_filter_group**
> CreateFilterGroup201Response create_filter_group(create_filter_group_request)

Create filter group

Create a new filter group for the current user limited to open projects only. The filter group can be shared with other users.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_filter_group201_response import CreateFilterGroup201Response
from sometech.pykitsu._client.models.create_filter_group_request import CreateFilterGroupRequest
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    create_filter_group_request = sometech.pykitsu._client.CreateFilterGroupRequest() # CreateFilterGroupRequest | 

    try:
        # Create filter group
        api_response = await api_instance.create_filter_group(create_filter_group_request)
        print("The response of UserApi->create_filter_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_filter_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_filter_group_request** | [**CreateFilterGroupRequest**](CreateFilterGroupRequest.md)|  | 

### Return type

[**CreateFilterGroup201Response**](CreateFilterGroup201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Filter group created successfully |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filter**
> delete_filter(filter_id)

Delete filter

Delete a specific filter if it is owned by the current user.

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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    filter_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter unique identifier

    try:
        # Delete filter
        await api_instance.delete_filter(filter_id)
    except Exception as e:
        print("Exception when calling UserApi->delete_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **UUID**| Filter unique identifier | 

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
**204** | Filter deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filter_group**
> delete_filter_group(filter_group_id)

Delete filter group

Delete a specific filter group if it is owned by the current user.

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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    filter_group_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter group unique identifier

    try:
        # Delete filter group
        await api_instance.delete_filter_group(filter_group_id)
    except Exception as e:
        print("Exception when calling UserApi->delete_filter_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_group_id** | **UUID**| Filter group unique identifier | 

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
**204** | Filter group deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_task_types_get_data_user_assets_asset_id_task_types**
> List[TaskType] get_asset_task_types_get_data_user_assets_asset_id_task_types(asset_id)

Get asset task types

Retrieve task types related to a specific asset for the current user. Returns all task types available for the given asset.

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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    asset_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Asset unique identifier

    try:
        # Get asset task types
        api_response = await api_instance.get_asset_task_types_get_data_user_assets_asset_id_task_types(asset_id)
        print("The response of UserApi->get_asset_task_types_get_data_user_assets_asset_id_task_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_asset_task_types_get_data_user_assets_asset_id_task_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**| Asset unique identifier | 

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
**200** | Task types related to given asset for current user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_tasks_get_data_user_assets_asset_id_tasks**
> List[GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner] get_asset_tasks_get_data_user_assets_asset_id_tasks(asset_id)

Get asset tasks

Return tasks related to given asset for current user.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_asset_tasks_get_data_user_assets_asset_id_tasks200_response_inner import GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    asset_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Asset unique identifier

    try:
        # Get asset tasks
        api_response = await api_instance.get_asset_tasks_get_data_user_assets_asset_id_tasks(asset_id)
        print("The response of UserApi->get_asset_tasks_get_data_user_assets_asset_id_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_asset_tasks_get_data_user_assets_asset_id_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**| Asset unique identifier | 

### Return type

[**List[GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner]**](GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tasks related to given asset for current user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chats_get_data_user_chats**
> List[GetChatsGetDataUserChats200ResponseInner] get_chats_get_data_user_chats()

Get chats

Retrieve all chats where the current user is a participant. Returns list of chat conversations the user can access.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_chats_get_data_user_chats200_response_inner import GetChatsGetDataUserChats200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)

    try:
        # Get chats
        api_response = await api_instance.get_chats_get_data_user_chats()
        print("The response of UserApi->get_chats_get_data_user_chats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_chats_get_data_user_chats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetChatsGetDataUserChats200ResponseInner]**](GetChatsGetDataUserChats200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chats where user is participant |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_context**
> GetContext200Response get_context()

Get context

Retrieve context information required to properly run a full application connected to the API. Returns user, project, and system configuration data.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_context200_response import GetContext200Response
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)

    try:
        # Get context
        api_response = await api_instance.get_context()
        print("The response of UserApi->get_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_context: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetContext200Response**](GetContext200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Context information for running a full app connected to the API |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_day_off_get_data_user_day_offs_date**
> GetDayOffGetDataUserDayOffsDate200Response get_day_off_get_data_user_day_offs_date(var_date)

Get day off

Retrieve day off information for the current user on a specific date.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_day_off_get_data_user_day_offs_date200_response import GetDayOffGetDataUserDayOffsDate200Response
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    var_date = '2023-01-01' # date | Date to check for day off

    try:
        # Get day off
        api_response = await api_instance.get_day_off_get_data_user_day_offs_date(var_date)
        print("The response of UserApi->get_day_off_get_data_user_day_offs_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_day_off_get_data_user_day_offs_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**| Date to check for day off | 

### Return type

[**GetDayOffGetDataUserDayOffsDate200Response**](GetDayOffGetDataUserDayOffsDate200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Day off object for the current user on given date |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_desktop_login_logs_get_data_user_desktop_login_logs**
> List[GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner] get_desktop_login_logs_get_data_user_desktop_login_logs()

Get desktop login logs

Retrieve desktop login logs for the current user.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_desktop_login_logs_get_data_user_desktop_login_logs200_response_inner import GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)

    try:
        # Get desktop login logs
        api_response = await api_instance.get_desktop_login_logs_get_data_user_desktop_login_logs()
        print("The response of UserApi->get_desktop_login_logs_get_data_user_desktop_login_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_desktop_login_logs_get_data_user_desktop_login_logs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner]**](GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Desktop login logs for current user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_done_tasks**
> List[GetDoneTasks200ResponseInner] get_done_tasks()

Get done tasks

Retrieve tasks currently assigned to the current user with status marked as done. Returns only tasks from open projects.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_done_tasks200_response_inner import GetDoneTasks200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)

    try:
        # Get done tasks
        api_response = await api_instance.get_done_tasks()
        print("The response of UserApi->get_done_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_done_tasks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetDoneTasks200ResponseInner]**](GetDoneTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Finished tasks currently assigned to current user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filter_group**
> GetFilterGroup200Response get_filter_group(search_filter_group_id, filter_group_id)

Get filter group

Retrieve a specific filter group for the current user. Returns detailed information about the filter group.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_filter_group200_response import GetFilterGroup200Response
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    search_filter_group_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter group unique identifier
    filter_group_id = 'filter_group_id_example' # str | 

    try:
        # Get filter group
        api_response = await api_instance.get_filter_group(search_filter_group_id, filter_group_id)
        print("The response of UserApi->get_filter_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_filter_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_filter_group_id** | **UUID**| Filter group unique identifier | 
 **filter_group_id** | **str**|  | 

### Return type

[**GetFilterGroup200Response**](GetFilterGroup200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filter group details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filter_groups**
> List[GetFilterGroups200ResponseInner] get_filter_groups()

Get filter groups

Retrieve filter groups for the current user limited to open projects only.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_filter_groups200_response_inner import GetFilterGroups200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)

    try:
        # Get filter groups
        api_response = await api_instance.get_filter_groups()
        print("The response of UserApi->get_filter_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_filter_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetFilterGroups200ResponseInner]**](GetFilterGroups200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filter groups for current user and only for open projects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filters**
> List[GetFilters200ResponseInner] get_filters()

Get filters

Retrieve filters for the current user limited to open projects only.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_filters200_response_inner import GetFilters200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)

    try:
        # Get filters
        api_response = await api_instance.get_filters()
        print("The response of UserApi->get_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_filters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetFilters200ResponseInner]**](GetFilters200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filters for current user and only for open projects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_tasks**
> List[GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner] get_my_tasks()

Get my tasks

Retrieve ttasks currently assigned to current user and of which status has is_done attribute set to false.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_asset_tasks_get_data_user_assets_asset_id_tasks200_response_inner import GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)

    try:
        # Get my tasks
        api_response = await api_instance.get_my_tasks()
        print("The response of UserApi->get_my_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_my_tasks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner]**](GetAssetTasksGetDataUserAssetsAssetIdTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unfinished tasks currently assigned to current user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_get_data_user_notifications_notification_id**
> Notification get_notification_get_data_user_notifications_notification_id(notification_id)

Get notification

Retrieve a specific notification by ID, only if it belongs to the current user.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.notification import Notification
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    notification_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Notification unique identifier

    try:
        # Get notification
        api_response = await api_instance.get_notification_get_data_user_notifications_notification_id(notification_id)
        print("The response of UserApi->get_notification_get_data_user_notifications_notification_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_notification_get_data_user_notifications_notification_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **UUID**| Notification unique identifier | 

### Return type

[**Notification**](Notification.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notification details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_get_data_user_notifications**
> List[Notification] get_notifications_get_data_user_notifications(after=after, before=before, task_type_id=task_type_id, task_status_id=task_status_id, type=type, read=read, watching=watching)

Get notifications

Retrieve the last 100 user notifications filtered by given parameters. Supports filtering by date range, task type, status, and other criteria.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.notification import Notification
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    after = '2023-01-01' # date | Filter notifications after this date (optional)
    before = '2023-12-31' # date | Filter notifications before this date (optional)
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter by task type ID (optional)
    task_status_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Filter by task status ID (optional)
    type = 'comment' # str | Filter by notification type (optional)
    read = false # bool | Filter by read status (optional)
    watching = true # bool | Filter by watching status (optional)

    try:
        # Get notifications
        api_response = await api_instance.get_notifications_get_data_user_notifications(after=after, before=before, task_type_id=task_type_id, task_status_id=task_status_id, type=type, read=read, watching=watching)
        print("The response of UserApi->get_notifications_get_data_user_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_notifications_get_data_user_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **date**| Filter notifications after this date | [optional] 
 **before** | **date**| Filter notifications before this date | [optional] 
 **task_type_id** | **UUID**| Filter by task type ID | [optional] 
 **task_status_id** | **UUID**| Filter by task status ID | [optional] 
 **type** | **str**| Filter by notification type | [optional] 
 **read** | **bool**| Filter by read status | [optional] 
 **watching** | **bool**| Filter by watching status | [optional] 

### Return type

[**List[Notification]**](Notification.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Last 100 user notifications matching filters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_projects_get_data_user_projects_open**
> List[GetOpenProjectsGetDataUserProjectsOpen200ResponseInner] get_open_projects_get_data_user_projects_open(name=name)

Get open projects

Retrieve open projects for which the current user has at least one task assigned. Optionally filter by project name.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_open_projects_get_data_user_projects_open200_response_inner import GetOpenProjectsGetDataUserProjectsOpen200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    name = 'My Project' # str | Filter projects by name (optional)

    try:
        # Get open projects
        api_response = await api_instance.get_open_projects_get_data_user_projects_open(name=name)
        print("The response of UserApi->get_open_projects_get_data_user_projects_open:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_open_projects_get_data_user_projects_open: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter projects by name | [optional] 

### Return type

[**List[GetOpenProjectsGetDataUserProjectsOpen200ResponseInner]**](GetOpenProjectsGetDataUserProjectsOpen200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Open projects with assigned tasks for current user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_asset_types_get_data_user_projects_project_id_asset_types**
> List[GetProjectAssetTypesGetDataUserProjectsProjectIdAssetTypes200ResponseInner] get_project_asset_types_get_data_user_projects_project_id_asset_types(project_id)

Get project asset types

Retrieve asset types related to a specific project for the current user.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_asset_types_get_data_user_projects_project_id_asset_types200_response_inner import GetProjectAssetTypesGetDataUserProjectsProjectIdAssetTypes200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get project asset types
        api_response = await api_instance.get_project_asset_types_get_data_user_projects_project_id_asset_types(project_id)
        print("The response of UserApi->get_project_asset_types_get_data_user_projects_project_id_asset_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_project_asset_types_get_data_user_projects_project_id_asset_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

[**List[GetProjectAssetTypesGetDataUserProjectsProjectIdAssetTypes200ResponseInner]**](GetProjectAssetTypesGetDataUserProjectsProjectIdAssetTypes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset types related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_assets_get_data_user_projects_project_id_asset_types_asset_type_id_assets**
> List[GetProjectAssetsGetDataUserProjectsProjectIdAssetTypesAssetTypeIdAssets200ResponseInner] get_project_assets_get_data_user_projects_project_id_asset_types_asset_type_id_assets(project_id, asset_type_id)

Get project assets

Retrieve assets of a specific type within a project matching the asset type in the given project if the user has access.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_assets_get_data_user_projects_project_id_asset_types_asset_type_id_assets200_response_inner import GetProjectAssetsGetDataUserProjectsProjectIdAssetTypesAssetTypeIdAssets200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    asset_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Asset type unique identifier

    try:
        # Get project assets
        api_response = await api_instance.get_project_assets_get_data_user_projects_project_id_asset_types_asset_type_id_assets(project_id, asset_type_id)
        print("The response of UserApi->get_project_assets_get_data_user_projects_project_id_asset_types_asset_type_id_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_project_assets_get_data_user_projects_project_id_asset_types_asset_type_id_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **asset_type_id** | **UUID**| Asset type unique identifier | 

### Return type

[**List[GetProjectAssetsGetDataUserProjectsProjectIdAssetTypesAssetTypeIdAssets200ResponseInner]**](GetProjectAssetsGetDataUserProjectsProjectIdAssetTypesAssetTypeIdAssets200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assets of given type in the specified project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_episodes_get_data_user_projects_project_id_episodes**
> List[GetProjectEpisodesGetDataUserProjectsProjectIdEpisodes200ResponseInner] get_project_episodes_get_data_user_projects_project_id_episodes(project_id)

Get project episodes

Retrieve episodes related to a specific project for the current user. Returns all episodes in the project if the user has access.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_episodes_get_data_user_projects_project_id_episodes200_response_inner import GetProjectEpisodesGetDataUserProjectsProjectIdEpisodes200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get project episodes
        api_response = await api_instance.get_project_episodes_get_data_user_projects_project_id_episodes(project_id)
        print("The response of UserApi->get_project_episodes_get_data_user_projects_project_id_episodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_project_episodes_get_data_user_projects_project_id_episodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

[**List[GetProjectEpisodesGetDataUserProjectsProjectIdEpisodes200ResponseInner]**](GetProjectEpisodesGetDataUserProjectsProjectIdEpisodes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Episodes related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_sequences_get_data_user_projects_project_id_sequences**
> List[GetProjectSequencesGetDataUserProjectsProjectIdSequences200ResponseInner] get_project_sequences_get_data_user_projects_project_id_sequences(project_id)

Get project sequences

Retrieve sequences related to a specific project for the current user. Returns all sequences in the project if the user has access.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_sequences_get_data_user_projects_project_id_sequences200_response_inner import GetProjectSequencesGetDataUserProjectsProjectIdSequences200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get project sequences
        api_response = await api_instance.get_project_sequences_get_data_user_projects_project_id_sequences(project_id)
        print("The response of UserApi->get_project_sequences_get_data_user_projects_project_id_sequences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_project_sequences_get_data_user_projects_project_id_sequences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

[**List[GetProjectSequencesGetDataUserProjectsProjectIdSequences200ResponseInner]**](GetProjectSequencesGetDataUserProjectsProjectIdSequences200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sequences related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scene_task_types_get_data_user_scenes_scene_id_task_types**
> List[TaskType] get_scene_task_types_get_data_user_scenes_scene_id_task_types(scene_id)

Get scene task types

Retrieve task types related to a specific scene for the current user.

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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    scene_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Scene unique identifier

    try:
        # Get scene task types
        api_response = await api_instance.get_scene_task_types_get_data_user_scenes_scene_id_task_types(scene_id)
        print("The response of UserApi->get_scene_task_types_get_data_user_scenes_scene_id_task_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_scene_task_types_get_data_user_scenes_scene_id_task_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **UUID**| Scene unique identifier | 

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
**200** | Task types related to given scene for current user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scene_tasks_get_data_user_scenes_scene_id_tasks**
> List[GetSceneTasksGetDataUserScenesSceneIdTasks200ResponseInner] get_scene_tasks_get_data_user_scenes_scene_id_tasks(scene_id)

Get scene tasks

Retrieve tasks related to a specific scene for the current user.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_scene_tasks_get_data_user_scenes_scene_id_tasks200_response_inner import GetSceneTasksGetDataUserScenesSceneIdTasks200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    scene_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Scene unique identifier

    try:
        # Get scene tasks
        api_response = await api_instance.get_scene_tasks_get_data_user_scenes_scene_id_tasks(scene_id)
        print("The response of UserApi->get_scene_tasks_get_data_user_scenes_scene_id_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_scene_tasks_get_data_user_scenes_scene_id_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **UUID**| Scene unique identifier | 

### Return type

[**List[GetSceneTasksGetDataUserScenesSceneIdTasks200ResponseInner]**](GetSceneTasksGetDataUserScenesSceneIdTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tasks related to given scene |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence_scenes_get_data_user_sequences_sequence_id_scenes**
> List[GetSequenceScenesGetDataUserSequencesSequenceIdScenes200ResponseInner] get_sequence_scenes_get_data_user_sequences_sequence_id_scenes(sequence_id)

Get sequence scenes

Retrieve scenes related to a specific sequence for the current user.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_sequence_scenes_get_data_user_sequences_sequence_id_scenes200_response_inner import GetSequenceScenesGetDataUserSequencesSequenceIdScenes200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Sequence unique identifier

    try:
        # Get sequence scenes
        api_response = await api_instance.get_sequence_scenes_get_data_user_sequences_sequence_id_scenes(sequence_id)
        print("The response of UserApi->get_sequence_scenes_get_data_user_sequences_sequence_id_scenes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_sequence_scenes_get_data_user_sequences_sequence_id_scenes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**| Sequence unique identifier | 

### Return type

[**List[GetSequenceScenesGetDataUserSequencesSequenceIdScenes200ResponseInner]**](GetSequenceScenesGetDataUserSequencesSequenceIdScenes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scenes related to given sequence |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence_shots_get_data_user_sequences_sequence_id_shots**
> List[GetSequenceShotsGetDataUserSequencesSequenceIdShots200ResponseInner] get_sequence_shots_get_data_user_sequences_sequence_id_shots(sequence_id)

Get sequence shots

Retrieve shots related to a specific sequence for the current user.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_sequence_shots_get_data_user_sequences_sequence_id_shots200_response_inner import GetSequenceShotsGetDataUserSequencesSequenceIdShots200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Sequence unique identifier

    try:
        # Get sequence shots
        api_response = await api_instance.get_sequence_shots_get_data_user_sequences_sequence_id_shots(sequence_id)
        print("The response of UserApi->get_sequence_shots_get_data_user_sequences_sequence_id_shots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_sequence_shots_get_data_user_sequences_sequence_id_shots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**| Sequence unique identifier | 

### Return type

[**List[GetSequenceShotsGetDataUserSequencesSequenceIdShots200ResponseInner]**](GetSequenceShotsGetDataUserSequencesSequenceIdShots200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shots related to given sequence |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence_subscriptions**
> List[UUID] get_sequence_subscriptions(project_id, task_type_id)

Get sequence subscriptions

Retrieve list of sequence IDs to which the current user has subscribed for a given task type within a specific project.

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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    task_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Task type unique identifier

    try:
        # Get sequence subscriptions
        api_response = await api_instance.get_sequence_subscriptions(project_id, task_type_id)
        print("The response of UserApi->get_sequence_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_sequence_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **task_type_id** | **UUID**| Task type unique identifier | 

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
**200** | List of subscribed sequence IDs for the task type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence_task_types_get_data_user_sequences_sequence_id_task_types**
> List[TaskType] get_sequence_task_types_get_data_user_sequences_sequence_id_task_types(sequence_id)

Get sequence task types

Retrieve task types related to a specific sequence for the current user.

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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Sequence unique identifier

    try:
        # Get sequence task types
        api_response = await api_instance.get_sequence_task_types_get_data_user_sequences_sequence_id_task_types(sequence_id)
        print("The response of UserApi->get_sequence_task_types_get_data_user_sequences_sequence_id_task_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_sequence_task_types_get_data_user_sequences_sequence_id_task_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**| Sequence unique identifier | 

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
**200** | Task types related to given sequence for current user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence_tasks_get_data_user_sequences_sequence_id_tasks**
> List[GetSequenceTasksGetDataUserSequencesSequenceIdTasks200ResponseInner] get_sequence_tasks_get_data_user_sequences_sequence_id_tasks(sequence_id)

Get sequence tasks

Retrieve tasks related to a specific sequence for the current user. sequence.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_sequence_tasks_get_data_user_sequences_sequence_id_tasks200_response_inner import GetSequenceTasksGetDataUserSequencesSequenceIdTasks200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Sequence unique identifier

    try:
        # Get sequence tasks
        api_response = await api_instance.get_sequence_tasks_get_data_user_sequences_sequence_id_tasks(sequence_id)
        print("The response of UserApi->get_sequence_tasks_get_data_user_sequences_sequence_id_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_sequence_tasks_get_data_user_sequences_sequence_id_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**| Sequence unique identifier | 

### Return type

[**List[GetSequenceTasksGetDataUserSequencesSequenceIdTasks200ResponseInner]**](GetSequenceTasksGetDataUserSequencesSequenceIdTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tasks related to given sequence |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_task_types_get_data_user_shots_shot_id_task_types**
> List[TaskType] get_shot_task_types_get_data_user_shots_shot_id_task_types(shot_id)

Get shot task types

Retrieve task types related to a specific shot for the current user. Returns all task types available for the given shot.

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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    shot_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Shot unique identifier

    try:
        # Get shot task types
        api_response = await api_instance.get_shot_task_types_get_data_user_shots_shot_id_task_types(shot_id)
        print("The response of UserApi->get_shot_task_types_get_data_user_shots_shot_id_task_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_shot_task_types_get_data_user_shots_shot_id_task_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | **UUID**| Shot unique identifier | 

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
**200** | Task types related to given shot for current user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_tasks_get_data_user_shots_shot_id_tasks**
> List[GetShotTasksGetDataUserShotsShotIdTasks200ResponseInner] get_shot_tasks_get_data_user_shots_shot_id_tasks(shot_id)

Get shot tasks

Retrieve tasks related to a specific shot for the current user. Returns all tasks assigned to the user for the given shot.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shot_tasks_get_data_user_shots_shot_id_tasks200_response_inner import GetShotTasksGetDataUserShotsShotIdTasks200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    shot_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Shot unique identifier

    try:
        # Get shot tasks
        api_response = await api_instance.get_shot_tasks_get_data_user_shots_shot_id_tasks(shot_id)
        print("The response of UserApi->get_shot_tasks_get_data_user_shots_shot_id_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_shot_tasks_get_data_user_shots_shot_id_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | **UUID**| Shot unique identifier | 

### Return type

[**List[GetShotTasksGetDataUserShotsShotIdTasks200ResponseInner]**](GetShotTasksGetDataUserShotsShotIdTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tasks related to given shot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_time_spent_get_data_user_tasks_task_id_time_spents_date**
> GetTaskTimeSpentGetDataUserTasksTaskIdTimeSpentsDate200Response get_task_time_spent_get_data_user_tasks_task_id_time_spents_date(task_id, var_date)

Get task time spent

Retrieve time spent entries for the current user on a specific task and date. Returns detailed time tracking information.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_task_time_spent_get_data_user_tasks_task_id_time_spents_date200_response import GetTaskTimeSpentGetDataUserTasksTaskIdTimeSpentsDate200Response
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Task unique identifier
    var_date = '2023-01-01' # date | Date to get time spent for

    try:
        # Get task time spent
        api_response = await api_instance.get_task_time_spent_get_data_user_tasks_task_id_time_spents_date(task_id, var_date)
        print("The response of UserApi->get_task_time_spent_get_data_user_tasks_task_id_time_spents_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_task_time_spent_get_data_user_tasks_task_id_time_spents_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Task unique identifier | 
 **var_date** | **date**| Date to get time spent for | 

### Return type

[**GetTaskTimeSpentGetDataUserTasksTaskIdTimeSpentsDate200Response**](GetTaskTimeSpentGetDataUserTasksTaskIdTimeSpentsDate200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time spent entry for the current user on given task and date |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_requiring_feedback**
> List[GetTasksRequiringFeedback200ResponseInner] get_tasks_requiring_feedback()

Get tasks requiring feedback

Retrieve tasks requiring feedback for departments where the current user is a supervisor. Returns empty list if user is not a supervisor.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_tasks_requiring_feedback200_response_inner import GetTasksRequiringFeedback200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)

    try:
        # Get tasks requiring feedback
        api_response = await api_instance.get_tasks_requiring_feedback()
        print("The response of UserApi->get_tasks_requiring_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_tasks_requiring_feedback: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetTasksRequiringFeedback200ResponseInner]**](GetTasksRequiringFeedback200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tasks requiring feedback in current user departments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_spents_by_date**
> GetTimeSpentsByDate200Response get_time_spents_by_date(var_date)

Get time spents by date

Retrieve time spent entries for the current user on a specific date. Returns all time entries for the given date.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_time_spents_by_date200_response import GetTimeSpentsByDate200Response
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    var_date = '2023-01-01' # date | Date to get time spents for

    try:
        # Get time spents by date
        api_response = await api_instance.get_time_spents_by_date(var_date)
        print("The response of UserApi->get_time_spents_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_time_spents_by_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**| Date to get time spents for | 

### Return type

[**GetTimeSpentsByDate200Response**](GetTimeSpentsByDate200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time spent entries for the current user on given date |  -  |
**400** | Wrong date format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_spents_get_data_user_time_spents**
> List[GetTimeSpentsGetDataUserTimeSpents200ResponseInner] get_time_spents_get_data_user_time_spents(start_date=start_date, end_date=end_date)

Get time spents

Retrieve all time spent entries for the current user. Optionally accepts date range parameters to filter results.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_time_spents_get_data_user_time_spents200_response_inner import GetTimeSpentsGetDataUserTimeSpents200ResponseInner
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    start_date = '2023-01-01' # date | Start date for filtering time spents (optional)
    end_date = '2023-12-31' # date | End date for filtering time spents (optional)

    try:
        # Get time spents
        api_response = await api_instance.get_time_spents_get_data_user_time_spents(start_date=start_date, end_date=end_date)
        print("The response of UserApi->get_time_spents_get_data_user_time_spents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_time_spents_get_data_user_time_spents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Start date for filtering time spents | [optional] 
 **end_date** | **date**| End date for filtering time spents | [optional] 

### Return type

[**List[GetTimeSpentsGetDataUserTimeSpents200ResponseInner]**](GetTimeSpentsGetDataUserTimeSpents200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time spent entries for the current user |  -  |
**400** | Wrong date format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_chat**
> JoinChat201Response join_chat(entity_id)

Join chat

Join a chat for a specific entity by adding the current user as a participant. The user will be listed as a participant in the chat.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.join_chat201_response import JoinChat201Response
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Entity unique identifier

    try:
        # Join chat
        api_response = await api_instance.join_chat(entity_id)
        print("The response of UserApi->join_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->join_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Entity unique identifier | 

### Return type

[**JoinChat201Response**](JoinChat201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Chat joined successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_chat**
> leave_chat(entity_id)

Leave chat

Leave a chat for a specific entity by removing the current user from participants. The user will no longer receive chat messages for this entity.

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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Entity unique identifier

    try:
        # Leave chat
        await api_instance.leave_chat(entity_id)
    except Exception as e:
        print("Exception when calling UserApi->leave_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Entity unique identifier | 

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
**204** | Chat left successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_all_notifications_as_read**
> MarkAllNotificationsAsRead200Response mark_all_notifications_as_read()

Mark all notifications as read

Mark all notifications as read for the current user.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.mark_all_notifications_as_read200_response import MarkAllNotificationsAsRead200Response
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)

    try:
        # Mark all notifications as read
        api_response = await api_instance.mark_all_notifications_as_read()
        print("The response of UserApi->mark_all_notifications_as_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->mark_all_notifications_as_read: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MarkAllNotificationsAsRead200Response**](MarkAllNotificationsAsRead200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_to_sequence**
> SubscribeToSequence201Response subscribe_to_sequence(sequence_id, task_type_id)

Subscribe to sequence

Create a subscription entry for the current user, given sequence, and task type. When subscribed, the user receives notifications for all comments posted on tasks related to the sequence.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.subscribe_to_sequence201_response import SubscribeToSequence201Response
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Sequence unique identifier
    task_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Task type unique identifier

    try:
        # Subscribe to sequence
        api_response = await api_instance.subscribe_to_sequence(sequence_id, task_type_id)
        print("The response of UserApi->subscribe_to_sequence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->subscribe_to_sequence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**| Sequence unique identifier | 
 **task_type_id** | **UUID**| Task type unique identifier | 

### Return type

[**SubscribeToSequence201Response**](SubscribeToSequence201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Subscription created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_to_task**
> SubscribeToTask201Response subscribe_to_task(task_id)

Subscribe to task

Create a subscription entry for the current user and given task. When subscribed, the user receives notifications for all comments posted on the task.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.subscribe_to_task201_response import SubscribeToTask201Response
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Task unique identifier

    try:
        # Subscribe to task
        api_response = await api_instance.subscribe_to_task(task_id)
        print("The response of UserApi->subscribe_to_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->subscribe_to_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Task unique identifier | 

### Return type

[**SubscribeToTask201Response**](SubscribeToTask201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Subscription created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_from_sequence**
> unsubscribe_from_sequence(sequence_id, task_type_id)

Unsubscribe from sequence

Remove the subscription entry for the current user, given sequence, and task type. The user will no longer receive notifications for tasks related to this sequence.

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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Sequence unique identifier
    task_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Task type unique identifier

    try:
        # Unsubscribe from sequence
        await api_instance.unsubscribe_from_sequence(sequence_id, task_type_id)
    except Exception as e:
        print("Exception when calling UserApi->unsubscribe_from_sequence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**| Sequence unique identifier | 
 **task_type_id** | **UUID**| Task type unique identifier | 

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
**204** | Subscription removed successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_from_task**
> unsubscribe_from_task(task_id)

Unsubscribe from task

Remove the subscription entry for the current user and given task. The user will no longer receive notifications for this task.

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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    task_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Task unique identifier

    try:
        # Unsubscribe from task
        await api_instance.unsubscribe_from_task(task_id)
    except Exception as e:
        print("Exception when calling UserApi->unsubscribe_from_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **UUID**| Task unique identifier | 

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
**204** | Subscription removed successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_filter**
> UpdateFilter200Response update_filter(filter_id, update_filter_request)

Update filter

Update an existing filter if it is owned by the current user.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.update_filter200_response import UpdateFilter200Response
from sometech.pykitsu._client.models.update_filter_request import UpdateFilterRequest
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    filter_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter unique identifier
    update_filter_request = sometech.pykitsu._client.UpdateFilterRequest() # UpdateFilterRequest | 

    try:
        # Update filter
        api_response = await api_instance.update_filter(filter_id, update_filter_request)
        print("The response of UserApi->update_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_filter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **UUID**| Filter unique identifier | 
 **update_filter_request** | [**UpdateFilterRequest**](UpdateFilterRequest.md)|  | 

### Return type

[**UpdateFilter200Response**](UpdateFilter200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filter updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_filter_group**
> UpdateFilterGroup200Response update_filter_group(filter_group_id, update_filter_group_request)

Update filter group

Update an existing filter group if it is owned by the current user. Allows modification of filter group properties.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.update_filter_group200_response import UpdateFilterGroup200Response
from sometech.pykitsu._client.models.update_filter_group_request import UpdateFilterGroupRequest
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    filter_group_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter group unique identifier
    update_filter_group_request = sometech.pykitsu._client.UpdateFilterGroupRequest() # UpdateFilterGroupRequest | 

    try:
        # Update filter group
        api_response = await api_instance.update_filter_group(filter_group_id, update_filter_group_request)
        print("The response of UserApi->update_filter_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_filter_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_group_id** | **UUID**| Filter group unique identifier | 
 **update_filter_group_request** | [**UpdateFilterGroupRequest**](UpdateFilterGroupRequest.md)|  | 

### Return type

[**UpdateFilterGroup200Response**](UpdateFilterGroup200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filter group updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_put_data_user_notifications_notification_id**
> Notification update_notification_put_data_user_notifications_notification_id(notification_id, update_notification_put_data_user_notifications_notification_id_request)

Update notification

Change the read status of a specific notification. Only the notification owner can update their notifications.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.notification import Notification
from sometech.pykitsu._client.models.update_notification_put_data_user_notifications_notification_id_request import UpdateNotificationPutDataUserNotificationsNotificationIdRequest
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
    api_instance = sometech.pykitsu._client.UserApi(api_client)
    notification_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Notification unique identifier
    update_notification_put_data_user_notifications_notification_id_request = sometech.pykitsu._client.UpdateNotificationPutDataUserNotificationsNotificationIdRequest() # UpdateNotificationPutDataUserNotificationsNotificationIdRequest | 

    try:
        # Update notification
        api_response = await api_instance.update_notification_put_data_user_notifications_notification_id(notification_id, update_notification_put_data_user_notifications_notification_id_request)
        print("The response of UserApi->update_notification_put_data_user_notifications_notification_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_notification_put_data_user_notifications_notification_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **UUID**| Notification unique identifier | 
 **update_notification_put_data_user_notifications_notification_id_request** | [**UpdateNotificationPutDataUserNotificationsNotificationIdRequest**](UpdateNotificationPutDataUserNotificationsNotificationIdRequest.md)|  | 

### Return type

[**Notification**](Notification.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notification updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

