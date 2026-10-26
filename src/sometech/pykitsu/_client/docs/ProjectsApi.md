# sometech.pykitsu._client.ProjectsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset_type_to_production**](ProjectsApi.md#add_asset_type_to_production) | **POST** /data/projects/{project_id}/settings/asset-types | Add asset type to production
[**add_person_to_production_team**](ProjectsApi.md#add_person_to_production_team) | **POST** /data/projects/{project_id}/team | Add person to production team
[**add_preview_background_file_to_production**](ProjectsApi.md#add_preview_background_file_to_production) | **POST** /data/projects/{project_id}/settings/preview-background-files | Add preview background file to production
[**add_status_automation_to_production**](ProjectsApi.md#add_status_automation_to_production) | **POST** /data/projects/{project_id}/settings/status-automations | Add status automation to production
[**add_task_status_to_production**](ProjectsApi.md#add_task_status_to_production) | **POST** /data/projects/{project_id}/settings/task-status | Add task status to production
[**add_task_type_to_production**](ProjectsApi.md#add_task_type_to_production) | **POST** /data/projects/{project_id}/settings/task-types | Add task type to production
[**apply_production_schedule_version**](ProjectsApi.md#apply_production_schedule_version) | **POST** /actions/production-schedule-versions/{production_schedule_version_id}/apply-to-production | Apply production schedule version
[**create_budget**](ProjectsApi.md#create_budget) | **POST** /data/projects/{project_id}/budgets | Create budget
[**create_budget_entry**](ProjectsApi.md#create_budget_entry) | **POST** /data/projects/{project_id}/budgets/{budget_id}/entries | Create budget entry
[**create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors**](ProjectsApi.md#create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors) | **POST** /data/projects/{project_id}/metadata-descriptors | Create metadata descriptor
[**delete_budget**](ProjectsApi.md#delete_budget) | **DELETE** /data/projects/{project_id}/budgets/{budget_id} | Delete budget
[**delete_budget_entry**](ProjectsApi.md#delete_budget_entry) | **DELETE** /data/projects/{project_id}/budgets/{budget_id}/entries/{entry_id} | Delete budget entry
[**delete_metadata_descriptor_delete_data_projects_project_id_metadata_descriptors_descriptor_id**](ProjectsApi.md#delete_metadata_descriptor_delete_data_projects_project_id_metadata_descriptors_descriptor_id) | **DELETE** /data/projects/{project_id}/metadata-descriptors/{descriptor_id} | Delete metadata descriptor
[**get_all_projects**](ProjectsApi.md#get_all_projects) | **GET** /data/projects/all | Get all projects
[**get_asset_types_schedule_items**](ProjectsApi.md#get_asset_types_schedule_items) | **GET** /data/projects/{project_id}/schedule-items/{task_type_id}/asset-types | Get asset types schedule items
[**get_budget**](ProjectsApi.md#get_budget) | **GET** /data/projects/{project_id}/budgets/{budget_id} | Get budget
[**get_budget_entries**](ProjectsApi.md#get_budget_entries) | **GET** /data/projects/{project_id}/budgets/{budget_id}/entries | Get budget entries
[**get_budget_entry**](ProjectsApi.md#get_budget_entry) | **GET** /data/projects/{project_id}/budgets/{budget_id}/entries/{entry_id} | Get budget entry
[**get_episodes_schedule_items**](ProjectsApi.md#get_episodes_schedule_items) | **GET** /data/projects/{project_id}/schedule-items/{task_type_id}/episodes | Get episodes schedule items
[**get_metadata_descriptor_get_data_projects_project_id_metadata_descriptors_descriptor_id**](ProjectsApi.md#get_metadata_descriptor_get_data_projects_project_id_metadata_descriptors_descriptor_id) | **GET** /data/projects/{project_id}/metadata-descriptors/{descriptor_id} | Get metadata descriptor
[**get_metadata_descriptors_get_data_projects_project_id_metadata_descriptors**](ProjectsApi.md#get_metadata_descriptors_get_data_projects_project_id_metadata_descriptors) | **GET** /data/projects/{project_id}/metadata-descriptors | Get metadata descriptors
[**get_open_projects_get_data_projects_open**](ProjectsApi.md#get_open_projects_get_data_projects_open) | **GET** /data/projects/open | Get open projects
[**get_production_budgets**](ProjectsApi.md#get_production_budgets) | **GET** /data/projects/{project_id}/budgets | Get production budgets
[**get_production_day_offs**](ProjectsApi.md#get_production_day_offs) | **GET** /data/projects/{project_id}/day-offs | Get production day offs
[**get_production_milestones**](ProjectsApi.md#get_production_milestones) | **GET** /data/projects/{project_id}/milestones | Get production milestones
[**get_production_month_time_spents**](ProjectsApi.md#get_production_month_time_spents) | **GET** /data/projects/{project_id}/budgets/time-spents | Get production month time spents
[**get_production_preview_background_files**](ProjectsApi.md#get_production_preview_background_files) | **GET** /data/projects/{project_id}/settings/preview-background-files | Get production preview background files
[**get_production_schedule_items**](ProjectsApi.md#get_production_schedule_items) | **GET** /data/projects/{project_id}/schedule-items | Get production schedule items
[**get_production_schedule_version_task_links_get_data_production_schedule_versions_production_schedule_version_id_task_links**](ProjectsApi.md#get_production_schedule_version_task_links_get_data_production_schedule_versions_production_schedule_version_id_task_links) | **GET** /data/production-schedule-versions/{production_schedule_version_id}/task-links | Get production schedule version task links
[**get_production_status_automations**](ProjectsApi.md#get_production_status_automations) | **GET** /data/projects/{project_id}/settings/status-automations | Get production status automations
[**get_production_task_statuses**](ProjectsApi.md#get_production_task_statuses) | **GET** /data/projects/{project_id}/settings/task-status | Get production task statuses
[**get_production_task_type_schedule_items**](ProjectsApi.md#get_production_task_type_schedule_items) | **GET** /data/projects/{project_id}/schedule-items/task-types | Get production task type schedule items
[**get_production_task_type_time_spents**](ProjectsApi.md#get_production_task_type_time_spents) | **GET** /data/projects/{project_id}/task-types/{task_type_id}/time-spents | Get production task type time spents
[**get_production_task_types**](ProjectsApi.md#get_production_task_types) | **GET** /data/projects/{project_id}/task-types | Get production task types
[**get_production_team**](ProjectsApi.md#get_production_team) | **GET** /data/projects/{project_id}/team | Get production team
[**get_production_time_spents**](ProjectsApi.md#get_production_time_spents) | **GET** /data/projects/{project_id}/time-spents | Get production time spents
[**get_sequences_schedule_items**](ProjectsApi.md#get_sequences_schedule_items) | **GET** /data/projects/{project_id}/schedule-items/{task_type_id}/sequences | Get sequences schedule items
[**remove_asset_type_from_production**](ProjectsApi.md#remove_asset_type_from_production) | **DELETE** /data/projects/{project_id}/settings/asset-types/{asset_type_id} | Remove asset type from production
[**remove_person_from_production_team**](ProjectsApi.md#remove_person_from_production_team) | **DELETE** /data/projects/{project_id}/team/{person_id} | Remove person from production team
[**remove_preview_background_file_from_production**](ProjectsApi.md#remove_preview_background_file_from_production) | **DELETE** /data/projects/{project_id}/settings/preview-background-files/{preview_background_file_id} | Remove preview background file from production
[**remove_status_automation_from_production**](ProjectsApi.md#remove_status_automation_from_production) | **DELETE** /data/projects/{project_id}/settings/status-automations/{status_automation_id} | Remove status automation from production
[**remove_task_status_from_production**](ProjectsApi.md#remove_task_status_from_production) | **DELETE** /data/projects/{project_id}/settings/task-status/{task_status_id} | Remove task status from production
[**remove_task_type_from_production**](ProjectsApi.md#remove_task_type_from_production) | **DELETE** /data/projects/{project_id}/settings/task-types/{task_type_id} | Remove task type from production
[**reorder_metadata_descriptors**](ProjectsApi.md#reorder_metadata_descriptors) | **POST** /data/projects/{project_id}/metadata-descriptors/reorder | Reorder metadata descriptors
[**set_task_links_from_production_schedule_version**](ProjectsApi.md#set_task_links_from_production_schedule_version) | **POST** /actions/production-schedule-versions/{production_schedule_version_id}/set-task-links-from-production-schedule-version | Set task links from production schedule version
[**set_task_links_from_tasks**](ProjectsApi.md#set_task_links_from_tasks) | **POST** /actions/production-schedule-versions/{production_schedule_version_id}/set-task-links-from-production | Set task links from tasks
[**update_budget**](ProjectsApi.md#update_budget) | **PUT** /data/projects/{project_id}/budgets/{budget_id} | Update budget
[**update_budget_entry**](ProjectsApi.md#update_budget_entry) | **PUT** /data/projects/{project_id}/budgets/{budget_id}/entries/{entry_id} | Update budget entry
[**update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id**](ProjectsApi.md#update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id) | **PUT** /data/projects/{project_id}/metadata-descriptors/{descriptor_id} | Update metadata descriptor


# **add_asset_type_to_production**
> AddPersonToProductionTeam201Response add_asset_type_to_production(project_id, add_asset_type_to_production_request)

Add asset type to production

Add an asset type linked to a production.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_asset_type_to_production_request import AddAssetTypeToProductionRequest
from sometech.pykitsu._client.models.add_person_to_production_team201_response import AddPersonToProductionTeam201Response
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    add_asset_type_to_production_request = sometech.pykitsu._client.AddAssetTypeToProductionRequest() # AddAssetTypeToProductionRequest | 

    try:
        # Add asset type to production
        api_response = await api_instance.add_asset_type_to_production(project_id, add_asset_type_to_production_request)
        print("The response of ProjectsApi->add_asset_type_to_production:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_asset_type_to_production: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **add_asset_type_to_production_request** | [**AddAssetTypeToProductionRequest**](AddAssetTypeToProductionRequest.md)|  | 

### Return type

[**AddPersonToProductionTeam201Response**](AddPersonToProductionTeam201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Asset type added to production |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_person_to_production_team**
> AddPersonToProductionTeam201Response add_person_to_production_team(project_id, add_person_to_production_team_request)

Add person to production team

Add a person to a production team.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_person_to_production_team201_response import AddPersonToProductionTeam201Response
from sometech.pykitsu._client.models.add_person_to_production_team_request import AddPersonToProductionTeamRequest
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    add_person_to_production_team_request = sometech.pykitsu._client.AddPersonToProductionTeamRequest() # AddPersonToProductionTeamRequest | 

    try:
        # Add person to production team
        api_response = await api_instance.add_person_to_production_team(project_id, add_person_to_production_team_request)
        print("The response of ProjectsApi->add_person_to_production_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_person_to_production_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **add_person_to_production_team_request** | [**AddPersonToProductionTeamRequest**](AddPersonToProductionTeamRequest.md)|  | 

### Return type

[**AddPersonToProductionTeam201Response**](AddPersonToProductionTeam201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Person added to the production team |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_preview_background_file_to_production**
> AddPersonToProductionTeam201Response add_preview_background_file_to_production(project_id, add_preview_background_file_to_production_request)

Add preview background file to production

Add a preview background file linked to a production.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_person_to_production_team201_response import AddPersonToProductionTeam201Response
from sometech.pykitsu._client.models.add_preview_background_file_to_production_request import AddPreviewBackgroundFileToProductionRequest
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    add_preview_background_file_to_production_request = sometech.pykitsu._client.AddPreviewBackgroundFileToProductionRequest() # AddPreviewBackgroundFileToProductionRequest | 

    try:
        # Add preview background file to production
        api_response = await api_instance.add_preview_background_file_to_production(project_id, add_preview_background_file_to_production_request)
        print("The response of ProjectsApi->add_preview_background_file_to_production:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_preview_background_file_to_production: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **add_preview_background_file_to_production_request** | [**AddPreviewBackgroundFileToProductionRequest**](AddPreviewBackgroundFileToProductionRequest.md)|  | 

### Return type

[**AddPersonToProductionTeam201Response**](AddPersonToProductionTeam201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Preview background file added to production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_status_automation_to_production**
> AddPersonToProductionTeam201Response add_status_automation_to_production(project_id, add_status_automation_to_production_request)

Add status automation to production

Add a status automation linked to a production.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_person_to_production_team201_response import AddPersonToProductionTeam201Response
from sometech.pykitsu._client.models.add_status_automation_to_production_request import AddStatusAutomationToProductionRequest
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    add_status_automation_to_production_request = sometech.pykitsu._client.AddStatusAutomationToProductionRequest() # AddStatusAutomationToProductionRequest | 

    try:
        # Add status automation to production
        api_response = await api_instance.add_status_automation_to_production(project_id, add_status_automation_to_production_request)
        print("The response of ProjectsApi->add_status_automation_to_production:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_status_automation_to_production: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **add_status_automation_to_production_request** | [**AddStatusAutomationToProductionRequest**](AddStatusAutomationToProductionRequest.md)|  | 

### Return type

[**AddPersonToProductionTeam201Response**](AddPersonToProductionTeam201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Status automation added to production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_task_status_to_production**
> AddPersonToProductionTeam201Response add_task_status_to_production(project_id, add_task_status_to_production_request)

Add task status to production

Add a task status linked to a production.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_person_to_production_team201_response import AddPersonToProductionTeam201Response
from sometech.pykitsu._client.models.add_task_status_to_production_request import AddTaskStatusToProductionRequest
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    add_task_status_to_production_request = sometech.pykitsu._client.AddTaskStatusToProductionRequest() # AddTaskStatusToProductionRequest | 

    try:
        # Add task status to production
        api_response = await api_instance.add_task_status_to_production(project_id, add_task_status_to_production_request)
        print("The response of ProjectsApi->add_task_status_to_production:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_task_status_to_production: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **add_task_status_to_production_request** | [**AddTaskStatusToProductionRequest**](AddTaskStatusToProductionRequest.md)|  | 

### Return type

[**AddPersonToProductionTeam201Response**](AddPersonToProductionTeam201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Task status added to production |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_task_type_to_production**
> AddPersonToProductionTeam201Response add_task_type_to_production(project_id, add_task_type_to_production_request)

Add task type to production

Add a task type linked to a production.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_person_to_production_team201_response import AddPersonToProductionTeam201Response
from sometech.pykitsu._client.models.add_task_type_to_production_request import AddTaskTypeToProductionRequest
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    add_task_type_to_production_request = sometech.pykitsu._client.AddTaskTypeToProductionRequest() # AddTaskTypeToProductionRequest | 

    try:
        # Add task type to production
        api_response = await api_instance.add_task_type_to_production(project_id, add_task_type_to_production_request)
        print("The response of ProjectsApi->add_task_type_to_production:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_task_type_to_production: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **add_task_type_to_production_request** | [**AddTaskTypeToProductionRequest**](AddTaskTypeToProductionRequest.md)|  | 

### Return type

[**AddPersonToProductionTeam201Response**](AddPersonToProductionTeam201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Task type added to production |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_production_schedule_version**
> object apply_production_schedule_version(production_schedule_version_id)

Apply production schedule version

Apply production schedule version to production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    production_schedule_version_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Production schedule version unique identifier

    try:
        # Apply production schedule version
        api_response = await api_instance.apply_production_schedule_version(production_schedule_version_id)
        print("The response of ProjectsApi->apply_production_schedule_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->apply_production_schedule_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_schedule_version_id** | **UUID**| Production schedule version unique identifier | 

### Return type

**object**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Production schedule version applied |  -  |
**400** | Wrong ID format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_budget**
> CreateBudget201Response create_budget(project_id, create_budget_request)

Create budget

Create a budget for given production.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_budget201_response import CreateBudget201Response
from sometech.pykitsu._client.models.create_budget_request import CreateBudgetRequest
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    create_budget_request = sometech.pykitsu._client.CreateBudgetRequest() # CreateBudgetRequest | 

    try:
        # Create budget
        api_response = await api_instance.create_budget(project_id, create_budget_request)
        print("The response of ProjectsApi->create_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **create_budget_request** | [**CreateBudgetRequest**](CreateBudgetRequest.md)|  | 

### Return type

[**CreateBudget201Response**](CreateBudget201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Budget created |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_budget_entry**
> CreateBudgetEntry201Response create_budget_entry(project_id, budget_id, create_budget_entry_request)

Create budget entry

Create a budget entry for given production and budget.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_budget_entry201_response import CreateBudgetEntry201Response
from sometech.pykitsu._client.models.create_budget_entry_request import CreateBudgetEntryRequest
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    budget_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Budget unique identifier
    create_budget_entry_request = sometech.pykitsu._client.CreateBudgetEntryRequest() # CreateBudgetEntryRequest | 

    try:
        # Create budget entry
        api_response = await api_instance.create_budget_entry(project_id, budget_id, create_budget_entry_request)
        print("The response of ProjectsApi->create_budget_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_budget_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **budget_id** | **UUID**| Budget unique identifier | 
 **create_budget_entry_request** | [**CreateBudgetEntryRequest**](CreateBudgetEntryRequest.md)|  | 

### Return type

[**CreateBudgetEntry201Response**](CreateBudgetEntry201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Budget entry created |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors**
> CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptors201Response create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors(project_id, create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors_request)

Create metadata descriptor

Create a new metadata descriptor. It serves to describe extra fields listed in the data attribute of entities.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors201_response import CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptors201Response
from sometech.pykitsu._client.models.create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors_request import CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptorsRequest
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors_request = sometech.pykitsu._client.CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptorsRequest() # CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptorsRequest | 

    try:
        # Create metadata descriptor
        api_response = await api_instance.create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors(project_id, create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors_request)
        print("The response of ProjectsApi->create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors_request** | [**CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptorsRequest**](CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptorsRequest.md)|  | 

### Return type

[**CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptors201Response**](CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptors201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Metadata descriptor created |  -  |
**400** | Invalid parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_budget**
> delete_budget(project_id, budget_id)

Delete budget

Delete a budget for given production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    budget_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Budget unique identifier

    try:
        # Delete budget
        await api_instance.delete_budget(project_id, budget_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **budget_id** | **UUID**| Budget unique identifier | 

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
**204** | Budget deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_budget_entry**
> delete_budget_entry(project_id, budget_id, entry_id)

Delete budget entry

Delete a budget entry for given production and budget.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    budget_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Budget unique identifier
    entry_id = UUID('c46c8gc6-eg97-6887-c292-79675204e47') # UUID | Budget entry unique identifier

    try:
        # Delete budget entry
        await api_instance.delete_budget_entry(project_id, budget_id, entry_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_budget_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **budget_id** | **UUID**| Budget unique identifier | 
 **entry_id** | **UUID**| Budget entry unique identifier | 

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
**204** | Budget entry deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata_descriptor_delete_data_projects_project_id_metadata_descriptors_descriptor_id**
> delete_metadata_descriptor_delete_data_projects_project_id_metadata_descriptors_descriptor_id(project_id, descriptor_id)

Delete metadata descriptor

Delete a metadata descriptor. Descriptors serve to describe extra fields listed in the data attribute of entities.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    descriptor_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Metadata descriptor unique identifier

    try:
        # Delete metadata descriptor
        await api_instance.delete_metadata_descriptor_delete_data_projects_project_id_metadata_descriptors_descriptor_id(project_id, descriptor_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_metadata_descriptor_delete_data_projects_project_id_metadata_descriptors_descriptor_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **descriptor_id** | **UUID**| Metadata descriptor unique identifier | 

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
**204** | Metadata descriptor deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_projects**
> List[GetOpenProjectsGetDataProjectsOpen200ResponseInner] get_all_projects(name=name)

Get all projects

Return all projects listed in database. Ensure that user has at least the manager level before that.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_open_projects_get_data_projects_open200_response_inner import GetOpenProjectsGetDataProjectsOpen200ResponseInner
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    name = 'My Project' # str | Filter projects by name (optional)

    try:
        # Get all projects
        api_response = await api_instance.get_all_projects(name=name)
        print("The response of ProjectsApi->get_all_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_all_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter projects by name | [optional] 

### Return type

[**List[GetOpenProjectsGetDataProjectsOpen200ResponseInner]**](GetOpenProjectsGetDataProjectsOpen200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All projects listed in database |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_types_schedule_items**
> List[object] get_asset_types_schedule_items(project_id, task_type_id)

Get asset types schedule items

Retrieve asset types schedule items for given task type.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    task_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Task type unique identifier

    try:
        # Get asset types schedule items
        api_response = await api_instance.get_asset_types_schedule_items(project_id, task_type_id)
        print("The response of ProjectsApi->get_asset_types_schedule_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_asset_types_schedule_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **task_type_id** | **UUID**| Task type unique identifier | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All asset types schedule items for given task type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget**
> object get_budget(project_id, budget_id)

Get budget

Retrieve a budget for given production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    budget_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Budget unique identifier

    try:
        # Get budget
        api_response = await api_instance.get_budget(project_id, budget_id)
        print("The response of ProjectsApi->get_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **budget_id** | **UUID**| Budget unique identifier | 

### Return type

**object**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Budget retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_entries**
> List[object] get_budget_entries(project_id, budget_id)

Get budget entries

Retrieve budget entries for given production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    budget_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Budget unique identifier

    try:
        # Get budget entries
        api_response = await api_instance.get_budget_entries(project_id, budget_id)
        print("The response of ProjectsApi->get_budget_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_budget_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **budget_id** | **UUID**| Budget unique identifier | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All budget entries of given production and budget |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_entry**
> object get_budget_entry(project_id, budget_id, entry_id)

Get budget entry

Retrieve a budget entry for given production and budget.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    budget_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Budget unique identifier
    entry_id = UUID('c46c8gc6-eg97-6887-c292-79675204e47') # UUID | Budget entry unique identifier

    try:
        # Get budget entry
        api_response = await api_instance.get_budget_entry(project_id, budget_id, entry_id)
        print("The response of ProjectsApi->get_budget_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_budget_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **budget_id** | **UUID**| Budget unique identifier | 
 **entry_id** | **UUID**| Budget entry unique identifier | 

### Return type

**object**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Budget entry retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episodes_schedule_items**
> List[object] get_episodes_schedule_items(project_id, task_type_id)

Get episodes schedule items

Retrieve episodes schedule items for given task type.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    task_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Task type unique identifier

    try:
        # Get episodes schedule items
        api_response = await api_instance.get_episodes_schedule_items(project_id, task_type_id)
        print("The response of ProjectsApi->get_episodes_schedule_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_episodes_schedule_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **task_type_id** | **UUID**| Task type unique identifier | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All episodes schedule items for given task type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_descriptor_get_data_projects_project_id_metadata_descriptors_descriptor_id**
> object get_metadata_descriptor_get_data_projects_project_id_metadata_descriptors_descriptor_id(project_id, descriptor_id)

Get metadata descriptor

Get a metadata descriptor. Descriptors serve to describe extra fields listed in the data attribute of entities.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    descriptor_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Metadata descriptor unique identifier

    try:
        # Get metadata descriptor
        api_response = await api_instance.get_metadata_descriptor_get_data_projects_project_id_metadata_descriptors_descriptor_id(project_id, descriptor_id)
        print("The response of ProjectsApi->get_metadata_descriptor_get_data_projects_project_id_metadata_descriptors_descriptor_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_metadata_descriptor_get_data_projects_project_id_metadata_descriptors_descriptor_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **descriptor_id** | **UUID**| Metadata descriptor unique identifier | 

### Return type

**object**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata descriptor |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_descriptors_get_data_projects_project_id_metadata_descriptors**
> List[object] get_metadata_descriptors_get_data_projects_project_id_metadata_descriptors(project_id)

Get metadata descriptors

Get all metadata descriptors. It serves to describe extra fields listed in the data attribute of entities.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get metadata descriptors
        api_response = await api_instance.get_metadata_descriptors_get_data_projects_project_id_metadata_descriptors(project_id)
        print("The response of ProjectsApi->get_metadata_descriptors_get_data_projects_project_id_metadata_descriptors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_metadata_descriptors_get_data_projects_project_id_metadata_descriptors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All metadata descriptors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_projects_get_data_projects_open**
> List[GetOpenProjectsGetDataProjectsOpen200ResponseInner] get_open_projects_get_data_projects_open(name=name)

Get open projects

Return the list of projects currently running. Most of the time, past projects are not needed.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_open_projects_get_data_projects_open200_response_inner import GetOpenProjectsGetDataProjectsOpen200ResponseInner
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    name = 'My Project' # str | Filter projects by name (optional)

    try:
        # Get open projects
        api_response = await api_instance.get_open_projects_get_data_projects_open(name=name)
        print("The response of ProjectsApi->get_open_projects_get_data_projects_open:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_open_projects_get_data_projects_open: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter projects by name | [optional] 

### Return type

[**List[GetOpenProjectsGetDataProjectsOpen200ResponseInner]**](GetOpenProjectsGetDataProjectsOpen200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All running projects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_budgets**
> List[object] get_production_budgets(project_id)

Get production budgets

Retrieve budgets for given production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get production budgets
        api_response = await api_instance.get_production_budgets(project_id)
        print("The response of ProjectsApi->get_production_budgets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_production_budgets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All budgets of given production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_day_offs**
> List[GetProductionDayOffs200ResponseInner] get_production_day_offs(project_id, start_date=start_date, end_date=end_date)

Get production day offs

Retrieve all day offs for a production.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_production_day_offs200_response_inner import GetProductionDayOffs200ResponseInner
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    start_date = '2022-07-01' # date | Start date for filtering day offs (optional)
    end_date = '2022-07-31' # date | End date for filtering day offs (optional)

    try:
        # Get production day offs
        api_response = await api_instance.get_production_day_offs(project_id, start_date=start_date, end_date=end_date)
        print("The response of ProjectsApi->get_production_day_offs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_production_day_offs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **start_date** | **date**| Start date for filtering day offs | [optional] 
 **end_date** | **date**| End date for filtering day offs | [optional] 

### Return type

[**List[GetProductionDayOffs200ResponseInner]**](GetProductionDayOffs200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All day offs for given project |  -  |
**400** | Invalid date range parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_milestones**
> List[object] get_production_milestones(project_id)

Get production milestones

Retrieve milestones for given production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get production milestones
        api_response = await api_instance.get_production_milestones(project_id)
        print("The response of ProjectsApi->get_production_milestones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_production_milestones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All milestones of given production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_month_time_spents**
> object get_production_month_time_spents(project_id)

Get production month time spents

Get aggregated time spents by month for given project.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get production month time spents
        api_response = await api_instance.get_production_month_time_spents(project_id)
        print("The response of ProjectsApi->get_production_month_time_spents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_production_month_time_spents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

**object**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Aggregated time spents for given project and month |  -  |
**400** | Wrong ID format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_preview_background_files**
> List[object] get_production_preview_background_files(project_id)

Get production preview background files

Return preview background files linked to a production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get production preview background files
        api_response = await api_instance.get_production_preview_background_files(project_id)
        print("The response of ProjectsApi->get_production_preview_background_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_production_preview_background_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preview background files linked to production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_schedule_items**
> List[object] get_production_schedule_items(project_id)

Get production schedule items

Retrieve schedule items for given production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get production schedule items
        api_response = await api_instance.get_production_schedule_items(project_id)
        print("The response of ProjectsApi->get_production_schedule_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_production_schedule_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All schedule items of given production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_schedule_version_task_links_get_data_production_schedule_versions_production_schedule_version_id_task_links**
> List[object] get_production_schedule_version_task_links_get_data_production_schedule_versions_production_schedule_version_id_task_links(production_schedule_version_id, task_type_id=task_type_id)

Get production schedule version task links

Get task links for given production schedule version.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    production_schedule_version_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Production schedule version unique identifier
    task_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Task type unique identifier for filtering (optional)

    try:
        # Get production schedule version task links
        api_response = await api_instance.get_production_schedule_version_task_links_get_data_production_schedule_versions_production_schedule_version_id_task_links(production_schedule_version_id, task_type_id=task_type_id)
        print("The response of ProjectsApi->get_production_schedule_version_task_links_get_data_production_schedule_versions_production_schedule_version_id_task_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_production_schedule_version_task_links_get_data_production_schedule_versions_production_schedule_version_id_task_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_schedule_version_id** | **UUID**| Production schedule version unique identifier | 
 **task_type_id** | **UUID**| Task type unique identifier for filtering | [optional] 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task links for given production schedule version |  -  |
**400** | Wrong ID format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_status_automations**
> List[object] get_production_status_automations(project_id)

Get production status automations

Get status automations linked to a production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get production status automations
        api_response = await api_instance.get_production_status_automations(project_id)
        print("The response of ProjectsApi->get_production_status_automations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_production_status_automations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status automations linked to production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_task_statuses**
> List[object] get_production_task_statuses(project_id)

Get production task statuses

Return task statuses linked to a production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get production task statuses
        api_response = await api_instance.get_production_task_statuses(project_id)
        print("The response of ProjectsApi->get_production_task_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_production_task_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task statuses linked to production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_task_type_schedule_items**
> List[object] get_production_task_type_schedule_items(project_id)

Get production task type schedule items

Retrieve task type schedule items for given production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get production task type schedule items
        api_response = await api_instance.get_production_task_type_schedule_items(project_id)
        print("The response of ProjectsApi->get_production_task_type_schedule_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_production_task_type_schedule_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All task types schedule items of given production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_task_type_time_spents**
> List[GetProductionTaskTypeTimeSpents200ResponseInner] get_production_task_type_time_spents(project_id, task_type_id, start_date=start_date, end_date=end_date)

Get production task type time spents

Retrieve time spents for a task type in the production.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_production_task_type_time_spents200_response_inner import GetProductionTaskTypeTimeSpents200ResponseInner
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    task_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Task type unique identifier
    start_date = '2022-07-01' # date | Start date for filtering time spents (optional)
    end_date = '2022-07-31' # date | End date for filtering time spents (optional)

    try:
        # Get production task type time spents
        api_response = await api_instance.get_production_task_type_time_spents(project_id, task_type_id, start_date=start_date, end_date=end_date)
        print("The response of ProjectsApi->get_production_task_type_time_spents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_production_task_type_time_spents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **task_type_id** | **UUID**| Task type unique identifier | 
 **start_date** | **date**| Start date for filtering time spents | [optional] 
 **end_date** | **date**| End date for filtering time spents | [optional] 

### Return type

[**List[GetProductionTaskTypeTimeSpents200ResponseInner]**](GetProductionTaskTypeTimeSpents200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All time spents for given task type and project |  -  |
**400** | Invalid date range parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_task_types**
> List[object] get_production_task_types(project_id)

Get production task types

Retrieve task types linked to the production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get production task types
        api_response = await api_instance.get_production_task_types(project_id)
        print("The response of ProjectsApi->get_production_task_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_production_task_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task types linked to the production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_team**
> List[GetProductionTeam200ResponseInner] get_production_team(project_id)

Get production team

Return the people listed in a production team.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_production_team200_response_inner import GetProductionTeam200ResponseInner
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get production team
        api_response = await api_instance.get_production_team(project_id)
        print("The response of ProjectsApi->get_production_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_production_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

[**List[GetProductionTeam200ResponseInner]**](GetProductionTeam200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | People listed in a production team |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_production_time_spents**
> List[object] get_production_time_spents(project_id)

Get production time spents

Retrieve time spents for given production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get production time spents
        api_response = await api_instance.get_production_time_spents(project_id)
        print("The response of ProjectsApi->get_production_time_spents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_production_time_spents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All time spents of given production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequences_schedule_items**
> List[object] get_sequences_schedule_items(project_id, task_type_id)

Get sequences schedule items

Retrieve sequences schedule items for given task type.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    task_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Task type unique identifier

    try:
        # Get sequences schedule items
        api_response = await api_instance.get_sequences_schedule_items(project_id, task_type_id)
        print("The response of ProjectsApi->get_sequences_schedule_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_sequences_schedule_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **task_type_id** | **UUID**| Task type unique identifier | 

### Return type

**List[object]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All sequences schedule items for given task type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_asset_type_from_production**
> remove_asset_type_from_production(project_id, asset_type_id)

Remove asset type from production

Remove an asset type from a production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    asset_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Asset type unique identifier

    try:
        # Remove asset type from production
        await api_instance.remove_asset_type_from_production(project_id, asset_type_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->remove_asset_type_from_production: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **asset_type_id** | **UUID**| Asset type unique identifier | 

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
**204** | Asset type removed from production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_person_from_production_team**
> remove_person_from_production_team(project_id, person_id)

Remove person from production team

Remove people listed in a production team.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    person_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Person unique identifier

    try:
        # Remove person from production team
        await api_instance.remove_person_from_production_team(project_id, person_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->remove_person_from_production_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **person_id** | **UUID**| Person unique identifier | 

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
**204** | Person removed from production team |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_preview_background_file_from_production**
> remove_preview_background_file_from_production(project_id, preview_background_file_id)

Remove preview background file from production

Remove a preview background file from a production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    preview_background_file_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Preview background file unique identifier

    try:
        # Remove preview background file from production
        await api_instance.remove_preview_background_file_from_production(project_id, preview_background_file_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->remove_preview_background_file_from_production: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **preview_background_file_id** | **UUID**| Preview background file unique identifier | 

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
**204** | Preview background file removed from production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_status_automation_from_production**
> remove_status_automation_from_production(project_id, status_automation_id)

Remove status automation from production

Remove a status automation from a production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    status_automation_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Status automation unique identifier

    try:
        # Remove status automation from production
        await api_instance.remove_status_automation_from_production(project_id, status_automation_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->remove_status_automation_from_production: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **status_automation_id** | **UUID**| Status automation unique identifier | 

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
**204** | Status automation removed from production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_task_status_from_production**
> remove_task_status_from_production(project_id, task_status_id)

Remove task status from production

Remove a task status from a production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    task_status_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Task status unique identifier

    try:
        # Remove task status from production
        await api_instance.remove_task_status_from_production(project_id, task_status_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->remove_task_status_from_production: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **task_status_id** | **UUID**| Task status unique identifier | 

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
**204** | Task status removed from production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_task_type_from_production**
> remove_task_type_from_production(project_id, task_type_id)

Remove task type from production

Remove a task type from a production.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    task_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Task type unique identifier

    try:
        # Remove task type from production
        await api_instance.remove_task_type_from_production(project_id, task_type_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->remove_task_type_from_production: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
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
**204** | Task type removed from production |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reorder_metadata_descriptors**
> List[ReorderMetadataDescriptors200ResponseInner] reorder_metadata_descriptors(project_id, reorder_metadata_descriptors_request)

Reorder metadata descriptors

Reorder metadata descriptors for a specific entity type and project. Descriptors are reordered based on the list of descriptor IDs provided in the request body. Position is set according to the order in the list.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.reorder_metadata_descriptors200_response_inner import ReorderMetadataDescriptors200ResponseInner
from sometech.pykitsu._client.models.reorder_metadata_descriptors_request import ReorderMetadataDescriptorsRequest
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    reorder_metadata_descriptors_request = sometech.pykitsu._client.ReorderMetadataDescriptorsRequest() # ReorderMetadataDescriptorsRequest | 

    try:
        # Reorder metadata descriptors
        api_response = await api_instance.reorder_metadata_descriptors(project_id, reorder_metadata_descriptors_request)
        print("The response of ProjectsApi->reorder_metadata_descriptors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->reorder_metadata_descriptors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **reorder_metadata_descriptors_request** | [**ReorderMetadataDescriptorsRequest**](ReorderMetadataDescriptorsRequest.md)|  | 

### Return type

[**List[ReorderMetadataDescriptors200ResponseInner]**](ReorderMetadataDescriptors200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata descriptors reordered successfully |  -  |
**400** | Invalid parameters or descriptor not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_task_links_from_production_schedule_version**
> object set_task_links_from_production_schedule_version(production_schedule_version_id, set_task_links_from_production_schedule_version_request)

Set task links from production schedule version

Set task links for given production schedule version from another production schedule version.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.set_task_links_from_production_schedule_version_request import SetTaskLinksFromProductionScheduleVersionRequest
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    production_schedule_version_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Production schedule version unique identifier
    set_task_links_from_production_schedule_version_request = sometech.pykitsu._client.SetTaskLinksFromProductionScheduleVersionRequest() # SetTaskLinksFromProductionScheduleVersionRequest | 

    try:
        # Set task links from production schedule version
        api_response = await api_instance.set_task_links_from_production_schedule_version(production_schedule_version_id, set_task_links_from_production_schedule_version_request)
        print("The response of ProjectsApi->set_task_links_from_production_schedule_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->set_task_links_from_production_schedule_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_schedule_version_id** | **UUID**| Production schedule version unique identifier | 
 **set_task_links_from_production_schedule_version_request** | [**SetTaskLinksFromProductionScheduleVersionRequest**](SetTaskLinksFromProductionScheduleVersionRequest.md)|  | 

### Return type

**object**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task links created |  -  |
**400** | Wrong ID format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_task_links_from_tasks**
> object set_task_links_from_tasks(production_schedule_version_id)

Set task links from tasks

Set task links for given production schedule version from tasks.

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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    production_schedule_version_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Production schedule version unique identifier

    try:
        # Set task links from tasks
        api_response = await api_instance.set_task_links_from_tasks(production_schedule_version_id)
        print("The response of ProjectsApi->set_task_links_from_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->set_task_links_from_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **production_schedule_version_id** | **UUID**| Production schedule version unique identifier | 

### Return type

**object**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task links created |  -  |
**400** | Wrong ID format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_budget**
> object update_budget(project_id, budget_id, update_budget_request)

Update budget

Update a budget for given production.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.update_budget_request import UpdateBudgetRequest
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    budget_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Budget unique identifier
    update_budget_request = sometech.pykitsu._client.UpdateBudgetRequest() # UpdateBudgetRequest | 

    try:
        # Update budget
        api_response = await api_instance.update_budget(project_id, budget_id, update_budget_request)
        print("The response of ProjectsApi->update_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **budget_id** | **UUID**| Budget unique identifier | 
 **update_budget_request** | [**UpdateBudgetRequest**](UpdateBudgetRequest.md)|  | 

### Return type

**object**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Budget updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_budget_entry**
> object update_budget_entry(project_id, budget_id, entry_id, update_budget_entry_request)

Update budget entry

Update a budget entry for given production and budget.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.update_budget_entry_request import UpdateBudgetEntryRequest
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    budget_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Budget unique identifier
    entry_id = UUID('c46c8gc6-eg97-6887-c292-79675204e47') # UUID | Budget entry unique identifier
    update_budget_entry_request = sometech.pykitsu._client.UpdateBudgetEntryRequest() # UpdateBudgetEntryRequest | 

    try:
        # Update budget entry
        api_response = await api_instance.update_budget_entry(project_id, budget_id, entry_id, update_budget_entry_request)
        print("The response of ProjectsApi->update_budget_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_budget_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **budget_id** | **UUID**| Budget unique identifier | 
 **entry_id** | **UUID**| Budget entry unique identifier | 
 **update_budget_entry_request** | [**UpdateBudgetEntryRequest**](UpdateBudgetEntryRequest.md)|  | 

### Return type

**object**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Budget entry updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id**
> object update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id(project_id, descriptor_id, update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id_request)

Update metadata descriptor

Update a metadata descriptor. Descriptors serve to describe extra fields listed in the data attribute of entities.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id_request import UpdateMetadataDescriptorPutDataProjectsProjectIdMetadataDescriptorsDescriptorIdRequest
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
    api_instance = sometech.pykitsu._client.ProjectsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    descriptor_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Metadata descriptor unique identifier
    update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id_request = sometech.pykitsu._client.UpdateMetadataDescriptorPutDataProjectsProjectIdMetadataDescriptorsDescriptorIdRequest() # UpdateMetadataDescriptorPutDataProjectsProjectIdMetadataDescriptorsDescriptorIdRequest | 

    try:
        # Update metadata descriptor
        api_response = await api_instance.update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id(project_id, descriptor_id, update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id_request)
        print("The response of ProjectsApi->update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **descriptor_id** | **UUID**| Metadata descriptor unique identifier | 
 **update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id_request** | [**UpdateMetadataDescriptorPutDataProjectsProjectIdMetadataDescriptorsDescriptorIdRequest**](UpdateMetadataDescriptorPutDataProjectsProjectIdMetadataDescriptorsDescriptorIdRequest.md)|  | 

### Return type

**object**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata descriptor updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

