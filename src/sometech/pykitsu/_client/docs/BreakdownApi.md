# sometech.pykitsu._client.BreakdownApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_shot_asset_instance**](BreakdownApi.md#add_shot_asset_instance) | **POST** /data/shots/{shot_id}/asset-instances | Add shot asset instance
[**create_scene_asset_instance**](BreakdownApi.md#create_scene_asset_instance) | **POST** /data/scenes/{scene_id}/asset-instances | Create scene asset instance
[**delete_entity_link_delete_data_projects_project_id_entity_links_entity_link_id**](BreakdownApi.md#delete_entity_link_delete_data_projects_project_id_entity_links_entity_link_id) | **DELETE** /data/projects/{project_id}/entity-links/{entity_link_id} | Delete entity link
[**get_asset_type_casting**](BreakdownApi.md#get_asset_type_casting) | **GET** /data/projects/{project_id}/asset-types/{asset_type_id}/casting | Get asset type casting
[**get_entity_casting**](BreakdownApi.md#get_entity_casting) | **GET** /data/projects/{project_id}/entities/{entity_id}/casting | Get entity casting
[**get_episode_shots_casting**](BreakdownApi.md#get_episode_shots_casting) | **GET** /data/projects/{project_id}/episodes/{episode_id}/sequences/all/casting | Get episode shots casting
[**get_episodes_casting**](BreakdownApi.md#get_episodes_casting) | **GET** /data/projects/{project_id}/episodes/casting | Get episodes casting
[**get_project_entity_links**](BreakdownApi.md#get_project_entity_links) | **GET** /data/projects/{project_id}/entity-links | Get project entity links
[**get_project_shots_casting**](BreakdownApi.md#get_project_shots_casting) | **GET** /data/projects/{project_id}/sequences/all/casting | Get project shots casting
[**get_scene_asset_instances_get_data_scenes_scene_id_asset_instances**](BreakdownApi.md#get_scene_asset_instances_get_data_scenes_scene_id_asset_instances) | **GET** /data/scenes/{scene_id}/asset-instances | Get scene asset instances
[**get_scene_camera_instances**](BreakdownApi.md#get_scene_camera_instances) | **GET** /data/scenes/{scene_id}/camera-instances | Get scene camera instances
[**get_sequence_shots_casting**](BreakdownApi.md#get_sequence_shots_casting) | **GET** /data/projects/{project_id}/sequences/{sequence_id}/casting | Get sequence shots casting
[**get_shot_asset_instances_get_data_shots_shot_id_asset_instances**](BreakdownApi.md#get_shot_asset_instances_get_data_shots_shot_id_asset_instances) | **GET** /data/shots/{shot_id}/asset-instances | Get shot asset instances
[**remove_shot_asset_instance**](BreakdownApi.md#remove_shot_asset_instance) | **DELETE** /data/shots/{shot_id}/asset-instances/{asset_instance_id} | Remove shot asset instance
[**update_entity_casting**](BreakdownApi.md#update_entity_casting) | **PUT** /data/projects/{project_id}/entities/{entity_id}/casting | Update entity casting


# **add_shot_asset_instance**
> AddShotAssetInstance201Response add_shot_asset_instance(shot_id, add_shot_asset_instance_request)

Add shot asset instance

Add an asset instance to a specific shot.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_shot_asset_instance201_response import AddShotAssetInstance201Response
from sometech.pykitsu._client.models.add_shot_asset_instance_request import AddShotAssetInstanceRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    shot_id = UUID('e68e0ie8-gi19-8009-e514-91897426g69') # UUID | Unique identifier of the shot
    add_shot_asset_instance_request = sometech.pykitsu._client.AddShotAssetInstanceRequest() # AddShotAssetInstanceRequest | 

    try:
        # Add shot asset instance
        api_response = await api_instance.add_shot_asset_instance(shot_id, add_shot_asset_instance_request)
        print("The response of BreakdownApi->add_shot_asset_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakdownApi->add_shot_asset_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | **UUID**| Unique identifier of the shot | 
 **add_shot_asset_instance_request** | [**AddShotAssetInstanceRequest**](AddShotAssetInstanceRequest.md)|  | 

### Return type

[**AddShotAssetInstance201Response**](AddShotAssetInstance201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Asset instance successfully added to shot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_scene_asset_instance**
> GetSceneAssetInstancesGetDataScenesSceneIdAssetInstances200ResponseInner create_scene_asset_instance(scene_id, create_scene_asset_instance_request)

Create scene asset instance

Create an asset instance on a specific scene.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_scene_asset_instance_request import CreateSceneAssetInstanceRequest
from sometech.pykitsu._client.models.get_scene_asset_instances_get_data_scenes_scene_id_asset_instances200_response_inner import GetSceneAssetInstancesGetDataScenesSceneIdAssetInstances200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    scene_id = UUID('i02i4mi2-km53-2443-i958-35231870k03') # UUID | Unique identifier of the scene
    create_scene_asset_instance_request = sometech.pykitsu._client.CreateSceneAssetInstanceRequest() # CreateSceneAssetInstanceRequest | 

    try:
        # Create scene asset instance
        api_response = await api_instance.create_scene_asset_instance(scene_id, create_scene_asset_instance_request)
        print("The response of BreakdownApi->create_scene_asset_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakdownApi->create_scene_asset_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **UUID**| Unique identifier of the scene | 
 **create_scene_asset_instance_request** | [**CreateSceneAssetInstanceRequest**](CreateSceneAssetInstanceRequest.md)|  | 

### Return type

[**GetSceneAssetInstancesGetDataScenesSceneIdAssetInstances200ResponseInner**](GetSceneAssetInstancesGetDataScenesSceneIdAssetInstances200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Asset instance successfully created on scene |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity_link_delete_data_projects_project_id_entity_links_entity_link_id**
> delete_entity_link_delete_data_projects_project_id_entity_links_entity_link_id(project_id, entity_link_id)

Delete entity link

Delete a specific entity link. It's mainly used for synchronisation purpose.

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
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    entity_link_id = UUID('m46m8qm6-oq97-6887-m403-80786315o47') # UUID | Unique identifier of the entity link

    try:
        # Delete entity link
        await api_instance.delete_entity_link_delete_data_projects_project_id_entity_links_entity_link_id(project_id, entity_link_id)
    except Exception as e:
        print("Exception when calling BreakdownApi->delete_entity_link_delete_data_projects_project_id_entity_links_entity_link_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **entity_link_id** | **UUID**| Unique identifier of the entity link | 

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
**200** | Entity link successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_type_casting**
> List[GetAssetTypeCasting200ResponseInner] get_asset_type_casting(project_id, asset_type_id)

Get asset type casting

Retrieve the casting information for all assets of a specific asset type in a project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_asset_type_casting200_response_inner import GetAssetTypeCasting200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    asset_type_id = UUID('g80g2kg0-ik31-0221-g736-13019648i81') # UUID | Unique identifier of the asset type

    try:
        # Get asset type casting
        api_response = await api_instance.get_asset_type_casting(project_id, asset_type_id)
        print("The response of BreakdownApi->get_asset_type_casting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakdownApi->get_asset_type_casting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **asset_type_id** | **UUID**| Unique identifier of the asset type | 

### Return type

[**List[GetAssetTypeCasting200ResponseInner]**](GetAssetTypeCasting200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset type casting information successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_casting**
> GetEntityCasting200Response get_entity_casting(project_id, entity_id)

Get entity casting

Retrieve the casting information for a specific entity showing which assets are linked to it.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_entity_casting200_response import GetEntityCasting200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the entity

    try:
        # Get entity casting
        api_response = await api_instance.get_entity_casting(project_id, entity_id)
        print("The response of BreakdownApi->get_entity_casting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakdownApi->get_entity_casting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **entity_id** | **UUID**| Unique identifier of the entity | 

### Return type

[**GetEntityCasting200Response**](GetEntityCasting200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity casting information successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episode_shots_casting**
> List[GetEpisodeShotsCasting200ResponseInner] get_episode_shots_casting(project_id, episode_id)

Get episode shots casting

Retrieve the casting information for all shots from a specific episode.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_episode_shots_casting200_response_inner import GetEpisodeShotsCasting200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    episode_id = UUID('d57d9hd7-fh08-7998-d403-80786315f58') # UUID | Unique identifier of the episode

    try:
        # Get episode shots casting
        api_response = await api_instance.get_episode_shots_casting(project_id, episode_id)
        print("The response of BreakdownApi->get_episode_shots_casting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakdownApi->get_episode_shots_casting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **episode_id** | **UUID**| Unique identifier of the episode | 

### Return type

[**List[GetEpisodeShotsCasting200ResponseInner]**](GetEpisodeShotsCasting200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Episode shots casting information successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episodes_casting**
> List[GetEpisodesCasting200ResponseInner] get_episodes_casting(project_id)

Get episodes casting

Retrieve the casting information for all episodes in a specific project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_episodes_casting200_response_inner import GetEpisodesCasting200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project

    try:
        # Get episodes casting
        api_response = await api_instance.get_episodes_casting(project_id)
        print("The response of BreakdownApi->get_episodes_casting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakdownApi->get_episodes_casting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 

### Return type

[**List[GetEpisodesCasting200ResponseInner]**](GetEpisodesCasting200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Episodes casting information successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_entity_links**
> List[GetProjectEntityLinks200ResponseInner] get_project_entity_links(project_id, page=page, limit=limit, cursor_created_at=cursor_created_at)

Get project entity links

Retrieve all entity links related to a specific project. Results can be paginated using page and limit query parameters. If you prefer a more accurate pagination, you can use cursor_created_at to get the next page. It's mainly used for synchronisation purpose.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_entity_links200_response_inner import GetProjectEntityLinks200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    page = 2 # int | Page number for pagination (optional)
    limit = 100 # int | Number of items per page (optional)
    cursor_created_at = '2020-01-01T00:00:00' # datetime | Cursor for pagination based on creation date (optional)

    try:
        # Get project entity links
        api_response = await api_instance.get_project_entity_links(project_id, page=page, limit=limit, cursor_created_at=cursor_created_at)
        print("The response of BreakdownApi->get_project_entity_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakdownApi->get_project_entity_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **page** | **int**| Page number for pagination | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **cursor_created_at** | **datetime**| Cursor for pagination based on creation date | [optional] 

### Return type

[**List[GetProjectEntityLinks200ResponseInner]**](GetProjectEntityLinks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project entity links successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_shots_casting**
> List[GetProjectShotsCasting200ResponseInner] get_project_shots_casting(project_id)

Get project shots casting

Retrieve the casting information for all shots from all sequences in a specific project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_shots_casting200_response_inner import GetProjectShotsCasting200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project

    try:
        # Get project shots casting
        api_response = await api_instance.get_project_shots_casting(project_id)
        print("The response of BreakdownApi->get_project_shots_casting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakdownApi->get_project_shots_casting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 

### Return type

[**List[GetProjectShotsCasting200ResponseInner]**](GetProjectShotsCasting200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project shots casting information successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scene_asset_instances_get_data_scenes_scene_id_asset_instances**
> List[GetSceneAssetInstancesGetDataScenesSceneIdAssetInstances200ResponseInner] get_scene_asset_instances_get_data_scenes_scene_id_asset_instances(scene_id)

Get scene asset instances

Retrieve all asset instances that are linked to a specific scene.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_scene_asset_instances_get_data_scenes_scene_id_asset_instances200_response_inner import GetSceneAssetInstancesGetDataScenesSceneIdAssetInstances200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    scene_id = UUID('i02i4mi2-km53-2443-i958-35231870k03') # UUID | Unique identifier of the scene

    try:
        # Get scene asset instances
        api_response = await api_instance.get_scene_asset_instances_get_data_scenes_scene_id_asset_instances(scene_id)
        print("The response of BreakdownApi->get_scene_asset_instances_get_data_scenes_scene_id_asset_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakdownApi->get_scene_asset_instances_get_data_scenes_scene_id_asset_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **UUID**| Unique identifier of the scene | 

### Return type

[**List[GetSceneAssetInstancesGetDataScenesSceneIdAssetInstances200ResponseInner]**](GetSceneAssetInstancesGetDataScenesSceneIdAssetInstances200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scene asset instances successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scene_camera_instances**
> List[GetSceneCameraInstances200ResponseInner] get_scene_camera_instances(scene_id)

Get scene camera instances

Retrieve all camera instances that are linked to a specific scene.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_scene_camera_instances200_response_inner import GetSceneCameraInstances200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    scene_id = UUID('i02i4mi2-km53-2443-i958-35231870k03') # UUID | Unique identifier of the scene

    try:
        # Get scene camera instances
        api_response = await api_instance.get_scene_camera_instances(scene_id)
        print("The response of BreakdownApi->get_scene_camera_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakdownApi->get_scene_camera_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_id** | **UUID**| Unique identifier of the scene | 

### Return type

[**List[GetSceneCameraInstances200ResponseInner]**](GetSceneCameraInstances200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scene camera instances successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence_shots_casting**
> List[GetSequenceShotsCasting200ResponseInner] get_sequence_shots_casting(project_id, sequence_id)

Get sequence shots casting

Retrieve the casting information for all shots from a specific sequence.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_sequence_shots_casting200_response_inner import GetSequenceShotsCasting200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    sequence_id = UUID('f79f1jf9-hj20-9110-f625-02908537h70') # UUID | Unique identifier of the sequence

    try:
        # Get sequence shots casting
        api_response = await api_instance.get_sequence_shots_casting(project_id, sequence_id)
        print("The response of BreakdownApi->get_sequence_shots_casting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakdownApi->get_sequence_shots_casting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **sequence_id** | **UUID**| Unique identifier of the sequence | 

### Return type

[**List[GetSequenceShotsCasting200ResponseInner]**](GetSequenceShotsCasting200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sequence shots casting information successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_asset_instances_get_data_shots_shot_id_asset_instances**
> List[GetShotAssetInstancesGetDataShotsShotIdAssetInstances200ResponseInner] get_shot_asset_instances_get_data_shots_shot_id_asset_instances(shot_id)

Get shot asset instances

Retrieve all asset instances that are linked to a specific shot.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shot_asset_instances_get_data_shots_shot_id_asset_instances200_response_inner import GetShotAssetInstancesGetDataShotsShotIdAssetInstances200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    shot_id = UUID('e68e0ie8-gi19-8009-e514-91897426g69') # UUID | Unique identifier of the shot

    try:
        # Get shot asset instances
        api_response = await api_instance.get_shot_asset_instances_get_data_shots_shot_id_asset_instances(shot_id)
        print("The response of BreakdownApi->get_shot_asset_instances_get_data_shots_shot_id_asset_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakdownApi->get_shot_asset_instances_get_data_shots_shot_id_asset_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | **UUID**| Unique identifier of the shot | 

### Return type

[**List[GetShotAssetInstancesGetDataShotsShotIdAssetInstances200ResponseInner]**](GetShotAssetInstancesGetDataShotsShotIdAssetInstances200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shot asset instances successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shot_asset_instance**
> remove_shot_asset_instance(shot_id, asset_instance_id)

Remove shot asset instance

Remove an asset instance from a specific shot.

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
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    shot_id = UUID('e68e0ie8-gi19-8009-e514-91897426g69') # UUID | Unique identifier of the shot
    asset_instance_id = UUID('h91h3lh1-jl42-1332-h847-24120759j92') # UUID | Unique identifier of the asset instance

    try:
        # Remove shot asset instance
        await api_instance.remove_shot_asset_instance(shot_id, asset_instance_id)
    except Exception as e:
        print("Exception when calling BreakdownApi->remove_shot_asset_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | **UUID**| Unique identifier of the shot | 
 **asset_instance_id** | **UUID**| Unique identifier of the asset instance | 

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
**204** | Asset instance successfully removed from shot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity_casting**
> GetEntityCasting200Response update_entity_casting(project_id, entity_id, update_entity_casting_request)

Update entity casting

Modify the casting relationships for a specific entity by updating which assets are linked to it.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_entity_casting200_response import GetEntityCasting200Response
from sometech.pykitsu._client.models.update_entity_casting_request import UpdateEntityCastingRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.BreakdownApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the entity
    update_entity_casting_request = sometech.pykitsu._client.UpdateEntityCastingRequest() # UpdateEntityCastingRequest | 

    try:
        # Update entity casting
        api_response = await api_instance.update_entity_casting(project_id, entity_id, update_entity_casting_request)
        print("The response of BreakdownApi->update_entity_casting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakdownApi->update_entity_casting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **entity_id** | **UUID**| Unique identifier of the entity | 
 **update_entity_casting_request** | [**UpdateEntityCastingRequest**](UpdateEntityCastingRequest.md)|  | 

### Return type

[**GetEntityCasting200Response**](GetEntityCasting200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity casting successfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

