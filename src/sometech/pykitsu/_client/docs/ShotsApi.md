# sometech.pykitsu._client.ShotsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_episode**](ShotsApi.md#create_project_episode) | **POST** /data/projects/{project_id}/episodes | Create project episode
[**create_project_scene**](ShotsApi.md#create_project_scene) | **POST** /data/projects/{project_id}/scenes | Create project scene
[**create_project_sequence**](ShotsApi.md#create_project_sequence) | **POST** /data/projects/{project_id}/sequences | Create project sequence
[**create_project_shot**](ShotsApi.md#create_project_shot) | **POST** /data/projects/{project_id}/shots | Create project shot
[**delete_episode**](ShotsApi.md#delete_episode) | **DELETE** /data/episodes/{episode_id} | Delete episode
[**delete_given_shot_from_given_scene**](ShotsApi.md#delete_given_shot_from_given_scene) | **DELETE** /data/scenes/{scene_id}/shots/{shot_id} | Delete given shot from given scene.
[**delete_scene**](ShotsApi.md#delete_scene) | **DELETE** /data/scenes/{scene_id} | Delete scene
[**delete_sequence**](ShotsApi.md#delete_sequence) | **DELETE** /data/sequences/{sequence_id} | Delete sequence
[**delete_shot**](ShotsApi.md#delete_shot) | **DELETE** /data/shots/{shot_id} | Delete shot
[**get_all_shots**](ShotsApi.md#get_all_shots) | **GET** /data/shots | Get all shots
[**get_episode**](ShotsApi.md#get_episode) | **GET** /data/episodes/{episode_id} | Get episode
[**get_episode_asset_tasks**](ShotsApi.md#get_episode_asset_tasks) | **GET** /data/episodes/{episode_id}/asset-tasks | Get episode asset tasks
[**get_episode_retake_stats**](ShotsApi.md#get_episode_retake_stats) | **GET** /data/projects/{project_id}/episodes/retake-stats | Get episode retake stats
[**get_episode_sequences**](ShotsApi.md#get_episode_sequences) | **GET** /data/episodes/{episode_id}/sequences | Get episode sequences
[**get_episode_shot_tasks**](ShotsApi.md#get_episode_shot_tasks) | **GET** /data/episodes/{episode_id}/shot-tasks | Get episode shot tasks
[**get_episode_shots**](ShotsApi.md#get_episode_shots) | **GET** /data/episodes/{episode_id}/shots | Get episode shots
[**get_episode_stats**](ShotsApi.md#get_episode_stats) | **GET** /data/projects/{project_id}/episodes/stats | Get episode stats
[**get_episode_task_types**](ShotsApi.md#get_episode_task_types) | **GET** /data/episodes/{episode_id}/task-types | Get episode task types
[**get_episode_tasks**](ShotsApi.md#get_episode_tasks) | **GET** /data/episodes/{episode_id}/tasks | Get episode tasks
[**get_episodes**](ShotsApi.md#get_episodes) | **GET** /data/episodes | Get episodes
[**get_episodes_and_tasks**](ShotsApi.md#get_episodes_and_tasks) | **GET** /data/episodes/with-tasks | Get episodes and tasks
[**get_project_episodes_get_data_projects_project_id_episodes**](ShotsApi.md#get_project_episodes_get_data_projects_project_id_episodes) | **GET** /data/projects/{project_id}/episodes | Get project episodes
[**get_project_person_quotas**](ShotsApi.md#get_project_person_quotas) | **GET** /data/projects/{project_id}/quotas/persons/{person_id} | Get project person quotas
[**get_project_quotas**](ShotsApi.md#get_project_quotas) | **GET** /data/projects/{project_id}/quotas/{task_type_id} | Get project quotas
[**get_project_scenes**](ShotsApi.md#get_project_scenes) | **GET** /data/projects/{project_id}/scenes | Get project scenes
[**get_project_sequences_get_data_projects_project_id_sequences**](ShotsApi.md#get_project_sequences_get_data_projects_project_id_sequences) | **GET** /data/projects/{project_id}/sequences | Get project sequences
[**get_project_shots**](ShotsApi.md#get_project_shots) | **GET** /data/projects/{project_id}/shots | Get project shots
[**get_scene**](ShotsApi.md#get_scene) | **GET** /data/scenes/{scene_id} | Get scene
[**get_scene_shots**](ShotsApi.md#get_scene_shots) | **GET** /data/scenes/{scene_id}/shots | Get scene shots
[**get_scene_task_types_get_data_scenes_scene_id_task_types**](ShotsApi.md#get_scene_task_types_get_data_scenes_scene_id_task_types) | **GET** /data/scenes/{scene_id}/task-types | Get scene task types
[**get_scene_tasks_get_data_scenes_scene_id_tasks**](ShotsApi.md#get_scene_tasks_get_data_scenes_scene_id_tasks) | **GET** /data/scenes/{scene_id}/tasks | Get scene tasks
[**get_scenes**](ShotsApi.md#get_scenes) | **GET** /data/scenes/all | Get scenes
[**get_scenes_and_tasks**](ShotsApi.md#get_scenes_and_tasks) | **GET** /data/scenes/with-tasks | Get scenes and tasks
[**get_sequence**](ShotsApi.md#get_sequence) | **GET** /data/sequences/{sequence_id} | Get sequence
[**get_sequence_scenes_get_data_sequences_sequence_id_scenes**](ShotsApi.md#get_sequence_scenes_get_data_sequences_sequence_id_scenes) | **GET** /data/sequences/{sequence_id}/scenes | Get sequence scenes
[**get_sequence_shot_tasks**](ShotsApi.md#get_sequence_shot_tasks) | **GET** /data/sequences/{sequence_id}/shot-tasks | Get sequence shot tasks
[**get_sequence_shots_get_data_sequences_sequence_id_shots**](ShotsApi.md#get_sequence_shots_get_data_sequences_sequence_id_shots) | **GET** /data/sequences/{sequence_id}/shots | Get sequence shots
[**get_sequence_task_types_get_data_sequences_sequence_id_task_types**](ShotsApi.md#get_sequence_task_types_get_data_sequences_sequence_id_task_types) | **GET** /data/sequences/{sequence_id}/task-types | Get sequence task types
[**get_sequence_tasks_get_data_sequences_sequence_id_tasks**](ShotsApi.md#get_sequence_tasks_get_data_sequences_sequence_id_tasks) | **GET** /data/sequences/{sequence_id}/tasks | Get sequence tasks
[**get_sequences**](ShotsApi.md#get_sequences) | **GET** /data/sequences | Get sequences
[**get_sequences_and_tasks**](ShotsApi.md#get_sequences_and_tasks) | **GET** /data/sequences/with-tasks | Get sequences and tasks
[**get_shot**](ShotsApi.md#get_shot) | **GET** /data/shots/{shot_id} | Get shot
[**get_shot_assets**](ShotsApi.md#get_shot_assets) | **GET** /data/shots/{shot_id}/assets | Get shot assets
[**get_shot_previews**](ShotsApi.md#get_shot_previews) | **GET** /data/shots/{shot_id}/preview-files | Get shot previews
[**get_shot_task_types_get_data_shots_shot_id_task_types**](ShotsApi.md#get_shot_task_types_get_data_shots_shot_id_task_types) | **GET** /data/shots/{shot_id}/task-types | Get shot task types
[**get_shot_tasks_get_data_shots_shot_id_tasks**](ShotsApi.md#get_shot_tasks_get_data_shots_shot_id_tasks) | **GET** /data/shots/{shot_id}/tasks | Get shot tasks
[**get_shot_versions**](ShotsApi.md#get_shot_versions) | **GET** /data/shots/{shot_id}/versions | Get shot versions
[**get_shots**](ShotsApi.md#get_shots) | **GET** /data/shots/all | Get shots
[**get_shots_and_tasks**](ShotsApi.md#get_shots_and_tasks) | **GET** /data/shots/with-tasks | Get shots and tasks
[**link_shot_to_scene**](ShotsApi.md#link_shot_to_scene) | **POST** /data/scenes/{scene_id}/shots | Link shot to scene
[**set_shots_frames**](ShotsApi.md#set_shots_frames) | **POST** /actions/projects/{project_id}/task-types/{task_type_id}/set-shot-nb-frames | Set shots frames
[**update_shot**](ShotsApi.md#update_shot) | **PUT** /data/shots/{shot_id} | Update shot


# **create_project_episode**
> Episode create_project_episode(project_id, create_project_episode_request)

Create project episode

Create an episode in a project. Provide name and description. Status is optional.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_project_episode_request import CreateProjectEpisodeRequest
from sometech.pykitsu._client.models.episode import Episode
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    create_project_episode_request = sometech.pykitsu._client.CreateProjectEpisodeRequest() # CreateProjectEpisodeRequest | 

    try:
        # Create project episode
        api_response = await api_instance.create_project_episode(project_id, create_project_episode_request)
        print("The response of ShotsApi->create_project_episode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->create_project_episode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **create_project_episode_request** | [**CreateProjectEpisodeRequest**](CreateProjectEpisodeRequest.md)|  | 

### Return type

[**Episode**](Episode.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Episode created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_scene**
> GetProjectScenes200ResponseInner create_project_scene(project_id, create_project_scene_request)

Create project scene

Create a new scene in a project. Provide a name and the related sequence id.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_project_scene_request import CreateProjectSceneRequest
from sometech.pykitsu._client.models.get_project_scenes200_response_inner import GetProjectScenes200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    create_project_scene_request = sometech.pykitsu._client.CreateProjectSceneRequest() # CreateProjectSceneRequest | 

    try:
        # Create project scene
        api_response = await api_instance.create_project_scene(project_id, create_project_scene_request)
        print("The response of ShotsApi->create_project_scene:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->create_project_scene: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **create_project_scene_request** | [**CreateProjectSceneRequest**](CreateProjectSceneRequest.md)|  | 

### Return type

[**GetProjectScenes200ResponseInner**](GetProjectScenes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Scene created for given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_sequence**
> Sequence create_project_sequence(project_id, create_project_sequence_request)

Create project sequence

Create a sequence in a project. Provide name and optional episode_id.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_project_sequence_request import CreateProjectSequenceRequest
from sometech.pykitsu._client.models.sequence import Sequence
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    create_project_sequence_request = sometech.pykitsu._client.CreateProjectSequenceRequest() # CreateProjectSequenceRequest | 

    try:
        # Create project sequence
        api_response = await api_instance.create_project_sequence(project_id, create_project_sequence_request)
        print("The response of ShotsApi->create_project_sequence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->create_project_sequence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **create_project_sequence_request** | [**CreateProjectSequenceRequest**](CreateProjectSequenceRequest.md)|  | 

### Return type

[**Sequence**](Sequence.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Sequence created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_shot**
> CreateProjectShot201Response create_project_shot(project_id, create_project_shot_request)

Create project shot

Create a shot in a project. Provide name and optional fields like description, sequence_id and nb_frames.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_project_shot201_response import CreateProjectShot201Response
from sometech.pykitsu._client.models.create_project_shot_request import CreateProjectShotRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    create_project_shot_request = sometech.pykitsu._client.CreateProjectShotRequest() # CreateProjectShotRequest | 

    try:
        # Create project shot
        api_response = await api_instance.create_project_shot(project_id, create_project_shot_request)
        print("The response of ShotsApi->create_project_shot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->create_project_shot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **create_project_shot_request** | [**CreateProjectShotRequest**](CreateProjectShotRequest.md)|  | 

### Return type

[**CreateProjectShot201Response**](CreateProjectShot201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Shot created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_episode**
> delete_episode(episode_id)

Delete episode

Delete an episode by id. Requires manager access or ownership.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Delete episode
        await api_instance.delete_episode(episode_id)
    except Exception as e:
        print("Exception when calling ShotsApi->delete_episode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_id** | **UUID**|  | 

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
**204** | Episode deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_given_shot_from_given_scene**
> delete_given_shot_from_given_scene(scene_id, shot_id)

Delete given shot from given scene.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    scene_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    shot_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Delete given shot from given scene.
        await api_instance.delete_given_shot_from_given_scene(scene_id, shot_id)
    except Exception as e:
        print("Exception when calling ShotsApi->delete_given_shot_from_given_scene: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **UUID**|  | 
 **shot_id** | **UUID**|  | 

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
**204** | Given shot deleted from given scene |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scene**
> delete_scene(scene_id)

Delete scene

Delete a scene by id. Requires manager access or ownership.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    scene_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Delete scene
        await api_instance.delete_scene(scene_id)
    except Exception as e:
        print("Exception when calling ShotsApi->delete_scene: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **UUID**|  | 

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
**204** | Scene deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sequence**
> delete_sequence(sequence_id)

Delete sequence

Delete a sequence by id. Requires manager access or ownership.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Delete sequence
        await api_instance.delete_sequence(sequence_id)
    except Exception as e:
        print("Exception when calling ShotsApi->delete_sequence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**|  | 

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
**204** | Sequence deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shot**
> delete_shot(shot_id)

Delete shot

Delete a shot by id. Requires manager access or ownership of the shot.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    shot_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Delete shot
        await api_instance.delete_shot(shot_id)
    except Exception as e:
        print("Exception when calling ShotsApi->delete_shot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | **UUID**|  | 

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
**204** | Shot deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_shots**
> List[Shot] get_all_shots(sequence_id=sequence_id, project_id=project_id, parent_id=parent_id)

Get all shots

Get all shots across projects with optional filters. Use sequence_id, project_id, or parent_id to filter.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)
    parent_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)

    try:
        # Get all shots
        api_response = await api_instance.get_all_shots(sequence_id=sequence_id, project_id=project_id, parent_id=parent_id)
        print("The response of ShotsApi->get_all_shots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_all_shots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**|  | [optional] 
 **project_id** | **UUID**|  | [optional] 
 **parent_id** | **UUID**|  | [optional] 

### Return type

[**List[Shot]**](Shot.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All shot entries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episode**
> Episode get_episode(episode_id)

Get episode

Get an episode by id. needs.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.episode import Episode
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get episode
        api_response = await api_instance.get_episode(episode_id)
        print("The response of ShotsApi->get_episode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_episode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_id** | **UUID**|  | 

### Return type

[**Episode**](Episode.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Episode found and returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episode_asset_tasks**
> List[Task] get_episode_asset_tasks(episode_id)

Get episode asset tasks

Get asset tasks for an episode. Restricted for vendor permissions.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get episode asset tasks
        api_response = await api_instance.get_episode_asset_tasks(episode_id)
        print("The response of ShotsApi->get_episode_asset_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_episode_asset_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_id** | **UUID**|  | 

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
**200** | All assets tasks related to given episode |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episode_retake_stats**
> Dict[str, GetEpisodeRetakeStats200ResponseValue] get_episode_retake_stats(project_id)

Get episode retake stats

Return retake and done counts by task type and episode. Includes evolution data and max retake count.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_episode_retake_stats200_response_value import GetEpisodeRetakeStats200ResponseValue
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get episode retake stats
        api_response = await api_instance.get_episode_retake_stats(project_id)
        print("The response of ShotsApi->get_episode_retake_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_episode_retake_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 

### Return type

[**Dict[str, GetEpisodeRetakeStats200ResponseValue]**](GetEpisodeRetakeStats200ResponseValue.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Number of tasks by status, task types and episodes for given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episode_sequences**
> List[Sequence] get_episode_sequences(episode_id, project_id=project_id)

Get episode sequences

Get sequences for an episode. You can add query filters if needed.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.sequence import Sequence
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)

    try:
        # Get episode sequences
        api_response = await api_instance.get_episode_sequences(episode_id, project_id=project_id)
        print("The response of ShotsApi->get_episode_sequences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_episode_sequences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_id** | **UUID**|  | 
 **project_id** | **UUID**|  | [optional] 

### Return type

[**List[Sequence]**](Sequence.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All sequence entries for given episode |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episode_shot_tasks**
> List[Task] get_episode_shot_tasks(episode_id)

Get episode shot tasks

Get shot tasks for an episode. Restricted for vendor permissions.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get episode shot tasks
        api_response = await api_instance.get_episode_shot_tasks(episode_id)
        print("The response of ShotsApi->get_episode_shot_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_episode_shot_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_id** | **UUID**|  | 

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
**200** | All shot tasks related to given episode |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episode_shots**
> List[Shot] get_episode_shots(episode_id)

Get episode shots

Get shots for an episode. Supports including relations via query params.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get episode shots
        api_response = await api_instance.get_episode_shots(episode_id)
        print("The response of ShotsApi->get_episode_shots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_episode_shots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_id** | **UUID**|  | 

### Return type

[**List[Shot]**](Shot.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All shots related to given episode |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episode_stats**
> Dict[str, Dict[str, Dict[str, GetEpisodeStats200ResponseValueValueValue]]] get_episode_stats(project_id)

Get episode stats

Return number of tasks by status, task type and episode for the project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_episode_stats200_response_value_value_value import GetEpisodeStats200ResponseValueValueValue
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get episode stats
        api_response = await api_instance.get_episode_stats(project_id)
        print("The response of ShotsApi->get_episode_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_episode_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 

### Return type

**Dict[str, Dict[str, Dict[str, GetEpisodeStats200ResponseValueValueValue]]]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Number of tasks by status, task types and episodes for given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episode_task_types**
> List[GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner] get_episode_task_types(episode_id)

Get episode task types

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shot_task_types_get_data_shots_shot_id_task_types200_response_inner import GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get episode task types
        api_response = await api_instance.get_episode_task_types(episode_id)
        print("The response of ShotsApi->get_episode_task_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_episode_task_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_id** | **UUID**|  | 

### Return type

[**List[GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner]**](GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All task types related to given episode |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episode_tasks**
> List[Task] get_episode_tasks(episode_id)

Get episode tasks

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get episode tasks
        api_response = await api_instance.get_episode_tasks(episode_id)
        print("The response of ShotsApi->get_episode_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_episode_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_id** | **UUID**|  | 

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
**200** | All tasks related to given episode |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episodes**
> List[Episode] get_episodes(project_id=project_id)

Get episodes

Get episodes with optional filters. Use project_id to filter by project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.episode import Episode
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)

    try:
        # Get episodes
        api_response = await api_instance.get_episodes(project_id=project_id)
        print("The response of ShotsApi->get_episodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_episodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | [optional] 

### Return type

[**List[Episode]**](Episode.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All episode entries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episodes_and_tasks**
> List[GetEpisodesAndTasks200ResponseInner] get_episodes_and_tasks(project_id=project_id)

Get episodes and tasks

Get episodes and their related tasks. Optionally filter by project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_episodes_and_tasks200_response_inner import GetEpisodesAndTasks200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)

    try:
        # Get episodes and tasks
        api_response = await api_instance.get_episodes_and_tasks(project_id=project_id)
        print("The response of ShotsApi->get_episodes_and_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_episodes_and_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | [optional] 

### Return type

[**List[GetEpisodesAndTasks200ResponseInner]**](GetEpisodesAndTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All episodes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_episodes_get_data_projects_project_id_episodes**
> List[Episode] get_project_episodes_get_data_projects_project_id_episodes(project_id)

Get project episodes

Get episodes for a project. May limit to assigned items for vendor users.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.episode import Episode
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get project episodes
        api_response = await api_instance.get_project_episodes_get_data_projects_project_id_episodes(project_id)
        print("The response of ShotsApi->get_project_episodes_get_data_projects_project_id_episodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_project_episodes_get_data_projects_project_id_episodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 

### Return type

[**List[Episode]**](Episode.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All episodes related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_person_quotas**
> Dict[str, GetProjectPersonQuotas200ResponseValue] get_project_person_quotas(project_id, person_id, count_mode, studio_id=studio_id)

Get project person quotas

Get quotas statistics for a person in a project. Supports weighted and raw modes with optional feedback filtering.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_person_quotas200_response_value import GetProjectPersonQuotas200ResponseValue
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    count_mode = 'weighted' # str | 
    studio_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)

    try:
        # Get project person quotas
        api_response = await api_instance.get_project_person_quotas(project_id, person_id, count_mode, studio_id=studio_id)
        print("The response of ShotsApi->get_project_person_quotas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_project_person_quotas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **person_id** | **UUID**|  | 
 **count_mode** | **str**|  | 
 **studio_id** | **UUID**|  | [optional] 

### Return type

[**Dict[str, GetProjectPersonQuotas200ResponseValue]**](GetProjectPersonQuotas200ResponseValue.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quotas statistics for shots |  -  |
**400** | Invalid count_mode or parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_quotas**
> Dict[str, GetProjectQuotas200ResponseValue] get_project_quotas(project_id, task_type_id, count_mode, studio_id=studio_id)

Get project quotas

Get quotas statistics for a project and task type. Supports weighted and raw modes with optional feedback filtering.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_quotas200_response_value import GetProjectQuotas200ResponseValue
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    count_mode = 'weighted' # str | 
    studio_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)

    try:
        # Get project quotas
        api_response = await api_instance.get_project_quotas(project_id, task_type_id, count_mode, studio_id=studio_id)
        print("The response of ShotsApi->get_project_quotas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_project_quotas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 
 **task_type_id** | **UUID**|  | 
 **count_mode** | **str**|  | 
 **studio_id** | **UUID**|  | [optional] 

### Return type

[**Dict[str, GetProjectQuotas200ResponseValue]**](GetProjectQuotas200ResponseValue.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quotas statistics for shots |  -  |
**400** | Invalid count_mode or parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_scenes**
> List[GetProjectScenes200ResponseInner] get_project_scenes(project_id)

Get project scenes

Get all scenes for a project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_scenes200_response_inner import GetProjectScenes200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get project scenes
        api_response = await api_instance.get_project_scenes(project_id)
        print("The response of ShotsApi->get_project_scenes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_project_scenes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 

### Return type

[**List[GetProjectScenes200ResponseInner]**](GetProjectScenes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All scenes related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_sequences_get_data_projects_project_id_sequences**
> List[GetProjectSequencesGetDataProjectsProjectIdSequences200ResponseInner] get_project_sequences_get_data_projects_project_id_sequences(project_id)

Get project sequences

Get sequences for a project. May limit to assigned items for vendor users.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_sequences_get_data_projects_project_id_sequences200_response_inner import GetProjectSequencesGetDataProjectsProjectIdSequences200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get project sequences
        api_response = await api_instance.get_project_sequences_get_data_projects_project_id_sequences(project_id)
        print("The response of ShotsApi->get_project_sequences_get_data_projects_project_id_sequences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_project_sequences_get_data_projects_project_id_sequences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 

### Return type

[**List[GetProjectSequencesGetDataProjectsProjectIdSequences200ResponseInner]**](GetProjectSequencesGetDataProjectsProjectIdSequences200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All sequences related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_shots**
> List[Shot] get_project_shots(project_id)

Get project shots

Get shots for a project. May limit to assigned shots for vendor users.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get project shots
        api_response = await api_instance.get_project_shots(project_id)
        print("The response of ShotsApi->get_project_shots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_project_shots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | 

### Return type

[**List[Shot]**](Shot.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All shots related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scene**
> GetScenes200ResponseInner get_scene(scene_id)

Get scene

Get a scene by id. Returns full scene data needed by clients.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_scenes200_response_inner import GetScenes200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    scene_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get scene
        api_response = await api_instance.get_scene(scene_id)
        print("The response of ShotsApi->get_scene:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_scene: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **UUID**|  | 

### Return type

[**GetScenes200ResponseInner**](GetScenes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scene found and returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scene_shots**
> List[GetSceneShots200ResponseInner] get_scene_shots(scene_id)

Get scene shots

Get shots that come from a scene.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_scene_shots200_response_inner import GetSceneShots200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    scene_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get scene shots
        api_response = await api_instance.get_scene_shots(scene_id)
        print("The response of ShotsApi->get_scene_shots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_scene_shots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **UUID**|  | 

### Return type

[**List[GetSceneShots200ResponseInner]**](GetSceneShots200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All shots that come from given scene |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scene_task_types_get_data_scenes_scene_id_task_types**
> List[GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner] get_scene_task_types_get_data_scenes_scene_id_task_types(scene_id)

Get scene task types

Get task types for a scene.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shot_task_types_get_data_shots_shot_id_task_types200_response_inner import GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    scene_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get scene task types
        api_response = await api_instance.get_scene_task_types_get_data_scenes_scene_id_task_types(scene_id)
        print("The response of ShotsApi->get_scene_task_types_get_data_scenes_scene_id_task_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_scene_task_types_get_data_scenes_scene_id_task_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **UUID**|  | 

### Return type

[**List[GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner]**](GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All task types related to given scene |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scene_tasks_get_data_scenes_scene_id_tasks**
> List[Task] get_scene_tasks_get_data_scenes_scene_id_tasks(scene_id)

Get scene tasks

Get tasks for a scene.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    scene_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get scene tasks
        api_response = await api_instance.get_scene_tasks_get_data_scenes_scene_id_tasks(scene_id)
        print("The response of ShotsApi->get_scene_tasks_get_data_scenes_scene_id_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_scene_tasks_get_data_scenes_scene_id_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **UUID**|  | 

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
**200** | All tasks related to given scene |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenes**
> List[GetScenes200ResponseInner] get_scenes(project_id=project_id)

Get scenes

Get scenes with optional filters. Use project_id to filter by project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_scenes200_response_inner import GetScenes200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)

    try:
        # Get scenes
        api_response = await api_instance.get_scenes(project_id=project_id)
        print("The response of ShotsApi->get_scenes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_scenes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | [optional] 

### Return type

[**List[GetScenes200ResponseInner]**](GetScenes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All scene entries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenes_and_tasks**
> List[GetScenesAndTasks200ResponseInner] get_scenes_and_tasks(project_id=project_id)

Get scenes and tasks

Get scenes and their related tasks. Optionally filter by project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_scenes_and_tasks200_response_inner import GetScenesAndTasks200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)

    try:
        # Get scenes and tasks
        api_response = await api_instance.get_scenes_and_tasks(project_id=project_id)
        print("The response of ShotsApi->get_scenes_and_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_scenes_and_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | [optional] 

### Return type

[**List[GetScenesAndTasks200ResponseInner]**](GetScenesAndTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All scenes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence**
> Sequence get_sequence(sequence_id)

Get sequence

Get a sequence by id.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.sequence import Sequence
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get sequence
        api_response = await api_instance.get_sequence(sequence_id)
        print("The response of ShotsApi->get_sequence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_sequence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**|  | 

### Return type

[**Sequence**](Sequence.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sequence found and returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence_scenes_get_data_sequences_sequence_id_scenes**
> List[Sequence] get_sequence_scenes_get_data_sequences_sequence_id_scenes(sequence_id)

Get sequence scenes

Get scenes that belong to a sequence.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.sequence import Sequence
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get sequence scenes
        api_response = await api_instance.get_sequence_scenes_get_data_sequences_sequence_id_scenes(sequence_id)
        print("The response of ShotsApi->get_sequence_scenes_get_data_sequences_sequence_id_scenes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_sequence_scenes_get_data_sequences_sequence_id_scenes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**|  | 

### Return type

[**List[Sequence]**](Sequence.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All scenes related to given sequence |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence_shot_tasks**
> List[Task] get_sequence_shot_tasks(sequence_id)

Get sequence shot tasks

Get shot tasks for a sequence. Restricted for vendor permissions.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get sequence shot tasks
        api_response = await api_instance.get_sequence_shot_tasks(sequence_id)
        print("The response of ShotsApi->get_sequence_shot_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_sequence_shot_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**|  | 

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
**200** | All shot tasks related to given sequence |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence_shots_get_data_sequences_sequence_id_shots**
> List[Shot] get_sequence_shots_get_data_sequences_sequence_id_shots(sequence_id, project_id=project_id)

Get sequence shots

Get shots for a sequence. Supports filtering using query params.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)

    try:
        # Get sequence shots
        api_response = await api_instance.get_sequence_shots_get_data_sequences_sequence_id_shots(sequence_id, project_id=project_id)
        print("The response of ShotsApi->get_sequence_shots_get_data_sequences_sequence_id_shots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_sequence_shots_get_data_sequences_sequence_id_shots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**|  | 
 **project_id** | **UUID**|  | [optional] 

### Return type

[**List[Shot]**](Shot.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All shot entries for given sequence |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence_task_types_get_data_sequences_sequence_id_task_types**
> List[GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner] get_sequence_task_types_get_data_sequences_sequence_id_task_types(sequence_id)

Get sequence task types

Get task types for a sequence.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shot_task_types_get_data_shots_shot_id_task_types200_response_inner import GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get sequence task types
        api_response = await api_instance.get_sequence_task_types_get_data_sequences_sequence_id_task_types(sequence_id)
        print("The response of ShotsApi->get_sequence_task_types_get_data_sequences_sequence_id_task_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_sequence_task_types_get_data_sequences_sequence_id_task_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**|  | 

### Return type

[**List[GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner]**](GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All task types related to given shot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence_tasks_get_data_sequences_sequence_id_tasks**
> List[Task] get_sequence_tasks_get_data_sequences_sequence_id_tasks(sequence_id)

Get sequence tasks

Get tasks for a sequence. Optionally include relations using query params.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get sequence tasks
        api_response = await api_instance.get_sequence_tasks_get_data_sequences_sequence_id_tasks(sequence_id)
        print("The response of ShotsApi->get_sequence_tasks_get_data_sequences_sequence_id_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_sequence_tasks_get_data_sequences_sequence_id_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**|  | 

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
**200** | All tasks related to given shot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequences**
> List[Sequence] get_sequences(episode_id=episode_id)

Get sequences

Get sequences with optional filters. Use episode_id to filter by episode.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.sequence import Sequence
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)

    try:
        # Get sequences
        api_response = await api_instance.get_sequences(episode_id=episode_id)
        print("The response of ShotsApi->get_sequences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_sequences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_id** | **UUID**|  | [optional] 

### Return type

[**List[Sequence]**](Sequence.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All sequence entries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequences_and_tasks**
> List[GetSequencesAndTasks200ResponseInner] get_sequences_and_tasks(project_id=project_id)

Get sequences and tasks

Get sequences and their related tasks. Optionally filter by project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_sequences_and_tasks200_response_inner import GetSequencesAndTasks200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)

    try:
        # Get sequences and tasks
        api_response = await api_instance.get_sequences_and_tasks(project_id=project_id)
        print("The response of ShotsApi->get_sequences_and_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_sequences_and_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | [optional] 

### Return type

[**List[GetSequencesAndTasks200ResponseInner]**](GetSequencesAndTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All sequences |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot**
> GetShot200Response get_shot(shot_id)

Get shot

Get a shot by id. Returns full shot data. Use this to fetch a single shot with all fields needed by the UI.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shot200_response import GetShot200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    shot_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get shot
        api_response = await api_instance.get_shot(shot_id)
        print("The response of ShotsApi->get_shot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_shot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | **UUID**|  | 

### Return type

[**GetShot200Response**](GetShot200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shot found and returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_assets**
> List[GetShotAssets200ResponseInner] get_shot_assets(shot_id)

Get shot assets

Get assets linked to a shot. Returns the breakdown casting for the shot.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shot_assets200_response_inner import GetShotAssets200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    shot_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get shot assets
        api_response = await api_instance.get_shot_assets(shot_id)
        print("The response of ShotsApi->get_shot_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_shot_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | **UUID**|  | 

### Return type

[**List[GetShotAssets200ResponseInner]**](GetShotAssets200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All assets for given shot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_previews**
> Dict[str, List[GetShotPreviews200ResponseValueInner]] get_shot_previews(shot_id)

Get shot previews

Return previews for a shot as a dict keyed by task type id. Each value is an array of previews for that task type.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shot_previews200_response_value_inner import GetShotPreviews200ResponseValueInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    shot_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get shot previews
        api_response = await api_instance.get_shot_previews(shot_id)
        print("The response of ShotsApi->get_shot_previews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_shot_previews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | **UUID**|  | 

### Return type

**Dict[str, List[GetShotPreviews200ResponseValueInner]]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All previews related to given shot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_task_types_get_data_shots_shot_id_task_types**
> List[GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner] get_shot_task_types_get_data_shots_shot_id_task_types(shot_id)

Get shot task types

Get task types for a shot.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shot_task_types_get_data_shots_shot_id_task_types200_response_inner import GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    shot_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get shot task types
        api_response = await api_instance.get_shot_task_types_get_data_shots_shot_id_task_types(shot_id)
        print("The response of ShotsApi->get_shot_task_types_get_data_shots_shot_id_task_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_shot_task_types_get_data_shots_shot_id_task_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | **UUID**|  | 

### Return type

[**List[GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner]**](GetShotTaskTypesGetDataShotsShotIdTaskTypes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All task types related to given shot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_tasks_get_data_shots_shot_id_tasks**
> List[Task] get_shot_tasks_get_data_shots_shot_id_tasks(shot_id)

Get shot tasks

Get tasks for a shot. Optionally include relations using query params.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    shot_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get shot tasks
        api_response = await api_instance.get_shot_tasks_get_data_shots_shot_id_tasks(shot_id)
        print("The response of ShotsApi->get_shot_tasks_get_data_shots_shot_id_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_shot_tasks_get_data_shots_shot_id_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | **UUID**|  | 

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
**200** | All tasks related to given shot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_versions**
> List[GetShotVersions200ResponseInner] get_shot_versions(shot_id)

Get shot versions

Get data versions of a shot. Use this to inspect version history.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shot_versions200_response_inner import GetShotVersions200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    shot_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 

    try:
        # Get shot versions
        api_response = await api_instance.get_shot_versions(shot_id)
        print("The response of ShotsApi->get_shot_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_shot_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | **UUID**|  | 

### Return type

[**List[GetShotVersions200ResponseInner]**](GetShotVersions200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data versions of given shot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shots**
> List[Shot] get_shots(sequence_id=sequence_id, project_id=project_id, parent_id=parent_id)

Get shots

Get shots with optional filters. Use query params like project_id, sequence_id or parent_id to filter results.

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
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    sequence_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)
    parent_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)

    try:
        # Get shots
        api_response = await api_instance.get_shots(sequence_id=sequence_id, project_id=project_id, parent_id=parent_id)
        print("The response of ShotsApi->get_shots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_shots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **UUID**|  | [optional] 
 **project_id** | **UUID**|  | [optional] 
 **parent_id** | **UUID**|  | [optional] 

### Return type

[**List[Shot]**](Shot.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All shot entries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shots_and_tasks**
> List[GetShotsAndTasks200ResponseInner] get_shots_and_tasks(project_id=project_id)

Get shots and tasks

Get shots and their related tasks. Optionally filter by project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shots_and_tasks200_response_inner import GetShotsAndTasks200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID |  (optional)

    try:
        # Get shots and tasks
        api_response = await api_instance.get_shots_and_tasks(project_id=project_id)
        print("The response of ShotsApi->get_shots_and_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->get_shots_and_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**|  | [optional] 

### Return type

[**List[GetShotsAndTasks200ResponseInner]**](GetShotsAndTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All shots |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_shot_to_scene**
> LinkShotToScene201Response link_shot_to_scene(scene_id, link_shot_to_scene_request)

Link shot to scene

Link a shot to a scene as its source.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.link_shot_to_scene201_response import LinkShotToScene201Response
from sometech.pykitsu._client.models.link_shot_to_scene_request import LinkShotToSceneRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    scene_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    link_shot_to_scene_request = sometech.pykitsu._client.LinkShotToSceneRequest() # LinkShotToSceneRequest | 

    try:
        # Link shot to scene
        api_response = await api_instance.link_shot_to_scene(scene_id, link_shot_to_scene_request)
        print("The response of ShotsApi->link_shot_to_scene:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->link_shot_to_scene: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **UUID**|  | 
 **link_shot_to_scene_request** | [**LinkShotToSceneRequest**](LinkShotToSceneRequest.md)|  | 

### Return type

[**LinkShotToScene201Response**](LinkShotToScene201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Scene marked as source of shot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_shots_frames**
> SetShotsFrames200Response set_shots_frames(project_id, task_type_id, set_shots_frames_request)

Set shots frames

Set number of frames on shots based on latest preview files for a task type. Optionally scope by episode via query param.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.set_shots_frames200_response import SetShotsFrames200Response
from sometech.pykitsu._client.models.set_shots_frames_request import SetShotsFramesRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    project_id = 'project_id_example' # str | 
    task_type_id = 'task_type_id_example' # str | 
    set_shots_frames_request = sometech.pykitsu._client.SetShotsFramesRequest() # SetShotsFramesRequest | 

    try:
        # Set shots frames
        api_response = await api_instance.set_shots_frames(project_id, task_type_id, set_shots_frames_request)
        print("The response of ShotsApi->set_shots_frames:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->set_shots_frames: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **task_type_id** | **str**|  | 
 **set_shots_frames_request** | [**SetShotsFramesRequest**](SetShotsFramesRequest.md)|  | 

### Return type

[**SetShotsFrames200Response**](SetShotsFrames200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Frames set for given shots |  -  |
**400** | Invalid ids or parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shot**
> GetShot200Response update_shot(shot_id, update_shot_request)

Update shot

Update a shot by id. Only mutable fields are allowed. Send a JSON body with the fields to change.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shot200_response import GetShot200Response
from sometech.pykitsu._client.models.update_shot_request import UpdateShotRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ShotsApi(api_client)
    shot_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | 
    update_shot_request = sometech.pykitsu._client.UpdateShotRequest() # UpdateShotRequest | 

    try:
        # Update shot
        api_response = await api_instance.update_shot(shot_id, update_shot_request)
        print("The response of ShotsApi->update_shot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShotsApi->update_shot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | **UUID**|  | 
 **update_shot_request** | [**UpdateShotRequest**](UpdateShotRequest.md)|  | 

### Return type

[**GetShot200Response**](GetShot200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shot updated |  -  |
**400** | Invalid body or unsupported fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

