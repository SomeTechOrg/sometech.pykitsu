# sometech.pykitsu._client.AssetsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset**](AssetsApi.md#create_asset) | **POST** /data/projects/{project_id}/asset-types/{asset_type_id}/assets/new | Create asset
[**create_asset_instance_post_data_assets_asset_id_asset_asset_instances**](AssetsApi.md#create_asset_instance_post_data_assets_asset_id_asset_asset_instances) | **POST** /data/assets/{asset_id}/asset-asset-instances | Create asset instance
[**delete_asset**](AssetsApi.md#delete_asset) | **DELETE** /data/assets/{asset_id} | Delete asset
[**get_all_assets_get_data_assets**](AssetsApi.md#get_all_assets_get_data_assets) | **GET** /data/assets | Get all assets
[**get_all_assets_get_data_assets_all**](AssetsApi.md#get_all_assets_get_data_assets_all) | **GET** /data/assets/all | Get all assets
[**get_asset_casting**](AssetsApi.md#get_asset_casting) | **GET** /data/assets/{asset_id}/casting | Get asset casting
[**get_asset_instances_get_data_assets_asset_id_asset_asset_instances**](AssetsApi.md#get_asset_instances_get_data_assets_asset_id_asset_asset_instances) | **GET** /data/assets/{asset_id}/asset-asset-instances | Get asset instances
[**get_asset_ok**](AssetsApi.md#get_asset_ok) | **GET** /data/assets/{asset_id} | Get asset ok
[**get_asset_task_types_get_data_assets_asset_id_task_types**](AssetsApi.md#get_asset_task_types_get_data_assets_asset_id_task_types) | **GET** /data/assets/{asset_id}/task-types | Get asset task types
[**get_asset_tasks_get_data_assets_asset_id_tasks**](AssetsApi.md#get_asset_tasks_get_data_assets_asset_id_tasks) | **GET** /data/assets/{asset_id}/tasks | Get asset tasks
[**get_asset_type**](AssetsApi.md#get_asset_type) | **GET** /data/asset-types/{asset_type_id} | Get asset type
[**get_asset_types**](AssetsApi.md#get_asset_types) | **GET** /data/asset-types | Get asset types
[**get_assets_with_tasks**](AssetsApi.md#get_assets_with_tasks) | **GET** /data/assets/with-tasks | Get assets with tasks
[**get_linked_assets**](AssetsApi.md#get_linked_assets) | **GET** /data/assets/{asset_id}/assets | Get linked assets
[**get_project_asset_type_assets**](AssetsApi.md#get_project_asset_type_assets) | **GET** /data/projects/{project_id}/asset-types/{asset_type_id}/assets | Get project asset type assets
[**get_project_asset_types_get_data_projects_project_id_asset_types**](AssetsApi.md#get_project_asset_types_get_data_projects_project_id_asset_types) | **GET** /data/projects/{project_id}/asset-types | Get project asset types
[**get_project_assets_get_data_projects_project_id_assets**](AssetsApi.md#get_project_assets_get_data_projects_project_id_assets) | **GET** /data/projects/{project_id}/assets | Get project assets
[**get_scene_asset_instances_get_data_assets_asset_id_scene_asset_instances**](AssetsApi.md#get_scene_asset_instances_get_data_assets_asset_id_scene_asset_instances) | **GET** /data/assets/{asset_id}/scene-asset-instances | Get scene asset instances
[**get_shared_assets_used_in_episode**](AssetsApi.md#get_shared_assets_used_in_episode) | **GET** /data/projects/{project_id}/episodes/{episode_id}/assets/shared-used | Get shared assets used in episode
[**get_shared_assets_used_in_project**](AssetsApi.md#get_shared_assets_used_in_project) | **GET** /data/projects/{project_id}/assets/shared-used | Get shared assets used in project
[**get_shot_asset_instances_get_data_assets_asset_id_shot_asset_instances**](AssetsApi.md#get_shot_asset_instances_get_data_assets_asset_id_shot_asset_instances) | **GET** /data/assets/{asset_id}/shot-asset-instances | Get shot asset instances
[**get_shot_asset_types**](AssetsApi.md#get_shot_asset_types) | **GET** /data/shots/{shot_id}/asset-types | Get shot asset types
[**get_shots_casting_asset**](AssetsApi.md#get_shots_casting_asset) | **GET** /data/assets/{asset_id}/cast-in | Get shots casting asset
[**set_asset_type_assets_shared**](AssetsApi.md#set_asset_type_assets_shared) | **POST** /actions/projects/{project_id}/asset-types/{asset_type_id}/assets/share | Set asset type assets shared
[**set_assets_shared**](AssetsApi.md#set_assets_shared) | **POST** /actions/assets/share | Set assets shared
[**set_project_assets_shared**](AssetsApi.md#set_project_assets_shared) | **POST** /actions/projects/{project_id}/assets/share | Set project assets shared
[**update_asset_casting**](AssetsApi.md#update_asset_casting) | **PUT** /data/assets/{asset_id}/casting | Update asset casting


# **create_asset**
> CreateAsset201Response create_asset(project_id, asset_type_id, create_asset_request)

Create asset

Create a new asset in a specific project with the given asset type and parameters.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_asset201_response import CreateAsset201Response
from sometech.pykitsu._client.models.create_asset_request import CreateAssetRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    asset_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset type
    create_asset_request = sometech.pykitsu._client.CreateAssetRequest() # CreateAssetRequest | 

    try:
        # Create asset
        api_response = await api_instance.create_asset(project_id, asset_type_id, create_asset_request)
        print("The response of AssetsApi->create_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->create_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **asset_type_id** | **UUID**| Unique identifier of the asset type | 
 **create_asset_request** | [**CreateAssetRequest**](CreateAssetRequest.md)|  | 

### Return type

[**CreateAsset201Response**](CreateAsset201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Asset successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_instance_post_data_assets_asset_id_asset_asset_instances**
> CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstances201Response create_asset_instance_post_data_assets_asset_id_asset_asset_instances(asset_id, create_asset_instance_post_data_assets_asset_id_asset_asset_instances_request)

Create asset instance

Create a new asset instance inside a specific asset by instantiating another asset.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_asset_instance_post_data_assets_asset_id_asset_asset_instances201_response import CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstances201Response
from sometech.pykitsu._client.models.create_asset_instance_post_data_assets_asset_id_asset_asset_instances_request import CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstancesRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    asset_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the parent asset
    create_asset_instance_post_data_assets_asset_id_asset_asset_instances_request = sometech.pykitsu._client.CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstancesRequest() # CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstancesRequest | 

    try:
        # Create asset instance
        api_response = await api_instance.create_asset_instance_post_data_assets_asset_id_asset_asset_instances(asset_id, create_asset_instance_post_data_assets_asset_id_asset_asset_instances_request)
        print("The response of AssetsApi->create_asset_instance_post_data_assets_asset_id_asset_asset_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->create_asset_instance_post_data_assets_asset_id_asset_asset_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**| Unique identifier of the parent asset | 
 **create_asset_instance_post_data_assets_asset_id_asset_asset_instances_request** | [**CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstancesRequest**](CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstancesRequest.md)|  | 

### Return type

[**CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstances201Response**](CreateAssetInstancePostDataAssetsAssetIdAssetAssetInstances201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Asset instance successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset**
> delete_asset(asset_id, force=force)

Delete asset

Permanently remove an asset from the system. Only asset creators or project managers can delete assets

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
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    asset_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset to delete
    force = false # bool | Force deletion bypassing validation checks (optional)

    try:
        # Delete asset
        await api_instance.delete_asset(asset_id, force=force)
    except Exception as e:
        print("Exception when calling AssetsApi->delete_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**| Unique identifier of the asset to delete | 
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
**204** | Asset successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_assets_get_data_assets**
> List[GetAllAssetsGetDataAssets200ResponseInner] get_all_assets_get_data_assets(project_id=project_id, asset_type_id=asset_type_id, page=page, limit=limit)

Get all assets

Retrieve all production assets with filtering and pagination. Supports advanced filtering by project, asset type, task status, and other criteria

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_all_assets_get_data_assets200_response_inner import GetAllAssetsGetDataAssets200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter assets by specific project (optional)
    asset_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter assets by asset type (optional)
    page = 1 # int | Page number for pagination (optional)
    limit = 100 # int | Number of assets per page (optional)

    try:
        # Get all assets
        api_response = await api_instance.get_all_assets_get_data_assets(project_id=project_id, asset_type_id=asset_type_id, page=page, limit=limit)
        print("The response of AssetsApi->get_all_assets_get_data_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_all_assets_get_data_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Filter assets by specific project | [optional] 
 **asset_type_id** | **UUID**| Filter assets by asset type | [optional] 
 **page** | **int**| Page number for pagination | [optional] 
 **limit** | **int**| Number of assets per page | [optional] 

### Return type

[**List[GetAllAssetsGetDataAssets200ResponseInner]**](GetAllAssetsGetDataAssets200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of assets successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_assets_get_data_assets_all**
> List[GetAllAssetsGetDataAssets200ResponseInner] get_all_assets_get_data_assets_all(project_id=project_id, asset_type_id=asset_type_id, page=page, limit=limit)

Get all assets

Retrieve all production assets with filtering and pagination. Supports advanced filtering by project, asset type, task status, and other criteria

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_all_assets_get_data_assets200_response_inner import GetAllAssetsGetDataAssets200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter assets by specific project (optional)
    asset_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter assets by asset type (optional)
    page = 1 # int | Page number for pagination (optional)
    limit = 100 # int | Number of assets per page (optional)

    try:
        # Get all assets
        api_response = await api_instance.get_all_assets_get_data_assets_all(project_id=project_id, asset_type_id=asset_type_id, page=page, limit=limit)
        print("The response of AssetsApi->get_all_assets_get_data_assets_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_all_assets_get_data_assets_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Filter assets by specific project | [optional] 
 **asset_type_id** | **UUID**| Filter assets by asset type | [optional] 
 **page** | **int**| Page number for pagination | [optional] 
 **limit** | **int**| Number of assets per page | [optional] 

### Return type

[**List[GetAllAssetsGetDataAssets200ResponseInner]**](GetAllAssetsGetDataAssets200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of assets successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_casting**
> GetAssetCasting200Response get_asset_casting(asset_id)

Get asset casting

Retrieve the casting information for a specific asset showing which shots or sequences use this asset

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_asset_casting200_response import GetAssetCasting200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    asset_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset

    try:
        # Get asset casting
        api_response = await api_instance.get_asset_casting(asset_id)
        print("The response of AssetsApi->get_asset_casting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_casting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**| Unique identifier of the asset | 

### Return type

[**GetAssetCasting200Response**](GetAssetCasting200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset casting information successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_instances_get_data_assets_asset_id_asset_asset_instances**
> List[GetAssetInstancesGetDataAssetsAssetIdAssetAssetInstances200ResponseInner] get_asset_instances_get_data_assets_asset_id_asset_asset_instances(asset_id)

Get asset instances

Retrieve all asset instances that are instantiated inside a specific asset.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_asset_instances_get_data_assets_asset_id_asset_asset_instances200_response_inner import GetAssetInstancesGetDataAssetsAssetIdAssetAssetInstances200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    asset_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset

    try:
        # Get asset instances
        api_response = await api_instance.get_asset_instances_get_data_assets_asset_id_asset_asset_instances(asset_id)
        print("The response of AssetsApi->get_asset_instances_get_data_assets_asset_id_asset_asset_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_instances_get_data_assets_asset_id_asset_asset_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**| Unique identifier of the asset | 

### Return type

[**List[GetAssetInstancesGetDataAssetsAssetIdAssetAssetInstances200ResponseInner]**](GetAssetInstancesGetDataAssetsAssetIdAssetAssetInstances200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of asset instances successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_ok**
> GetAssetOk200Response get_asset_ok(asset_id)

Get asset ok

Retrieve detailed information about a specific asset including metadata, project context, and related data

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_asset_ok200_response import GetAssetOk200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    asset_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset

    try:
        # Get asset ok
        api_response = await api_instance.get_asset_ok(asset_id)
        print("The response of AssetsApi->get_asset_ok:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_ok: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**| Unique identifier of the asset | 

### Return type

[**GetAssetOk200Response**](GetAssetOk200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset information successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_task_types_get_data_assets_asset_id_task_types**
> List[TaskType] get_asset_task_types_get_data_assets_asset_id_task_types(asset_id)

Get asset task types

Retrieve all task types that are used for tasks related to a specific asset.

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
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    asset_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset

    try:
        # Get asset task types
        api_response = await api_instance.get_asset_task_types_get_data_assets_asset_id_task_types(asset_id)
        print("The response of AssetsApi->get_asset_task_types_get_data_assets_asset_id_task_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_task_types_get_data_assets_asset_id_task_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**| Unique identifier of the asset | 

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
**200** | List of asset task types successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_tasks_get_data_assets_asset_id_tasks**
> List[GetAssetTasksGetDataAssetsAssetIdTasks200ResponseInner] get_asset_tasks_get_data_assets_asset_id_tasks(asset_id, task_type_id=task_type_id, task_status_id=task_status_id)

Get asset tasks

Retrieve all tasks related to a specific asset.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_asset_tasks_get_data_assets_asset_id_tasks200_response_inner import GetAssetTasksGetDataAssetsAssetIdTasks200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    asset_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset
    task_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter tasks by task type (optional)
    task_status_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter tasks by task status (optional)

    try:
        # Get asset tasks
        api_response = await api_instance.get_asset_tasks_get_data_assets_asset_id_tasks(asset_id, task_type_id=task_type_id, task_status_id=task_status_id)
        print("The response of AssetsApi->get_asset_tasks_get_data_assets_asset_id_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_tasks_get_data_assets_asset_id_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**| Unique identifier of the asset | 
 **task_type_id** | **UUID**| Filter tasks by task type | [optional] 
 **task_status_id** | **UUID**| Filter tasks by task status | [optional] 

### Return type

[**List[GetAssetTasksGetDataAssetsAssetIdTasks200ResponseInner]**](GetAssetTasksGetDataAssetsAssetIdTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of asset tasks successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_type**
> GetAssetTypes200ResponseInner get_asset_type(asset_type_id)

Get asset type

Retrieve detailed information about a specific asset type including metadata and configuration

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_asset_types200_response_inner import GetAssetTypes200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    asset_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset type

    try:
        # Get asset type
        api_response = await api_instance.get_asset_type(asset_type_id)
        print("The response of AssetsApi->get_asset_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | **UUID**| Unique identifier of the asset type | 

### Return type

[**GetAssetTypes200ResponseInner**](GetAssetTypes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Given asset type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_types**
> List[GetAssetTypes200ResponseInner] get_asset_types(project_id=project_id)

Get asset types

Retrieve all available asset types (entity types that are not shot, sequence, or episode) with filtering support

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_asset_types200_response_inner import GetAssetTypes200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter asset types by project (optional)

    try:
        # Get asset types
        api_response = await api_instance.get_asset_types(project_id=project_id)
        print("The response of AssetsApi->get_asset_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Filter asset types by project | [optional] 

### Return type

[**List[GetAssetTypes200ResponseInner]**](GetAssetTypes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of asset types successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_with_tasks**
> List[GetAssetsWithTasks200ResponseInner] get_assets_with_tasks(project_id=project_id, episode_id=episode_id, asset_type_id=asset_type_id)

Get assets with tasks

Retrieve all production assets with their related tasks. Includes project name, asset type name, and all associated tasks. Supports filtering by episode

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_assets_with_tasks200_response_inner import GetAssetsWithTasks200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter assets by specific project (optional)
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter assets by episode (returns assets not linked to episode and assets linked to given episode) (optional)
    asset_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter assets by asset type (optional)

    try:
        # Get assets with tasks
        api_response = await api_instance.get_assets_with_tasks(project_id=project_id, episode_id=episode_id, asset_type_id=asset_type_id)
        print("The response of AssetsApi->get_assets_with_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_assets_with_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Filter assets by specific project | [optional] 
 **episode_id** | **UUID**| Filter assets by episode (returns assets not linked to episode and assets linked to given episode) | [optional] 
 **asset_type_id** | **UUID**| Filter assets by asset type | [optional] 

### Return type

[**List[GetAssetsWithTasks200ResponseInner]**](GetAssetsWithTasks200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of assets with tasks successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_assets**
> List[Asset] get_linked_assets(asset_id)

Get linked assets

Retrieve all assets that are linked to a specific asset through casting relationships

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
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    asset_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset

    try:
        # Get linked assets
        api_response = await api_instance.get_linked_assets(asset_id)
        print("The response of AssetsApi->get_linked_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_linked_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**| Unique identifier of the asset | 

### Return type

[**List[Asset]**](Asset.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of linked assets successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_asset_type_assets**
> List[GetAllAssetsGetDataAssets200ResponseInner] get_project_asset_type_assets(project_id, asset_type_id, page=page, limit=limit)

Get project asset type assets

Retrieve all assets of a specific type within a project.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_all_assets_get_data_assets200_response_inner import GetAllAssetsGetDataAssets200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    asset_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset type
    page = 1 # int | Page number for pagination (optional)
    limit = 100 # int | Number of assets per page (optional)

    try:
        # Get project asset type assets
        api_response = await api_instance.get_project_asset_type_assets(project_id, asset_type_id, page=page, limit=limit)
        print("The response of AssetsApi->get_project_asset_type_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_project_asset_type_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **asset_type_id** | **UUID**| Unique identifier of the asset type | 
 **page** | **int**| Page number for pagination | [optional] 
 **limit** | **int**| Number of assets per page | [optional] 

### Return type

[**List[GetAllAssetsGetDataAssets200ResponseInner]**](GetAllAssetsGetDataAssets200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of project asset type assets successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_asset_types_get_data_projects_project_id_asset_types**
> List[GetProjectAssetTypesGetDataProjectsProjectIdAssetTypes200ResponseInner] get_project_asset_types_get_data_projects_project_id_asset_types(project_id)

Get project asset types

Retrieve all asset types available for a specific project

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_asset_types_get_data_projects_project_id_asset_types200_response_inner import GetProjectAssetTypesGetDataProjectsProjectIdAssetTypes200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project

    try:
        # Get project asset types
        api_response = await api_instance.get_project_asset_types_get_data_projects_project_id_asset_types(project_id)
        print("The response of AssetsApi->get_project_asset_types_get_data_projects_project_id_asset_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_project_asset_types_get_data_projects_project_id_asset_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 

### Return type

[**List[GetProjectAssetTypesGetDataProjectsProjectIdAssetTypes200ResponseInner]**](GetProjectAssetTypesGetDataProjectsProjectIdAssetTypes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of project asset types successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_assets_get_data_projects_project_id_assets**
> List[GetAllAssetsGetDataAssets200ResponseInner] get_project_assets_get_data_projects_project_id_assets(project_id, asset_type_id=asset_type_id, page=page, limit=limit)

Get project assets

Retrieve all assets belonging to a specific project with filtering support

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_all_assets_get_data_assets200_response_inner import GetAllAssetsGetDataAssets200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    asset_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Filter assets by asset type (optional)
    page = 1 # int | Page number for pagination (optional)
    limit = 100 # int | Number of assets per page (optional)

    try:
        # Get project assets
        api_response = await api_instance.get_project_assets_get_data_projects_project_id_assets(project_id, asset_type_id=asset_type_id, page=page, limit=limit)
        print("The response of AssetsApi->get_project_assets_get_data_projects_project_id_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_project_assets_get_data_projects_project_id_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **asset_type_id** | **UUID**| Filter assets by asset type | [optional] 
 **page** | **int**| Page number for pagination | [optional] 
 **limit** | **int**| Number of assets per page | [optional] 

### Return type

[**List[GetAllAssetsGetDataAssets200ResponseInner]**](GetAllAssetsGetDataAssets200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of project assets successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scene_asset_instances_get_data_assets_asset_id_scene_asset_instances**
> List[GetSceneAssetInstancesGetDataAssetsAssetIdSceneAssetInstances200ResponseInner] get_scene_asset_instances_get_data_assets_asset_id_scene_asset_instances(asset_id)

Get scene asset instances

Retrieve all scene asset instances that are linked to a specific asset.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_scene_asset_instances_get_data_assets_asset_id_scene_asset_instances200_response_inner import GetSceneAssetInstancesGetDataAssetsAssetIdSceneAssetInstances200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    asset_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset

    try:
        # Get scene asset instances
        api_response = await api_instance.get_scene_asset_instances_get_data_assets_asset_id_scene_asset_instances(asset_id)
        print("The response of AssetsApi->get_scene_asset_instances_get_data_assets_asset_id_scene_asset_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_scene_asset_instances_get_data_assets_asset_id_scene_asset_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**| Unique identifier of the asset | 

### Return type

[**List[GetSceneAssetInstancesGetDataAssetsAssetIdSceneAssetInstances200ResponseInner]**](GetSceneAssetInstancesGetDataAssetsAssetIdSceneAssetInstances200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of scene asset instances successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_assets_used_in_episode**
> List[GetSharedAssetsUsedInEpisode200ResponseInner] get_shared_assets_used_in_episode(project_id, episode_id)

Get shared assets used in episode

Retrieve all shared assets that are used in a specific project episode.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shared_assets_used_in_episode200_response_inner import GetSharedAssetsUsedInEpisode200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the episode

    try:
        # Get shared assets used in episode
        api_response = await api_instance.get_shared_assets_used_in_episode(project_id, episode_id)
        print("The response of AssetsApi->get_shared_assets_used_in_episode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_shared_assets_used_in_episode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **episode_id** | **UUID**| Unique identifier of the episode | 

### Return type

[**List[GetSharedAssetsUsedInEpisode200ResponseInner]**](GetSharedAssetsUsedInEpisode200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of shared assets used in episode successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_assets_used_in_project**
> List[Asset] get_shared_assets_used_in_project(project_id)

Get shared assets used in project

Retrieve all shared assets that are used in a specific project.

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
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project

    try:
        # Get shared assets used in project
        api_response = await api_instance.get_shared_assets_used_in_project(project_id)
        print("The response of AssetsApi->get_shared_assets_used_in_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_shared_assets_used_in_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 

### Return type

[**List[Asset]**](Asset.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of shared assets used in project successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_asset_instances_get_data_assets_asset_id_shot_asset_instances**
> List[GetShotAssetInstancesGetDataAssetsAssetIdShotAssetInstances200ResponseInner] get_shot_asset_instances_get_data_assets_asset_id_shot_asset_instances(asset_id)

Get shot asset instances

Retrieve all shot asset instances that are linked to a specific asset.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shot_asset_instances_get_data_assets_asset_id_shot_asset_instances200_response_inner import GetShotAssetInstancesGetDataAssetsAssetIdShotAssetInstances200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    asset_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset

    try:
        # Get shot asset instances
        api_response = await api_instance.get_shot_asset_instances_get_data_assets_asset_id_shot_asset_instances(asset_id)
        print("The response of AssetsApi->get_shot_asset_instances_get_data_assets_asset_id_shot_asset_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_shot_asset_instances_get_data_assets_asset_id_shot_asset_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**| Unique identifier of the asset | 

### Return type

[**List[GetShotAssetInstancesGetDataAssetsAssetIdShotAssetInstances200ResponseInner]**](GetShotAssetInstancesGetDataAssetsAssetIdShotAssetInstances200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of shot asset instances successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shot_asset_types**
> List[GetShotAssetTypes200ResponseInner] get_shot_asset_types(shot_id)

Get shot asset types

Retrieve all asset types of assets that are casted in a specific shot

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shot_asset_types200_response_inner import GetShotAssetTypes200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    shot_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the shot

    try:
        # Get shot asset types
        api_response = await api_instance.get_shot_asset_types(shot_id)
        print("The response of AssetsApi->get_shot_asset_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_shot_asset_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shot_id** | **UUID**| Unique identifier of the shot | 

### Return type

[**List[GetShotAssetTypes200ResponseInner]**](GetShotAssetTypes200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of shot asset types successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shots_casting_asset**
> List[GetShotsCastingAsset200ResponseInner] get_shots_casting_asset(asset_id)

Get shots casting asset

Retrieve all shots that cast a specific asset in their breakdown.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_shots_casting_asset200_response_inner import GetShotsCastingAsset200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    asset_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset

    try:
        # Get shots casting asset
        api_response = await api_instance.get_shots_casting_asset(asset_id)
        print("The response of AssetsApi->get_shots_casting_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_shots_casting_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**| Unique identifier of the asset | 

### Return type

[**List[GetShotsCastingAsset200ResponseInner]**](GetShotsCastingAsset200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of shots casting the asset successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_asset_type_assets_shared**
> SetAssetTypeAssetsShared200Response set_asset_type_assets_shared(project_id, asset_type_id, set_asset_type_assets_shared_request=set_asset_type_assets_shared_request)

Set asset type assets shared

Share or unshare all assets for a specific project and asset type.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.set_asset_type_assets_shared200_response import SetAssetTypeAssetsShared200Response
from sometech.pykitsu._client.models.set_asset_type_assets_shared_request import SetAssetTypeAssetsSharedRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    asset_type_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset type
    set_asset_type_assets_shared_request = sometech.pykitsu._client.SetAssetTypeAssetsSharedRequest() # SetAssetTypeAssetsSharedRequest |  (optional)

    try:
        # Set asset type assets shared
        api_response = await api_instance.set_asset_type_assets_shared(project_id, asset_type_id, set_asset_type_assets_shared_request=set_asset_type_assets_shared_request)
        print("The response of AssetsApi->set_asset_type_assets_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->set_asset_type_assets_shared: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **asset_type_id** | **UUID**| Unique identifier of the asset type | 
 **set_asset_type_assets_shared_request** | [**SetAssetTypeAssetsSharedRequest**](SetAssetTypeAssetsSharedRequest.md)|  | [optional] 

### Return type

[**SetAssetTypeAssetsShared200Response**](SetAssetTypeAssetsShared200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset type assets shared status successfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_assets_shared**
> SetAssetsShared200Response set_assets_shared(set_assets_shared_request)

Set assets shared

Share or unshare a specific list of assets by their IDs.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.set_assets_shared200_response import SetAssetsShared200Response
from sometech.pykitsu._client.models.set_assets_shared_request import SetAssetsSharedRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    set_assets_shared_request = sometech.pykitsu._client.SetAssetsSharedRequest() # SetAssetsSharedRequest | 

    try:
        # Set assets shared
        api_response = await api_instance.set_assets_shared(set_assets_shared_request)
        print("The response of AssetsApi->set_assets_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->set_assets_shared: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_assets_shared_request** | [**SetAssetsSharedRequest**](SetAssetsSharedRequest.md)|  | 

### Return type

[**SetAssetsShared200Response**](SetAssetsShared200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assets shared status successfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_assets_shared**
> SetProjectAssetsShared200Response set_project_assets_shared(project_id, set_project_assets_shared_request=set_project_assets_shared_request)

Set project assets shared

Share or unshare all assets for a specific project or a list of specific assets.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.set_project_assets_shared200_response import SetProjectAssetsShared200Response
from sometech.pykitsu._client.models.set_project_assets_shared_request import SetProjectAssetsSharedRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the project
    set_project_assets_shared_request = sometech.pykitsu._client.SetProjectAssetsSharedRequest() # SetProjectAssetsSharedRequest |  (optional)

    try:
        # Set project assets shared
        api_response = await api_instance.set_project_assets_shared(project_id, set_project_assets_shared_request=set_project_assets_shared_request)
        print("The response of AssetsApi->set_project_assets_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->set_project_assets_shared: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Unique identifier of the project | 
 **set_project_assets_shared_request** | [**SetProjectAssetsSharedRequest**](SetProjectAssetsSharedRequest.md)|  | [optional] 

### Return type

[**SetProjectAssetsShared200Response**](SetProjectAssetsShared200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Assets shared status successfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_casting**
> UpdateAssetCasting200Response update_asset_casting(asset_id, update_asset_casting_request)

Update asset casting

Modify the casting relationships for a specific asset by updating which shots or sequences use this asset.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.update_asset_casting200_response import UpdateAssetCasting200Response
from sometech.pykitsu._client.models.update_asset_casting_request import UpdateAssetCastingRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.AssetsApi(api_client)
    asset_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the asset
    update_asset_casting_request = sometech.pykitsu._client.UpdateAssetCastingRequest() # UpdateAssetCastingRequest | 

    try:
        # Update asset casting
        api_response = await api_instance.update_asset_casting(asset_id, update_asset_casting_request)
        print("The response of AssetsApi->update_asset_casting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->update_asset_casting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **UUID**| Unique identifier of the asset | 
 **update_asset_casting_request** | [**UpdateAssetCastingRequest**](UpdateAssetCastingRequest.md)|  | 

### Return type

[**UpdateAssetCasting200Response**](UpdateAssetCasting200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset casting successfully updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

