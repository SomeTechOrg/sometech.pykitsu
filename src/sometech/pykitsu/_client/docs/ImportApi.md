# sometech.pykitsu._client.ImportApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shotgun_import_error**](ImportApi.md#create_shotgun_import_error) | **POST** /import/shotgun/errors | Create shotgun import error
[**delete_shotgun_import_error**](ImportApi.md#delete_shotgun_import_error) | **DELETE** /import/shotgun/errors/{error_id} | Delete shotgun import error
[**get_shotgun_import_errors**](ImportApi.md#get_shotgun_import_errors) | **GET** /import/shotgun/errors | Get shotgun import errors
[**import_assets_csv**](ImportApi.md#import_assets_csv) | **POST** /import/csv/projects/{project_id}/assets | Import assets csv
[**import_casting_csv**](ImportApi.md#import_casting_csv) | **POST** /import/csv/projects/{project_id}/casting | Import casting csv
[**import_edits_csv**](ImportApi.md#import_edits_csv) | **POST** /import/csv/projects/{project_id}/edits | Import edits csv
[**import_episode_otio**](ImportApi.md#import_episode_otio) | **POST** /import/otio/projects/{project_id}/episodes/{episode_id} | Import episode otio
[**import_episode_task_type_estimations_csv**](ImportApi.md#import_episode_task_type_estimations_csv) | **POST** /import/csv/projects/{project_id}/episodes/{episode_id}/task-types/{task_type_id}/estimations | Import episode task type estimations csv
[**import_kitsu_comments**](ImportApi.md#import_kitsu_comments) | **POST** /import/kitsu/comments | Import kitsu comments
[**import_kitsu_entities**](ImportApi.md#import_kitsu_entities) | **POST** /import/kitsu/entities | Import kitsu entities
[**import_kitsu_entity_links**](ImportApi.md#import_kitsu_entity_links) | **POST** /import/kitsu/entity-links | Import kitsu entity links
[**import_kitsu_projects**](ImportApi.md#import_kitsu_projects) | **POST** /import/kitsu/projects | Import kitsu projects
[**import_kitsu_tasks**](ImportApi.md#import_kitsu_tasks) | **POST** /import/kitsu/tasks | Import kitsu tasks
[**import_otio_edl**](ImportApi.md#import_otio_edl) | **POST** /import/otio/projects/{project_id} | Import otio EDL
[**import_persons_csv**](ImportApi.md#import_persons_csv) | **POST** /import/csv/persons | Import persons csv
[**import_shotgun_assets**](ImportApi.md#import_shotgun_assets) | **POST** /import/shotgun/assets | Import shotgun assets
[**import_shotgun_episodes**](ImportApi.md#import_shotgun_episodes) | **POST** /import/shotgun/episodes | Import shotgun episodes
[**import_shotgun_notes**](ImportApi.md#import_shotgun_notes) | **POST** /import/shotgun/notes | Import shotgun notes
[**import_shotgun_persons**](ImportApi.md#import_shotgun_persons) | **POST** /import/shotgun/persons | Import shotgun persons
[**import_shotgun_project_connections**](ImportApi.md#import_shotgun_project_connections) | **POST** /import/shotgun/projectconnections | Import shotgun project connections
[**import_shotgun_projects**](ImportApi.md#import_shotgun_projects) | **POST** /import/shotgun/projects | Import shotgun projects
[**import_shotgun_scenes**](ImportApi.md#import_shotgun_scenes) | **POST** /import/shotgun/scenes | Import shotgun scenes
[**import_shotgun_sequences**](ImportApi.md#import_shotgun_sequences) | **POST** /import/shotgun/sequences | Import shotgun sequences
[**import_shotgun_shots**](ImportApi.md#import_shotgun_shots) | **POST** /import/shotgun/shots | Import shotgun shots
[**import_shotgun_steps**](ImportApi.md#import_shotgun_steps) | **POST** /import/shotgun/steps | Import shotgun steps
[**import_shotgun_task_statuses**](ImportApi.md#import_shotgun_task_statuses) | **POST** /import/shotgun/status | Import shotgun task statuses
[**import_shotgun_tasks**](ImportApi.md#import_shotgun_tasks) | **POST** /import/shotgun/tasks | Import shotgun tasks
[**import_shotgun_versions**](ImportApi.md#import_shotgun_versions) | **POST** /import/shotgun/versions | Import shotgun versions
[**import_shots_csv**](ImportApi.md#import_shots_csv) | **POST** /import/csv/projects/{project_id}/shots | Import shots csv
[**import_task_type_estimations_csv**](ImportApi.md#import_task_type_estimations_csv) | **POST** /import/csv/projects/{project_id}/task-types/{task_type_id}/estimations | Import task type estimations csv
[**remove_shotgun_asset**](ImportApi.md#remove_shotgun_asset) | **POST** /import/shotgun/remove/asset | Remove shotgun asset
[**remove_shotgun_episode**](ImportApi.md#remove_shotgun_episode) | **POST** /import/shotgun/remove/episode | Remove shotgun episode
[**remove_shotgun_note**](ImportApi.md#remove_shotgun_note) | **POST** /import/shotgun/remove/note | Remove shotgun note
[**remove_shotgun_person**](ImportApi.md#remove_shotgun_person) | **POST** /import/shotgun/remove/person | Remove shotgun person
[**remove_shotgun_project**](ImportApi.md#remove_shotgun_project) | **POST** /import/shotgun/remove/project | Remove shotgun project
[**remove_shotgun_project_connection**](ImportApi.md#remove_shotgun_project_connection) | **POST** /import/shotgun/remove/projectconnection | Remove shotgun project connection
[**remove_shotgun_scene**](ImportApi.md#remove_shotgun_scene) | **POST** /import/shotgun/remove/scene | Remove shotgun scene
[**remove_shotgun_sequence**](ImportApi.md#remove_shotgun_sequence) | **POST** /import/shotgun/remove/sequence | Remove shotgun sequence
[**remove_shotgun_shot**](ImportApi.md#remove_shotgun_shot) | **POST** /import/shotgun/remove/shot | Remove shotgun shot
[**remove_shotgun_step**](ImportApi.md#remove_shotgun_step) | **POST** /import/shotgun/remove/step | Remove shotgun step
[**remove_shotgun_task**](ImportApi.md#remove_shotgun_task) | **POST** /import/shotgun/remove/task | Remove shotgun task
[**remove_shotgun_task_status**](ImportApi.md#remove_shotgun_task_status) | **POST** /import/shotgun/remove/status | Remove shotgun task status
[**remove_shotgun_version**](ImportApi.md#remove_shotgun_version) | **POST** /import/shotgun/remove/version | Remove shotgun version


# **create_shotgun_import_error**
> CreateShotgunImportError201Response create_shotgun_import_error(create_shotgun_import_error_request)

Create shotgun import error

Create a new Shotgun import error record. The error event data should be provided in the JSON body.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_shotgun_import_error201_response import CreateShotgunImportError201Response
from sometech.pykitsu._client.models.create_shotgun_import_error_request import CreateShotgunImportErrorRequest
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    create_shotgun_import_error_request = sometech.pykitsu._client.CreateShotgunImportErrorRequest() # CreateShotgunImportErrorRequest | 

    try:
        # Create shotgun import error
        api_response = await api_instance.create_shotgun_import_error(create_shotgun_import_error_request)
        print("The response of ImportApi->create_shotgun_import_error:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->create_shotgun_import_error: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_shotgun_import_error_request** | [**CreateShotgunImportErrorRequest**](CreateShotgunImportErrorRequest.md)|  | 

### Return type

[**CreateShotgunImportError201Response**](CreateShotgunImportError201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Import error created successfully |  -  |
**400** | Invalid request body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shotgun_import_error**
> DeleteShotgunImportError204Response delete_shotgun_import_error(error_id)

Delete shotgun import error

Delete a Shotgun import error by its unique identifier. Returns success confirmation when the error is deleted.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.delete_shotgun_import_error204_response import DeleteShotgunImportError204Response
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    error_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Import error unique identifier

    try:
        # Delete shotgun import error
        api_response = await api_instance.delete_shotgun_import_error(error_id)
        print("The response of ImportApi->delete_shotgun_import_error:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->delete_shotgun_import_error: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_id** | **UUID**| Import error unique identifier | 

### Return type

[**DeleteShotgunImportError204Response**](DeleteShotgunImportError204Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Import error deleted successfully |  -  |
**400** | Invalid error ID format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shotgun_import_errors**
> List[GetShotgunImportErrors200ResponseInner] get_shotgun_import_errors()

Get shotgun import errors

Get all Shotgun import errors from the database. Returns a list of data import errors with source "shotgun".

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shotgun_import_errors200_response_inner import GetShotgunImportErrors200ResponseInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)

    try:
        # Get shotgun import errors
        api_response = await api_instance.get_shotgun_import_errors()
        print("The response of ImportApi->get_shotgun_import_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->get_shotgun_import_errors: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetShotgunImportErrors200ResponseInner]**](GetShotgunImportErrors200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of import errors retrieved successfully |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_assets_csv**
> List[Asset] import_assets_csv(project_id, file, update=update)

Import assets csv

Import project assets from a CSV file. Creates or updates assets based on CSV rows. Supports metadata descriptors and task status updates.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.asset import Asset
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    file = None # bytes | CSV file with asset data
    update = False # bool | Whether to update existing assets (optional) (default to False)

    try:
        # Import assets csv
        api_response = await api_instance.import_assets_csv(project_id, file, update=update)
        print("The response of ImportApi->import_assets_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_assets_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **file** | **bytes**| CSV file with asset data | 
 **update** | **bool**| Whether to update existing assets | [optional] [default to False]

### Return type

[**List[Asset]**](Asset.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Assets imported successfully |  -  |
**400** | Invalid CSV format or missing required columns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_casting_csv**
> List[ImportCastingCsv201ResponseInner] import_casting_csv(project_id, file, update=update)

Import casting csv

Import project casting links from a CSV file. Links assets to shots, sequences, or episodes based on CSV rows.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_casting_csv201_response_inner import ImportCastingCsv201ResponseInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    file = None # bytes | CSV file with casting link data
    update = False # bool | Whether to update existing casting links (optional) (default to False)

    try:
        # Import casting csv
        api_response = await api_instance.import_casting_csv(project_id, file, update=update)
        print("The response of ImportApi->import_casting_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_casting_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **file** | **bytes**| CSV file with casting link data | 
 **update** | **bool**| Whether to update existing casting links | [optional] [default to False]

### Return type

[**List[ImportCastingCsv201ResponseInner]**](ImportCastingCsv201ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Casting links imported successfully |  -  |
**400** | Invalid CSV format or missing required columns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_edits_csv**
> List[ImportEditsCsv201ResponseInner] import_edits_csv(project_id, file, update=update)

Import edits csv

Import project edits from a CSV file. Creates or updates edits based on CSV rows. Supports metadata descriptors and task status updates.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_edits_csv201_response_inner import ImportEditsCsv201ResponseInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    file = None # bytes | CSV file with edit data
    update = False # bool | Whether to update existing edits (optional) (default to False)

    try:
        # Import edits csv
        api_response = await api_instance.import_edits_csv(project_id, file, update=update)
        print("The response of ImportApi->import_edits_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_edits_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **file** | **bytes**| CSV file with edit data | 
 **update** | **bool**| Whether to update existing edits | [optional] [default to False]

### Return type

[**List[ImportEditsCsv201ResponseInner]**](ImportEditsCsv201ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Edits imported successfully |  -  |
**400** | Invalid CSV format or missing required columns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_episode_otio**
> ImportEpisodeOtio201Response import_episode_otio(project_id, episode_id, file, naming_convention=naming_convention, match_case=match_case)

Import episode otio

Import an OTIO file to set frame_in, frame_out, and nb_frames for shots in an episode. Supports any OpenTimelineIO adapter format like EDL or OTIO. Uses naming convention with episode name to match shots.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_episode_otio201_response import ImportEpisodeOtio201Response
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    episode_id = UUID('b24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    file = None # bytes | OTIO file to import (EDL, OTIO, etc.)
    naming_convention = '${project_name}_${episode_name}-${sequence_name}-${shot_name}' # str | Template for matching shot names from the file (optional) (default to '${project_name}_${episode_name}-${sequence_name}-${shot_name}')
    match_case = True # bool | Whether to match shot names case-sensitively (optional) (default to True)

    try:
        # Import episode otio
        api_response = await api_instance.import_episode_otio(project_id, episode_id, file, naming_convention=naming_convention, match_case=match_case)
        print("The response of ImportApi->import_episode_otio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_episode_otio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **episode_id** | **UUID**|  | 
 **file** | **bytes**| OTIO file to import (EDL, OTIO, etc.) | 
 **naming_convention** | **str**| Template for matching shot names from the file | [optional] [default to &#39;${project_name}_${episode_name}-${sequence_name}-${shot_name}&#39;]
 **match_case** | **bool**| Whether to match shot names case-sensitively | [optional] [default to True]

### Return type

[**ImportEpisodeOtio201Response**](ImportEpisodeOtio201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Shots imported successfully |  -  |
**400** | Invalid file format or parsing error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_episode_task_type_estimations_csv**
> List[Task] import_episode_task_type_estimations_csv(project_id, task_type_id, episode_id, file)

Import episode task type estimations csv

Import task type estimations from a CSV file for a specific episode. Updates estimations, dates, and other task properties for assets or shots based on CSV rows.

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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    task_type_id = UUID('b24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    episode_id = UUID('c24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    file = None # bytes | CSV file with task estimation data

    try:
        # Import episode task type estimations csv
        api_response = await api_instance.import_episode_task_type_estimations_csv(project_id, task_type_id, episode_id, file)
        print("The response of ImportApi->import_episode_task_type_estimations_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_episode_task_type_estimations_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **task_type_id** | **UUID**|  | 
 **episode_id** | **UUID**|  | 
 **file** | **bytes**| CSV file with task estimation data | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Task estimations imported successfully |  -  |
**400** | Invalid CSV format or entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_kitsu_comments**
> List[ImportKitsuComments200ResponseInner] import_kitsu_comments(import_kitsu_comments_request_inner)

Import kitsu comments

Import Kitsu comments. Send a list of Kitsu comment entries in the JSON body. Returns created or updated comments linked to tasks.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_kitsu_comments200_response_inner import ImportKitsuComments200ResponseInner
from sometech.pykitsu._client.models.import_kitsu_comments_request_inner import ImportKitsuCommentsRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_kitsu_comments_request_inner = [{"id":"a24a6ea4-ce75-4665-a070-57453082c25","object_id":"b24a6ea4-ce75-4665-a070-57453082c25","text":"This is a comment","person_id":"c24a6ea4-ce75-4665-a070-57453082c25"}] # List[ImportKitsuCommentsRequestInner] | 

    try:
        # Import kitsu comments
        api_response = await api_instance.import_kitsu_comments(import_kitsu_comments_request_inner)
        print("The response of ImportApi->import_kitsu_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_kitsu_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_kitsu_comments_request_inner** | [**List[ImportKitsuCommentsRequestInner]**](ImportKitsuCommentsRequestInner.md)|  | 

### Return type

[**List[ImportKitsuComments200ResponseInner]**](ImportKitsuComments200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comments imported successfully |  -  |
**400** | Invalid request body or missing required fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_kitsu_entities**
> List[ImportKitsuEntities200ResponseInner] import_kitsu_entities(import_kitsu_entities_request_inner)

Import kitsu entities

Import Kitsu entities (assets, shots, sequences, etc.). Send a list of Kitsu entity entries in the JSON body. Returns created or updated entities.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_kitsu_entities200_response_inner import ImportKitsuEntities200ResponseInner
from sometech.pykitsu._client.models.import_kitsu_entities_request_inner import ImportKitsuEntitiesRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_kitsu_entities_request_inner = [{"id":"a24a6ea4-ce75-4665-a070-57453082c25","name":"Asset01","project_id":"b24a6ea4-ce75-4665-a070-57453082c25","entity_type_id":"c24a6ea4-ce75-4665-a070-57453082c25"}] # List[ImportKitsuEntitiesRequestInner] | 

    try:
        # Import kitsu entities
        api_response = await api_instance.import_kitsu_entities(import_kitsu_entities_request_inner)
        print("The response of ImportApi->import_kitsu_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_kitsu_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_kitsu_entities_request_inner** | [**List[ImportKitsuEntitiesRequestInner]**](ImportKitsuEntitiesRequestInner.md)|  | 

### Return type

[**List[ImportKitsuEntities200ResponseInner]**](ImportKitsuEntities200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entities imported successfully |  -  |
**400** | Invalid request body or missing required fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_kitsu_entity_links**
> List[ImportKitsuEntityLinks200ResponseInner] import_kitsu_entity_links(import_kitsu_entity_links_request_inner)

Import kitsu entity links

Import Kitsu entity links (casting links). Send a list of Kitsu entity link entries in the JSON body. Returns created or updated entity links.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_kitsu_entity_links200_response_inner import ImportKitsuEntityLinks200ResponseInner
from sometech.pykitsu._client.models.import_kitsu_entity_links_request_inner import ImportKitsuEntityLinksRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_kitsu_entity_links_request_inner = [{"id":"a24a6ea4-ce75-4665-a070-57453082c25","entity_in_id":"b24a6ea4-ce75-4665-a070-57453082c25","entity_out_id":"c24a6ea4-ce75-4665-a070-57453082c25"}] # List[ImportKitsuEntityLinksRequestInner] | 

    try:
        # Import kitsu entity links
        api_response = await api_instance.import_kitsu_entity_links(import_kitsu_entity_links_request_inner)
        print("The response of ImportApi->import_kitsu_entity_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_kitsu_entity_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_kitsu_entity_links_request_inner** | [**List[ImportKitsuEntityLinksRequestInner]**](ImportKitsuEntityLinksRequestInner.md)|  | 

### Return type

[**List[ImportKitsuEntityLinks200ResponseInner]**](ImportKitsuEntityLinks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity links imported successfully |  -  |
**400** | Invalid request body or missing required fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_kitsu_projects**
> List[ImportKitsuProjects200ResponseInner] import_kitsu_projects(import_kitsu_projects_request_inner)

Import kitsu projects

Import Kitsu projects. Send a list of Kitsu project entries in the JSON body. Returns created or updated projects.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_kitsu_projects200_response_inner import ImportKitsuProjects200ResponseInner
from sometech.pykitsu._client.models.import_kitsu_projects_request_inner import ImportKitsuProjectsRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_kitsu_projects_request_inner = [{"id":"a24a6ea4-ce75-4665-a070-57453082c25","name":"My Project","production_type":"tvshow"}] # List[ImportKitsuProjectsRequestInner] | 

    try:
        # Import kitsu projects
        api_response = await api_instance.import_kitsu_projects(import_kitsu_projects_request_inner)
        print("The response of ImportApi->import_kitsu_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_kitsu_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_kitsu_projects_request_inner** | [**List[ImportKitsuProjectsRequestInner]**](ImportKitsuProjectsRequestInner.md)|  | 

### Return type

[**List[ImportKitsuProjects200ResponseInner]**](ImportKitsuProjects200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Projects imported successfully |  -  |
**400** | Invalid request body or missing required fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_kitsu_tasks**
> List[ImportKitsuTasks200ResponseInner] import_kitsu_tasks(import_kitsu_tasks_request_inner)

Import kitsu tasks

Import Kitsu tasks. Send a list of Kitsu task entries in the JSON body. Returns created or updated tasks.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_kitsu_tasks200_response_inner import ImportKitsuTasks200ResponseInner
from sometech.pykitsu._client.models.import_kitsu_tasks_request_inner import ImportKitsuTasksRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_kitsu_tasks_request_inner = [{"id":"a24a6ea4-ce75-4665-a070-57453082c25","name":"Modeling","project_id":"b24a6ea4-ce75-4665-a070-57453082c25","entity_id":"c24a6ea4-ce75-4665-a070-57453082c25","task_type_id":"d24a6ea4-ce75-4665-a070-57453082c25"}] # List[ImportKitsuTasksRequestInner] | 

    try:
        # Import kitsu tasks
        api_response = await api_instance.import_kitsu_tasks(import_kitsu_tasks_request_inner)
        print("The response of ImportApi->import_kitsu_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_kitsu_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_kitsu_tasks_request_inner** | [**List[ImportKitsuTasksRequestInner]**](ImportKitsuTasksRequestInner.md)|  | 

### Return type

[**List[ImportKitsuTasks200ResponseInner]**](ImportKitsuTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tasks imported successfully |  -  |
**400** | Invalid request body or missing required fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_otio_edl**
> ImportOtioEdl201Response import_otio_edl(project_id, file, naming_convention=naming_convention, match_case=match_case)

Import otio EDL

Import an OTIO file to set frame_in, frame_out, and nb_frames for shots. Supports any OpenTimelineIO adapter format like EDL or OTIO. Uses naming convention to match shots.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_otio_edl201_response import ImportOtioEdl201Response
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    file = None # bytes | OTIO file to import (EDL, OTIO, etc.)
    naming_convention = '${project_name}_${sequence_name}-${shot_name}' # str | Template for matching shot names from the file (optional) (default to '${project_name}_${sequence_name}-${shot_name}')
    match_case = True # bool | Whether to match shot names case-sensitively (optional) (default to True)

    try:
        # Import otio EDL
        api_response = await api_instance.import_otio_edl(project_id, file, naming_convention=naming_convention, match_case=match_case)
        print("The response of ImportApi->import_otio_edl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_otio_edl: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **file** | **bytes**| OTIO file to import (EDL, OTIO, etc.) | 
 **naming_convention** | **str**| Template for matching shot names from the file | [optional] [default to &#39;${project_name}_${sequence_name}-${shot_name}&#39;]
 **match_case** | **bool**| Whether to match shot names case-sensitively | [optional] [default to True]

### Return type

[**ImportOtioEdl201Response**](ImportOtioEdl201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Shots imported successfully |  -  |
**400** | Invalid file format or parsing error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_persons_csv**
> List[Person] import_persons_csv(file, update=update)

Import persons csv

Import persons from a CSV file. Creates or updates persons based on CSV rows. Supports role, contract type, and active status updates.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.person import Person
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    file = None # bytes | CSV file with person data
    update = False # bool | Whether to update existing persons (optional) (default to False)

    try:
        # Import persons csv
        api_response = await api_instance.import_persons_csv(file, update=update)
        print("The response of ImportApi->import_persons_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_persons_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytes**| CSV file with person data | 
 **update** | **bool**| Whether to update existing persons | [optional] [default to False]

### Return type

[**List[Person]**](Person.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Persons imported successfully |  -  |
**400** | Invalid CSV format or missing required columns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shotgun_assets**
> List[ImportShotgunAssets200ResponseInner] import_shotgun_assets(import_shotgun_assets_request_inner)

Import shotgun assets

Import Shotgun assets. Send a list of Shotgun asset entries in the JSON body. Returns created or updated assets with parent-child relationships.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_shotgun_assets200_response_inner import ImportShotgunAssets200ResponseInner
from sometech.pykitsu._client.models.import_shotgun_assets_request_inner import ImportShotgunAssetsRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_shotgun_assets_request_inner = [{"id":12345,"code":"Asset01","description":"Main character asset","sg_asset_type":"Character","project":{"id":11111},"parents":[{"id":22222}]}] # List[ImportShotgunAssetsRequestInner] | 

    try:
        # Import shotgun assets
        api_response = await api_instance.import_shotgun_assets(import_shotgun_assets_request_inner)
        print("The response of ImportApi->import_shotgun_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_shotgun_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_shotgun_assets_request_inner** | [**List[ImportShotgunAssetsRequestInner]**](ImportShotgunAssetsRequestInner.md)|  | 

### Return type

[**List[ImportShotgunAssets200ResponseInner]**](ImportShotgunAssets200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assets imported successfully |  -  |
**400** | Invalid request body or data format error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shotgun_episodes**
> List[ImportShotgunEpisodes200ResponseInner] import_shotgun_episodes(import_shotgun_episodes_request_inner)

Import shotgun episodes

Import Shotgun episodes. Send a list of Shotgun episode entries in the JSON body. Returns created or updated episodes.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_shotgun_episodes200_response_inner import ImportShotgunEpisodes200ResponseInner
from sometech.pykitsu._client.models.import_shotgun_episodes_request_inner import ImportShotgunEpisodesRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_shotgun_episodes_request_inner = [{"id":12345,"code":"EP01","description":"First episode","project":{"name":"My Project"}}] # List[ImportShotgunEpisodesRequestInner] | 

    try:
        # Import shotgun episodes
        api_response = await api_instance.import_shotgun_episodes(import_shotgun_episodes_request_inner)
        print("The response of ImportApi->import_shotgun_episodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_shotgun_episodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_shotgun_episodes_request_inner** | [**List[ImportShotgunEpisodesRequestInner]**](ImportShotgunEpisodesRequestInner.md)|  | 

### Return type

[**List[ImportShotgunEpisodes200ResponseInner]**](ImportShotgunEpisodes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Episodes imported successfully |  -  |
**400** | Invalid request body or data format error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shotgun_notes**
> List[ImportShotgunNotes200ResponseInner] import_shotgun_notes(import_shotgun_notes_request_inner)

Import shotgun notes

Import Shotgun notes (comments) linked to tasks. Send a list of Shotgun note entries in the JSON body. Only notes linked to tasks are imported. Returns created or updated comments.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_shotgun_notes200_response_inner import ImportShotgunNotes200ResponseInner
from sometech.pykitsu._client.models.import_shotgun_notes_request_inner import ImportShotgunNotesRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_shotgun_notes_request_inner = [{"id":12345,"content":"This is a comment","tasks":[{"id":67890}],"user":{"id":11111},"created_at":"2024-01-15T10:30:00Z"}] # List[ImportShotgunNotesRequestInner] | 

    try:
        # Import shotgun notes
        api_response = await api_instance.import_shotgun_notes(import_shotgun_notes_request_inner)
        print("The response of ImportApi->import_shotgun_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_shotgun_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_shotgun_notes_request_inner** | [**List[ImportShotgunNotesRequestInner]**](ImportShotgunNotesRequestInner.md)|  | 

### Return type

[**List[ImportShotgunNotes200ResponseInner]**](ImportShotgunNotes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notes imported successfully |  -  |
**400** | Invalid request body or data format error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shotgun_persons**
> List[ImportShotgunPersons200ResponseInner] import_shotgun_persons(import_shotgun_persons_request_inner)

Import shotgun persons

Import Shotgun persons (users). Send a list of Shotgun person entries in the JSON body. Returns created or updated persons with department associations.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_shotgun_persons200_response_inner import ImportShotgunPersons200ResponseInner
from sometech.pykitsu._client.models.import_shotgun_persons_request_inner import ImportShotgunPersonsRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_shotgun_persons_request_inner = [{"id":12345,"firstname":"John","lastname":"Doe","email":"john.doe@example.com","login":"jdoe","sg_status_list":"act","permission_rule_set":{"name":"Manager"},"department":{"name":"Animation"}}] # List[ImportShotgunPersonsRequestInner] | 

    try:
        # Import shotgun persons
        api_response = await api_instance.import_shotgun_persons(import_shotgun_persons_request_inner)
        print("The response of ImportApi->import_shotgun_persons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_shotgun_persons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_shotgun_persons_request_inner** | [**List[ImportShotgunPersonsRequestInner]**](ImportShotgunPersonsRequestInner.md)|  | 

### Return type

[**List[ImportShotgunPersons200ResponseInner]**](ImportShotgunPersons200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Persons imported successfully |  -  |
**400** | Invalid request body or data format error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shotgun_project_connections**
> List[ImportShotgunProjectConnections200ResponseInner] import_shotgun_project_connections(import_shotgun_project_connections_request_inner)

Import shotgun project connections

Import Shotgun project-user connections. Send a list of Shotgun project connection entries in the JSON body. Returns projects with team members added.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_shotgun_project_connections200_response_inner import ImportShotgunProjectConnections200ResponseInner
from sometech.pykitsu._client.models.import_shotgun_project_connections_request_inner import ImportShotgunProjectConnectionsRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_shotgun_project_connections_request_inner = [{"id":12345,"project":{"id":11111},"user":{"id":22222}}] # List[ImportShotgunProjectConnectionsRequestInner] | 

    try:
        # Import shotgun project connections
        api_response = await api_instance.import_shotgun_project_connections(import_shotgun_project_connections_request_inner)
        print("The response of ImportApi->import_shotgun_project_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_shotgun_project_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_shotgun_project_connections_request_inner** | [**List[ImportShotgunProjectConnectionsRequestInner]**](ImportShotgunProjectConnectionsRequestInner.md)|  | 

### Return type

[**List[ImportShotgunProjectConnections200ResponseInner]**](ImportShotgunProjectConnections200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project connections imported successfully |  -  |
**400** | Invalid request body or data format error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shotgun_projects**
> List[ImportShotgunProjects200ResponseInner] import_shotgun_projects(import_shotgun_projects_request_inner)

Import shotgun projects

Import Shotgun projects. Send a list of Shotgun project entries in the JSON body. Returns created or updated projects with custom fields preserved.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_shotgun_projects200_response_inner import ImportShotgunProjects200ResponseInner
from sometech.pykitsu._client.models.import_shotgun_projects_request_inner import ImportShotgunProjectsRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_shotgun_projects_request_inner = [{"id":12345,"name":"My Project","sg_status":"Active"}] # List[ImportShotgunProjectsRequestInner] | 

    try:
        # Import shotgun projects
        api_response = await api_instance.import_shotgun_projects(import_shotgun_projects_request_inner)
        print("The response of ImportApi->import_shotgun_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_shotgun_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_shotgun_projects_request_inner** | [**List[ImportShotgunProjectsRequestInner]**](ImportShotgunProjectsRequestInner.md)|  | 

### Return type

[**List[ImportShotgunProjects200ResponseInner]**](ImportShotgunProjects200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Projects imported successfully |  -  |
**400** | Invalid request body or data format error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shotgun_scenes**
> List[ImportShotgunScenes200ResponseInner] import_shotgun_scenes(import_shotgun_scenes_request_inner)

Import shotgun scenes

Import Shotgun scenes. Send a list of Shotgun scene entries in the JSON body. Returns created or updated scenes linked to sequences.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_shotgun_scenes200_response_inner import ImportShotgunScenes200ResponseInner
from sometech.pykitsu._client.models.import_shotgun_scenes_request_inner import ImportShotgunScenesRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_shotgun_scenes_request_inner = [{"id":12345,"code":"SC01","project":{"name":"My Project"}}] # List[ImportShotgunScenesRequestInner] | 

    try:
        # Import shotgun scenes
        api_response = await api_instance.import_shotgun_scenes(import_shotgun_scenes_request_inner)
        print("The response of ImportApi->import_shotgun_scenes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_shotgun_scenes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_shotgun_scenes_request_inner** | [**List[ImportShotgunScenesRequestInner]**](ImportShotgunScenesRequestInner.md)|  | 

### Return type

[**List[ImportShotgunScenes200ResponseInner]**](ImportShotgunScenes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scenes imported successfully |  -  |
**400** | Invalid request body or data format error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shotgun_sequences**
> List[ImportShotgunSequences200ResponseInner] import_shotgun_sequences(import_shotgun_sequences_request_inner)

Import shotgun sequences

Import Shotgun sequences. Send a list of Shotgun sequence entries in the JSON body. Returns created or updated sequences linked to episodes.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_shotgun_sequences200_response_inner import ImportShotgunSequences200ResponseInner
from sometech.pykitsu._client.models.import_shotgun_sequences_request_inner import ImportShotgunSequencesRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_shotgun_sequences_request_inner = [{"id":12345,"code":"SQ01","description":"Main sequence","project":{"name":"My Project"},"episode":{"id":11111}}] # List[ImportShotgunSequencesRequestInner] | 

    try:
        # Import shotgun sequences
        api_response = await api_instance.import_shotgun_sequences(import_shotgun_sequences_request_inner)
        print("The response of ImportApi->import_shotgun_sequences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_shotgun_sequences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_shotgun_sequences_request_inner** | [**List[ImportShotgunSequencesRequestInner]**](ImportShotgunSequencesRequestInner.md)|  | 

### Return type

[**List[ImportShotgunSequences200ResponseInner]**](ImportShotgunSequences200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sequences imported successfully |  -  |
**400** | Invalid request body or data format error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shotgun_shots**
> List[ImportShotgunShots200ResponseInner] import_shotgun_shots(import_shotgun_shots_request_inner)

Import shotgun shots

Import Shotgun shots. Send a list of Shotgun shot entries in the JSON body. Returns created or updated shots with frame ranges, custom fields, and asset links.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_shotgun_shots200_response_inner import ImportShotgunShots200ResponseInner
from sometech.pykitsu._client.models.import_shotgun_shots_request_inner import ImportShotgunShotsRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_shotgun_shots_request_inner = [{"id":12345,"code":"SH010","sg_cut_in":1001,"sg_cut_duration":50,"project":{"name":"My Project"},"sg_sequence":{"id":11111},"sg_scene":{"id":22222},"assets":[{"id":33333}]}] # List[ImportShotgunShotsRequestInner] | 

    try:
        # Import shotgun shots
        api_response = await api_instance.import_shotgun_shots(import_shotgun_shots_request_inner)
        print("The response of ImportApi->import_shotgun_shots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_shotgun_shots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_shotgun_shots_request_inner** | [**List[ImportShotgunShotsRequestInner]**](ImportShotgunShotsRequestInner.md)|  | 

### Return type

[**List[ImportShotgunShots200ResponseInner]**](ImportShotgunShots200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shots imported successfully |  -  |
**400** | Invalid request body or data format error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shotgun_steps**
> List[ImportShotgunSteps200ResponseInner] import_shotgun_steps(import_shotgun_steps_request_inner)

Import shotgun steps

Import Shotgun steps (task types). Send a list of Shotgun step entries in the JSON body. Returns created or updated task types with departments.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_shotgun_steps200_response_inner import ImportShotgunSteps200ResponseInner
from sometech.pykitsu._client.models.import_shotgun_steps_request_inner import ImportShotgunStepsRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_shotgun_steps_request_inner = [{"id":12345,"code":"Animation Modeling","short_name":"mod","color":"255,128,0","entity_type":"Asset"}] # List[ImportShotgunStepsRequestInner] | 

    try:
        # Import shotgun steps
        api_response = await api_instance.import_shotgun_steps(import_shotgun_steps_request_inner)
        print("The response of ImportApi->import_shotgun_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_shotgun_steps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_shotgun_steps_request_inner** | [**List[ImportShotgunStepsRequestInner]**](ImportShotgunStepsRequestInner.md)|  | 

### Return type

[**List[ImportShotgunSteps200ResponseInner]**](ImportShotgunSteps200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task types imported successfully |  -  |
**400** | Invalid request body or data format error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shotgun_task_statuses**
> List[ImportShotgunTaskStatuses200ResponseInner] import_shotgun_task_statuses(import_shotgun_task_statuses_request_inner)

Import shotgun task statuses

Import Shotgun task statuses. Send a list of Shotgun status entries in the JSON body. Returns created or updated task statuses with colors.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_shotgun_task_statuses200_response_inner import ImportShotgunTaskStatuses200ResponseInner
from sometech.pykitsu._client.models.import_shotgun_task_statuses_request_inner import ImportShotgunTaskStatusesRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_shotgun_task_statuses_request_inner = [{"id":12345,"name":"In Progress","code":"IP","bg_color":"255,128,0"}] # List[ImportShotgunTaskStatusesRequestInner] | 

    try:
        # Import shotgun task statuses
        api_response = await api_instance.import_shotgun_task_statuses(import_shotgun_task_statuses_request_inner)
        print("The response of ImportApi->import_shotgun_task_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_shotgun_task_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_shotgun_task_statuses_request_inner** | [**List[ImportShotgunTaskStatusesRequestInner]**](ImportShotgunTaskStatusesRequestInner.md)|  | 

### Return type

[**List[ImportShotgunTaskStatuses200ResponseInner]**](ImportShotgunTaskStatuses200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task statuses imported successfully |  -  |
**400** | Invalid request body or data format error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shotgun_tasks**
> List[ImportShotgunTasks200ResponseInner] import_shotgun_tasks(import_shotgun_tasks_request_inner)

Import shotgun tasks

Import Shotgun tasks. Send a list of Shotgun task entries in the JSON body. Only tasks with steps and projects are imported. Returns created or updated tasks with assignees.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_shotgun_tasks200_response_inner import ImportShotgunTasks200ResponseInner
from sometech.pykitsu._client.models.import_shotgun_tasks_request_inner import ImportShotgunTasksRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_shotgun_tasks_request_inner = [{"id":12345,"cached_display_name":"Modeling for Asset","start_date":"2024-01-15","due_date":"2024-02-15","sg_sort_order":1,"duration":30,"step":{"id":11111},"project":{"id":22222},"entity":{"id":33333,"type":"Asset"},"sg_status_list":"IP","created_by":{"id":44444},"task_assignees":[{"id":55555}]}] # List[ImportShotgunTasksRequestInner] | 

    try:
        # Import shotgun tasks
        api_response = await api_instance.import_shotgun_tasks(import_shotgun_tasks_request_inner)
        print("The response of ImportApi->import_shotgun_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_shotgun_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_shotgun_tasks_request_inner** | [**List[ImportShotgunTasksRequestInner]**](ImportShotgunTasksRequestInner.md)|  | 

### Return type

[**List[ImportShotgunTasks200ResponseInner]**](ImportShotgunTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tasks imported successfully |  -  |
**400** | Invalid request body or data format error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shotgun_versions**
> List[ImportShotgunVersions200ResponseInner] import_shotgun_versions(import_shotgun_versions_request_inner)

Import shotgun versions

Import Shotgun versions (preview files). Send a list of Shotgun version entries in the JSON body. Only versions linked to tasks are imported. Returns created or updated preview files.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.import_shotgun_versions200_response_inner import ImportShotgunVersions200ResponseInner
from sometech.pykitsu._client.models.import_shotgun_versions_request_inner import ImportShotgunVersionsRequestInner
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    import_shotgun_versions_request_inner = [{"id":12345,"code":"v001","description":"First version","sg_task":{"id":11111},"user":{"id":22222},"sg_uploaded_movie":{"url":"https://example.com/movie.mp4","name":"movie.mp4"}}] # List[ImportShotgunVersionsRequestInner] | 

    try:
        # Import shotgun versions
        api_response = await api_instance.import_shotgun_versions(import_shotgun_versions_request_inner)
        print("The response of ImportApi->import_shotgun_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_shotgun_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_shotgun_versions_request_inner** | [**List[ImportShotgunVersionsRequestInner]**](ImportShotgunVersionsRequestInner.md)|  | 

### Return type

[**List[ImportShotgunVersions200ResponseInner]**](ImportShotgunVersions200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Versions imported successfully |  -  |
**400** | Invalid request body or data format error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_shots_csv**
> List[Shot] import_shots_csv(project_id, file, update=update)

Import shots csv

Import project shots from a CSV file. Creates or updates shots based on CSV rows. Supports sequences, episodes, and task status updates.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.shot import Shot
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    file = None # bytes | CSV file with shot data
    update = False # bool | Whether to update existing shots (optional) (default to False)

    try:
        # Import shots csv
        api_response = await api_instance.import_shots_csv(project_id, file, update=update)
        print("The response of ImportApi->import_shots_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_shots_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **file** | **bytes**| CSV file with shot data | 
 **update** | **bool**| Whether to update existing shots | [optional] [default to False]

### Return type

[**List[Shot]**](Shot.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Shots imported successfully |  -  |
**400** | Invalid CSV format or missing required columns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_task_type_estimations_csv**
> List[Task] import_task_type_estimations_csv(project_id, task_type_id, file)

Import task type estimations csv

Import task type estimations from a CSV file. Updates estimations, dates, and other task properties for assets or shots based on CSV rows.

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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    task_type_id = UUID('b24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    file = None # bytes | CSV file with task estimation data

    try:
        # Import task type estimations csv
        api_response = await api_instance.import_task_type_estimations_csv(project_id, task_type_id, file)
        print("The response of ImportApi->import_task_type_estimations_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->import_task_type_estimations_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **task_type_id** | **UUID**|  | 
 **file** | **bytes**| CSV file with task estimation data | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Task estimations imported successfully |  -  |
**400** | Invalid CSV format or entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shotgun_asset**
> RemoveShotgunAsset200Response remove_shotgun_asset(remove_shotgun_asset_request)

Remove shotgun asset

Remove a Shotgun asset from the database. Provide the Shotgun entry ID in the JSON body. If the asset has working files linked to tasks, it will be cancelled instead of deleted.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.remove_shotgun_asset200_response import RemoveShotgunAsset200Response
from sometech.pykitsu._client.models.remove_shotgun_asset_request import RemoveShotgunAssetRequest
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    remove_shotgun_asset_request = {"id":12345} # RemoveShotgunAssetRequest | 

    try:
        # Remove shotgun asset
        api_response = await api_instance.remove_shotgun_asset(remove_shotgun_asset_request)
        print("The response of ImportApi->remove_shotgun_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->remove_shotgun_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_shotgun_asset_request** | [**RemoveShotgunAssetRequest**](RemoveShotgunAssetRequest.md)|  | 

### Return type

[**RemoveShotgunAsset200Response**](RemoveShotgunAsset200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removal result returned |  -  |
**400** | Invalid request body or instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shotgun_episode**
> RemoveShotgunEpisode200Response remove_shotgun_episode(remove_shotgun_episode_request)

Remove shotgun episode

Remove a Shotgun episode from the database. Provide the Shotgun entry ID in the JSON body.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.remove_shotgun_episode200_response import RemoveShotgunEpisode200Response
from sometech.pykitsu._client.models.remove_shotgun_episode_request import RemoveShotgunEpisodeRequest
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    remove_shotgun_episode_request = {"id":12345} # RemoveShotgunEpisodeRequest | 

    try:
        # Remove shotgun episode
        api_response = await api_instance.remove_shotgun_episode(remove_shotgun_episode_request)
        print("The response of ImportApi->remove_shotgun_episode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->remove_shotgun_episode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_shotgun_episode_request** | [**RemoveShotgunEpisodeRequest**](RemoveShotgunEpisodeRequest.md)|  | 

### Return type

[**RemoveShotgunEpisode200Response**](RemoveShotgunEpisode200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removal result returned |  -  |
**400** | Invalid request body or instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shotgun_note**
> RemoveShotgunNote200Response remove_shotgun_note(remove_shotgun_note_request)

Remove shotgun note

Remove a Shotgun note (comment) from the database. Provide the Shotgun entry ID in the JSON body.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.remove_shotgun_note200_response import RemoveShotgunNote200Response
from sometech.pykitsu._client.models.remove_shotgun_note_request import RemoveShotgunNoteRequest
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    remove_shotgun_note_request = {"id":12345} # RemoveShotgunNoteRequest | 

    try:
        # Remove shotgun note
        api_response = await api_instance.remove_shotgun_note(remove_shotgun_note_request)
        print("The response of ImportApi->remove_shotgun_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->remove_shotgun_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_shotgun_note_request** | [**RemoveShotgunNoteRequest**](RemoveShotgunNoteRequest.md)|  | 

### Return type

[**RemoveShotgunNote200Response**](RemoveShotgunNote200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removal result returned |  -  |
**400** | Invalid request body or instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shotgun_person**
> RemoveShotgunPerson200Response remove_shotgun_person(remove_shotgun_person_request)

Remove shotgun person

Remove a Shotgun person (user) from the database. Provide the Shotgun entry ID in the JSON body.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.remove_shotgun_person200_response import RemoveShotgunPerson200Response
from sometech.pykitsu._client.models.remove_shotgun_person_request import RemoveShotgunPersonRequest
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    remove_shotgun_person_request = {"id":12345} # RemoveShotgunPersonRequest | 

    try:
        # Remove shotgun person
        api_response = await api_instance.remove_shotgun_person(remove_shotgun_person_request)
        print("The response of ImportApi->remove_shotgun_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->remove_shotgun_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_shotgun_person_request** | [**RemoveShotgunPersonRequest**](RemoveShotgunPersonRequest.md)|  | 

### Return type

[**RemoveShotgunPerson200Response**](RemoveShotgunPerson200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removal result returned |  -  |
**400** | Invalid request body or instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shotgun_project**
> RemoveShotgunProject200Response remove_shotgun_project(remove_shotgun_project_request)

Remove shotgun project

Remove a Shotgun project from the database. Provide the Shotgun entry ID in the JSON body.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.remove_shotgun_project200_response import RemoveShotgunProject200Response
from sometech.pykitsu._client.models.remove_shotgun_project_request import RemoveShotgunProjectRequest
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    remove_shotgun_project_request = {"id":12345} # RemoveShotgunProjectRequest | 

    try:
        # Remove shotgun project
        api_response = await api_instance.remove_shotgun_project(remove_shotgun_project_request)
        print("The response of ImportApi->remove_shotgun_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->remove_shotgun_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_shotgun_project_request** | [**RemoveShotgunProjectRequest**](RemoveShotgunProjectRequest.md)|  | 

### Return type

[**RemoveShotgunProject200Response**](RemoveShotgunProject200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removal result returned |  -  |
**400** | Invalid request body or instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shotgun_project_connection**
> RemoveShotgunProjectConnection200Response remove_shotgun_project_connection(remove_shotgun_project_connection_request)

Remove shotgun project connection

Remove a Shotgun project-user connection from the database. Provide the Shotgun entry ID in the JSON body.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.remove_shotgun_project_connection200_response import RemoveShotgunProjectConnection200Response
from sometech.pykitsu._client.models.remove_shotgun_project_connection_request import RemoveShotgunProjectConnectionRequest
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    remove_shotgun_project_connection_request = {"id":12345} # RemoveShotgunProjectConnectionRequest | 

    try:
        # Remove shotgun project connection
        api_response = await api_instance.remove_shotgun_project_connection(remove_shotgun_project_connection_request)
        print("The response of ImportApi->remove_shotgun_project_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->remove_shotgun_project_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_shotgun_project_connection_request** | [**RemoveShotgunProjectConnectionRequest**](RemoveShotgunProjectConnectionRequest.md)|  | 

### Return type

[**RemoveShotgunProjectConnection200Response**](RemoveShotgunProjectConnection200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removal result returned |  -  |
**400** | Invalid request body or instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shotgun_scene**
> RemoveShotgunScene200Response remove_shotgun_scene(remove_shotgun_scene_request)

Remove shotgun scene

Remove a Shotgun scene from the database. Provide the Shotgun entry ID in the JSON body.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.remove_shotgun_scene200_response import RemoveShotgunScene200Response
from sometech.pykitsu._client.models.remove_shotgun_scene_request import RemoveShotgunSceneRequest
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    remove_shotgun_scene_request = {"id":12345} # RemoveShotgunSceneRequest | 

    try:
        # Remove shotgun scene
        api_response = await api_instance.remove_shotgun_scene(remove_shotgun_scene_request)
        print("The response of ImportApi->remove_shotgun_scene:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->remove_shotgun_scene: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_shotgun_scene_request** | [**RemoveShotgunSceneRequest**](RemoveShotgunSceneRequest.md)|  | 

### Return type

[**RemoveShotgunScene200Response**](RemoveShotgunScene200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removal result returned |  -  |
**400** | Invalid request body or instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shotgun_sequence**
> RemoveShotgunSequence200Response remove_shotgun_sequence(remove_shotgun_sequence_request)

Remove shotgun sequence

Remove a Shotgun sequence from the database. Provide the Shotgun entry ID in the JSON body.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.remove_shotgun_sequence200_response import RemoveShotgunSequence200Response
from sometech.pykitsu._client.models.remove_shotgun_sequence_request import RemoveShotgunSequenceRequest
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    remove_shotgun_sequence_request = {"id":12345} # RemoveShotgunSequenceRequest | 

    try:
        # Remove shotgun sequence
        api_response = await api_instance.remove_shotgun_sequence(remove_shotgun_sequence_request)
        print("The response of ImportApi->remove_shotgun_sequence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->remove_shotgun_sequence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_shotgun_sequence_request** | [**RemoveShotgunSequenceRequest**](RemoveShotgunSequenceRequest.md)|  | 

### Return type

[**RemoveShotgunSequence200Response**](RemoveShotgunSequence200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removal result returned |  -  |
**400** | Invalid request body or instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shotgun_shot**
> RemoveShotgunShot200Response remove_shotgun_shot(remove_shotgun_shot_request)

Remove shotgun shot

Remove a Shotgun shot from the database. Provide the Shotgun entry ID in the JSON body.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.remove_shotgun_shot200_response import RemoveShotgunShot200Response
from sometech.pykitsu._client.models.remove_shotgun_shot_request import RemoveShotgunShotRequest
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    remove_shotgun_shot_request = {"id":12345} # RemoveShotgunShotRequest | 

    try:
        # Remove shotgun shot
        api_response = await api_instance.remove_shotgun_shot(remove_shotgun_shot_request)
        print("The response of ImportApi->remove_shotgun_shot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->remove_shotgun_shot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_shotgun_shot_request** | [**RemoveShotgunShotRequest**](RemoveShotgunShotRequest.md)|  | 

### Return type

[**RemoveShotgunShot200Response**](RemoveShotgunShot200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removal result returned |  -  |
**400** | Invalid request body or instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shotgun_step**
> RemoveShotgunStep200Response remove_shotgun_step(remove_shotgun_step_request)

Remove shotgun step

Remove a Shotgun step (task type) from the database. Provide the Shotgun entry ID in the JSON body.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.remove_shotgun_step200_response import RemoveShotgunStep200Response
from sometech.pykitsu._client.models.remove_shotgun_step_request import RemoveShotgunStepRequest
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    remove_shotgun_step_request = {"id":12345} # RemoveShotgunStepRequest | 

    try:
        # Remove shotgun step
        api_response = await api_instance.remove_shotgun_step(remove_shotgun_step_request)
        print("The response of ImportApi->remove_shotgun_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->remove_shotgun_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_shotgun_step_request** | [**RemoveShotgunStepRequest**](RemoveShotgunStepRequest.md)|  | 

### Return type

[**RemoveShotgunStep200Response**](RemoveShotgunStep200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removal result returned |  -  |
**400** | Invalid request body or instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shotgun_task**
> RemoveShotgunTask200Response remove_shotgun_task(remove_shotgun_task_request)

Remove shotgun task

Remove a Shotgun task from the database. Provide the Shotgun entry ID in the JSON body.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.remove_shotgun_task200_response import RemoveShotgunTask200Response
from sometech.pykitsu._client.models.remove_shotgun_task_request import RemoveShotgunTaskRequest
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    remove_shotgun_task_request = {"id":12345} # RemoveShotgunTaskRequest | 

    try:
        # Remove shotgun task
        api_response = await api_instance.remove_shotgun_task(remove_shotgun_task_request)
        print("The response of ImportApi->remove_shotgun_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->remove_shotgun_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_shotgun_task_request** | [**RemoveShotgunTaskRequest**](RemoveShotgunTaskRequest.md)|  | 

### Return type

[**RemoveShotgunTask200Response**](RemoveShotgunTask200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removal result returned |  -  |
**400** | Invalid request body or instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shotgun_task_status**
> RemoveShotgunTaskStatus200Response remove_shotgun_task_status(remove_shotgun_task_status_request)

Remove shotgun task status

Remove a Shotgun task status from the database. Provide the Shotgun entry ID in the JSON body.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.remove_shotgun_task_status200_response import RemoveShotgunTaskStatus200Response
from sometech.pykitsu._client.models.remove_shotgun_task_status_request import RemoveShotgunTaskStatusRequest
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    remove_shotgun_task_status_request = {"id":12345} # RemoveShotgunTaskStatusRequest | 

    try:
        # Remove shotgun task status
        api_response = await api_instance.remove_shotgun_task_status(remove_shotgun_task_status_request)
        print("The response of ImportApi->remove_shotgun_task_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->remove_shotgun_task_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_shotgun_task_status_request** | [**RemoveShotgunTaskStatusRequest**](RemoveShotgunTaskStatusRequest.md)|  | 

### Return type

[**RemoveShotgunTaskStatus200Response**](RemoveShotgunTaskStatus200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removal result returned |  -  |
**400** | Invalid request body or instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shotgun_version**
> RemoveShotgunVersion200Response remove_shotgun_version(remove_shotgun_version_request)

Remove shotgun version

Remove a Shotgun version (preview file) from the database. Provide the Shotgun entry ID in the JSON body.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.remove_shotgun_version200_response import RemoveShotgunVersion200Response
from sometech.pykitsu._client.models.remove_shotgun_version_request import RemoveShotgunVersionRequest
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
    api_instance = sometech.pykitsu._client.ImportApi(api_client)
    remove_shotgun_version_request = {"id":12345} # RemoveShotgunVersionRequest | 

    try:
        # Remove shotgun version
        api_response = await api_instance.remove_shotgun_version(remove_shotgun_version_request)
        print("The response of ImportApi->remove_shotgun_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportApi->remove_shotgun_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_shotgun_version_request** | [**RemoveShotgunVersionRequest**](RemoveShotgunVersionRequest.md)|  | 

### Return type

[**RemoveShotgunVersion200Response**](RemoveShotgunVersion200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removal result returned |  -  |
**400** | Invalid request body or instance not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

