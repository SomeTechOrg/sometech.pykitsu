# sometech.pykitsu._client.PlaylistsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_entity_to_playlist**](PlaylistsApi.md#add_entity_to_playlist) | **POST** /actions/playlists/{playlist_id}/add-entity | Add entity to playlist
[**attach_files_to_a_guest_owned_comment**](PlaylistsApi.md#attach_files_to_a_guest_owned_comment) | **POST** /shared/playlists/{token}/comments/{comment_id}/attachments | Attach files to a guest-owned comment
[**build_playlist_movie**](PlaylistsApi.md#build_playlist_movie) | **GET** /data/playlists/{playlist_id}/build/mp4 | Build playlist movie
[**create_or_retrieve_guest_for_shared_playlist**](PlaylistsApi.md#create_or_retrieve_guest_for_shared_playlist) | **POST** /shared/playlists/{token}/guest | Create or retrieve guest for shared playlist
[**delete_an_attachment_from_a_guest_owned_comment**](PlaylistsApi.md#delete_an_attachment_from_a_guest_owned_comment) | **DELETE** /shared/playlists/{token}/comments/{comment_id}/attachments/{attachment_id} | Delete an attachment from a guest-owned comment
[**delete_build_job**](PlaylistsApi.md#delete_build_job) | **DELETE** /data/playlists/{playlist_id}/jobs/{build_job_id} | Delete build job
[**delete_guest_owned_comment**](PlaylistsApi.md#delete_guest_owned_comment) | **DELETE** /shared/playlists/{token}/comments/{comment_id} | Delete guest-owned comment
[**download_attachment_file_get_shared_playlists_token_attachment_files_attachment_id_file_file_name**](PlaylistsApi.md#download_attachment_file_get_shared_playlists_token_attachment_files_attachment_id_file_file_name) | **GET** /shared/playlists/{token}/attachment-files/{attachment_id}/file/{file_name} | Download attachment file
[**download_playlist_build**](PlaylistsApi.md#download_playlist_build) | **GET** /data/playlists/{playlist_id}/jobs/{build_job_id}/build/mp4 | Download playlist build
[**download_playlist_zip**](PlaylistsApi.md#download_playlist_zip) | **GET** /data/playlists/{playlist_id}/download/zip | Download playlist zip
[**edit_guest_owned_comment**](PlaylistsApi.md#edit_guest_owned_comment) | **PUT** /shared/playlists/{token}/comments/{comment_id} | Edit guest-owned comment
[**generate_temp_playlist**](PlaylistsApi.md#generate_temp_playlist) | **POST** /data/projects/{project_id}/playlists/temp | Generate temp playlist
[**get_all_project_playlists**](PlaylistsApi.md#get_all_project_playlists) | **GET** /data/projects/{project_id}/playlists/all | Get all project playlists
[**get_build_job**](PlaylistsApi.md#get_build_job) | **GET** /data/playlists/{playlist_id}/jobs/{build_job_id} | Get build job
[**get_entity_previews**](PlaylistsApi.md#get_entity_previews) | **GET** /data/playlists/entities/{entity_id}/preview-files | Get entity previews
[**get_episode_playlists**](PlaylistsApi.md#get_episode_playlists) | **GET** /data/projects/{project_id}/episodes/{episode_id}/playlists | Get episode playlists
[**get_playlist_get_data_projects_project_id_playlists_playlist_id**](PlaylistsApi.md#get_playlist_get_data_projects_project_id_playlists_playlist_id) | **GET** /data/projects/{project_id}/playlists/{playlist_id} | Get playlist
[**get_project_build_jobs**](PlaylistsApi.md#get_project_build_jobs) | **GET** /data/projects/{project_id}/build-jobs | Get project build jobs
[**get_project_playlists**](PlaylistsApi.md#get_project_playlists) | **GET** /data/projects/{project_id}/playlists | Get project playlists
[**get_shared_movie_tile_strip**](PlaylistsApi.md#get_shared_movie_tile_strip) | **GET** /shared/playlists/{token}/movies/tiles/preview-files/{preview_file_id}.png | Get shared movie tile strip
[**get_shared_original_movie_preview**](PlaylistsApi.md#get_shared_original_movie_preview) | **GET** /shared/playlists/{token}/movies/originals/preview-files/{preview_file_id}.mp4 | Get shared original movie preview
[**get_shared_original_picture_preview**](PlaylistsApi.md#get_shared_original_picture_preview) | **GET** /shared/playlists/{token}/pictures/originals/preview-files/{preview_file_id}.png | Get shared original picture preview
[**get_shared_playlist**](PlaylistsApi.md#get_shared_playlist) | **GET** /shared/playlists/{token} | Get shared playlist
[**get_shared_playlist_context**](PlaylistsApi.md#get_shared_playlist_context) | **GET** /shared/playlists/{token}/context | Get shared playlist context
[**get_shared_preview_file_metadata**](PlaylistsApi.md#get_shared_preview_file_metadata) | **GET** /shared/playlists/{token}/preview-files/{preview_file_id} | Get shared preview file metadata
[**get_shared_preview_thumbnail**](PlaylistsApi.md#get_shared_preview_thumbnail) | **GET** /shared/playlists/{token}/pictures/thumbnails/preview-files/{preview_file_id}.png | Get shared preview thumbnail
[**invite_reviewers_to_a_shared_playlist**](PlaylistsApi.md#invite_reviewers_to_a_shared_playlist) | **POST** /data/playlists/{playlist_id}/share/{token}/invite | Invite reviewers to a shared playlist
[**list_shared_playlist_comments**](PlaylistsApi.md#list_shared_playlist_comments) | **GET** /shared/playlists/{token}/comments | List shared playlist comments
[**notify_clients_playlist_ready**](PlaylistsApi.md#notify_clients_playlist_ready) | **POST** /data/playlists/{playlist_id}/notify-clients | Notify clients playlist ready
[**post_comment_on_shared_playlist**](PlaylistsApi.md#post_comment_on_shared_playlist) | **POST** /shared/playlists/{token}/comments | Post comment on shared playlist
[**update_guest_annotations_for_a_preview_file**](PlaylistsApi.md#update_guest_annotations_for_a_preview_file) | **PUT** /shared/playlists/{token}/annotations | Update guest annotations for a preview file


# **add_entity_to_playlist**
> object add_entity_to_playlist(playlist_id, add_entity_to_playlist_request)

Add entity to playlist

Atomically add a single entity to the given playlist.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_entity_to_playlist_request import AddEntityToPlaylistRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    playlist_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Playlist unique identifier
    add_entity_to_playlist_request = sometech.pykitsu._client.AddEntityToPlaylistRequest() # AddEntityToPlaylistRequest | 

    try:
        # Add entity to playlist
        api_response = await api_instance.add_entity_to_playlist(playlist_id, add_entity_to_playlist_request)
        print("The response of PlaylistsApi->add_entity_to_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->add_entity_to_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **UUID**| Playlist unique identifier | 
 **add_entity_to_playlist_request** | [**AddEntityToPlaylistRequest**](AddEntityToPlaylistRequest.md)|  | 

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
**200** | Updated playlist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_files_to_a_guest_owned_comment**
> attach_files_to_a_guest_owned_comment(token, comment_id)

Attach files to a guest-owned comment

Upload one or more files as attachments to a comment the same guest previously posted.

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | 
    comment_id = 'comment_id_example' # str | 

    try:
        # Attach files to a guest-owned comment
        await api_instance.attach_files_to_a_guest_owned_comment(token, comment_id)
    except Exception as e:
        print("Exception when calling PlaylistsApi->attach_files_to_a_guest_owned_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **comment_id** | **str**|  | 

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

# **build_playlist_movie**
> BuildPlaylistMovie200Response build_playlist_movie(playlist_id, full=full)

Build playlist movie

Build given playlist as MP4 movie. Starts a build job that processes the playlist shots into a video file.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.build_playlist_movie200_response import BuildPlaylistMovie200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    playlist_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Playlist unique identifier
    full = true # bool | Whether to build full quality movie (optional)

    try:
        # Build playlist movie
        api_response = await api_instance.build_playlist_movie(playlist_id, full=full)
        print("The response of PlaylistsApi->build_playlist_movie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->build_playlist_movie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **UUID**| Playlist unique identifier | 
 **full** | **bool**| Whether to build full quality movie | [optional] 

### Return type

[**BuildPlaylistMovie200Response**](BuildPlaylistMovie200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Build job created for playlist movie |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_retrieve_guest_for_shared_playlist**
> object create_or_retrieve_guest_for_shared_playlist(token, create_or_retrieve_guest_for_shared_playlist_request=create_or_retrieve_guest_for_shared_playlist_request)

Create or retrieve guest for shared playlist

Create a guest identity for the shared playlist, or return an existing guest when `guest_id` is provided and still valid.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_or_retrieve_guest_for_shared_playlist_request import CreateOrRetrieveGuestForSharedPlaylistRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | Share link token
    create_or_retrieve_guest_for_shared_playlist_request = sometech.pykitsu._client.CreateOrRetrieveGuestForSharedPlaylistRequest() # CreateOrRetrieveGuestForSharedPlaylistRequest |  (optional)

    try:
        # Create or retrieve guest for shared playlist
        api_response = await api_instance.create_or_retrieve_guest_for_shared_playlist(token, create_or_retrieve_guest_for_shared_playlist_request=create_or_retrieve_guest_for_shared_playlist_request)
        print("The response of PlaylistsApi->create_or_retrieve_guest_for_shared_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->create_or_retrieve_guest_for_shared_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Share link token | 
 **create_or_retrieve_guest_for_shared_playlist_request** | [**CreateOrRetrieveGuestForSharedPlaylistRequest**](CreateOrRetrieveGuestForSharedPlaylistRequest.md)|  | [optional] 

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
**200** | Existing guest returned |  -  |
**201** | New guest created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_an_attachment_from_a_guest_owned_comment**
> delete_an_attachment_from_a_guest_owned_comment(token, comment_id, attachment_id)

Delete an attachment from a guest-owned comment

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | 
    comment_id = 'comment_id_example' # str | 
    attachment_id = 'attachment_id_example' # str | 

    try:
        # Delete an attachment from a guest-owned comment
        await api_instance.delete_an_attachment_from_a_guest_owned_comment(token, comment_id, attachment_id)
    except Exception as e:
        print("Exception when calling PlaylistsApi->delete_an_attachment_from_a_guest_owned_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **comment_id** | **str**|  | 
 **attachment_id** | **str**|  | 

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

# **delete_build_job**
> delete_build_job(playlist_id, build_job_id)

Delete build job

Remove given build job related to given playlist.

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    playlist_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Playlist unique identifier
    build_job_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Build job unique identifier

    try:
        # Delete build job
        await api_instance.delete_build_job(playlist_id, build_job_id)
    except Exception as e:
        print("Exception when calling PlaylistsApi->delete_build_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **UUID**| Playlist unique identifier | 
 **build_job_id** | **UUID**| Build job unique identifier | 

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
**204** | Build job removed successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guest_owned_comment**
> delete_guest_owned_comment(token, comment_id)

Delete guest-owned comment

Delete a comment previously posted by the same guest.

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | 
    comment_id = 'comment_id_example' # str | 

    try:
        # Delete guest-owned comment
        await api_instance.delete_guest_owned_comment(token, comment_id)
    except Exception as e:
        print("Exception when calling PlaylistsApi->delete_guest_owned_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **comment_id** | **str**|  | 

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

# **download_attachment_file_get_shared_playlists_token_attachment_files_attachment_id_file_file_name**
> download_attachment_file_get_shared_playlists_token_attachment_files_attachment_id_file_file_name(token, attachment_id, file_name)

Download attachment file

Serve an attachment file linked to a comment visible in this shared playlist (either `for_client=True` or authored by a guest).

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | 
    attachment_id = 'attachment_id_example' # str | 
    file_name = 'file_name_example' # str | 

    try:
        # Download attachment file
        await api_instance.download_attachment_file_get_shared_playlists_token_attachment_files_attachment_id_file_file_name(token, attachment_id, file_name)
    except Exception as e:
        print("Exception when calling PlaylistsApi->download_attachment_file_get_shared_playlists_token_attachment_files_attachment_id_file_file_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **attachment_id** | **str**|  | 
 **file_name** | **str**|  | 

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

# **download_playlist_build**
> bytes download_playlist_build(playlist_id, build_job_id)

Download playlist build

Download given playlist build as MP4 file.

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    playlist_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Playlist unique identifier
    build_job_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Build job unique identifier

    try:
        # Download playlist build
        api_response = await api_instance.download_playlist_build(playlist_id, build_job_id)
        print("The response of PlaylistsApi->download_playlist_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->download_playlist_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **UUID**| Playlist unique identifier | 
 **build_job_id** | **UUID**| Build job unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/mp4, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Playlist build downloaded as MP4 file |  -  |
**400** | Build not finished, need to retry later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_playlist_zip**
> bytes download_playlist_zip(playlist_id)

Download playlist zip

Download given playlist as ZIP file containing all preview files.

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    playlist_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Playlist unique identifier

    try:
        # Download playlist zip
        api_response = await api_instance.download_playlist_zip(playlist_id)
        print("The response of PlaylistsApi->download_playlist_zip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->download_playlist_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **UUID**| Playlist unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Playlist downloaded as ZIP file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_guest_owned_comment**
> edit_guest_owned_comment(token, comment_id)

Edit guest-owned comment

Update the text / checklist / task status of a comment previously posted by the same guest.

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | 
    comment_id = 'comment_id_example' # str | 

    try:
        # Edit guest-owned comment
        await api_instance.edit_guest_owned_comment(token, comment_id)
    except Exception as e:
        print("Exception when calling PlaylistsApi->edit_guest_owned_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **comment_id** | **str**|  | 

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

# **generate_temp_playlist**
> List[GetEntityPreviews200ResponseValueInner] generate_temp_playlist(project_id, generate_temp_playlist_request, sort=sort)

Generate temp playlist

Generate a temporary playlist from task IDs. It's mainly used for synchronisation purpose.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.generate_temp_playlist_request import GenerateTempPlaylistRequest
from sometech.pykitsu._client.models.get_entity_previews200_response_value_inner import GetEntityPreviews200ResponseValueInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    generate_temp_playlist_request = sometech.pykitsu._client.GenerateTempPlaylistRequest() # GenerateTempPlaylistRequest | 
    sort = true # bool | Whether to sort the playlist (optional)

    try:
        # Generate temp playlist
        api_response = await api_instance.generate_temp_playlist(project_id, generate_temp_playlist_request, sort=sort)
        print("The response of PlaylistsApi->generate_temp_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->generate_temp_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **generate_temp_playlist_request** | [**GenerateTempPlaylistRequest**](GenerateTempPlaylistRequest.md)|  | 
 **sort** | **bool**| Whether to sort the playlist | [optional] 

### Return type

[**List[GetEntityPreviews200ResponseValueInner]**](GetEntityPreviews200ResponseValueInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Temporary playlist generated |  -  |
**400** | Invalid task IDs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_project_playlists**
> List[GetProjectPlaylists200ResponseInner] get_all_project_playlists(project_id)

Get all project playlists

Retrieve all playlists related to given project. It's mainly used for synchronisation purpose.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_playlists200_response_inner import GetProjectPlaylists200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get all project playlists
        api_response = await api_instance.get_all_project_playlists(project_id)
        print("The response of PlaylistsApi->get_all_project_playlists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_all_project_playlists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

[**List[GetProjectPlaylists200ResponseInner]**](GetProjectPlaylists200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All playlists related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_job**
> GetBuildJob200Response get_build_job(playlist_id, build_job_id)

Get build job

Retrieve build job related to given playlist.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_build_job200_response import GetBuildJob200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    playlist_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Playlist unique identifier
    build_job_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Build job unique identifier

    try:
        # Get build job
        api_response = await api_instance.get_build_job(playlist_id, build_job_id)
        print("The response of PlaylistsApi->get_build_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_build_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **UUID**| Playlist unique identifier | 
 **build_job_id** | **UUID**| Build job unique identifier | 

### Return type

[**GetBuildJob200Response**](GetBuildJob200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Build job related to given playlist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_previews**
> Dict[str, List[GetEntityPreviews200ResponseValueInner]] get_entity_previews(entity_id)

Get entity previews

Retrieve all previews related to a given entity. It sends them as a dict. Keys are related task type ids and values are arrays of preview for this task type.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_entity_previews200_response_value_inner import GetEntityPreviews200ResponseValueInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Entity unique identifier

    try:
        # Get entity previews
        api_response = await api_instance.get_entity_previews(entity_id)
        print("The response of PlaylistsApi->get_entity_previews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_entity_previews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| Entity unique identifier | 

### Return type

**Dict[str, List[GetEntityPreviews200ResponseValueInner]]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All previews related to given entity grouped by task type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_episode_playlists**
> List[GetEpisodePlaylists200ResponseInner] get_episode_playlists(project_id, episode_id)

Get episode playlists

Retrieve all playlists related to given episode. The full list is returned because the number of playlists in an episode is not that big.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_episode_playlists200_response_inner import GetEpisodePlaylists200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    episode_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Episode unique identifier or special value (main, all)

    try:
        # Get episode playlists
        api_response = await api_instance.get_episode_playlists(project_id, episode_id)
        print("The response of PlaylistsApi->get_episode_playlists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_episode_playlists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **episode_id** | **UUID**| Episode unique identifier or special value (main, all) | 

### Return type

[**List[GetEpisodePlaylists200ResponseInner]**](GetEpisodePlaylists200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All playlists related to given episode |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlist_get_data_projects_project_id_playlists_playlist_id**
> GetPlaylistGetDataProjectsProjectIdPlaylistsPlaylistId200Response get_playlist_get_data_projects_project_id_playlists_playlist_id(project_id, playlist_id)

Get playlist

Retrieve a specific playlist by ID with preview file revisions.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_playlist_get_data_projects_project_id_playlists_playlist_id200_response import GetPlaylistGetDataProjectsProjectIdPlaylistsPlaylistId200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    playlist_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Playlist unique identifier

    try:
        # Get playlist
        api_response = await api_instance.get_playlist_get_data_projects_project_id_playlists_playlist_id(project_id, playlist_id)
        print("The response of PlaylistsApi->get_playlist_get_data_projects_project_id_playlists_playlist_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_playlist_get_data_projects_project_id_playlists_playlist_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **playlist_id** | **UUID**| Playlist unique identifier | 

### Return type

[**GetPlaylistGetDataProjectsProjectIdPlaylistsPlaylistId200Response**](GetPlaylistGetDataProjectsProjectIdPlaylistsPlaylistId200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Playlist details with preview file revisions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_build_jobs**
> List[GetBuildJob200Response] get_project_build_jobs(project_id)

Get project build jobs

Retrieve all build jobs related to given project. It's mainly used for synchronisation purpose.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_build_job200_response import GetBuildJob200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier

    try:
        # Get project build jobs
        api_response = await api_instance.get_project_build_jobs(project_id)
        print("The response of PlaylistsApi->get_project_build_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_project_build_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 

### Return type

[**List[GetBuildJob200Response]**](GetBuildJob200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All build jobs related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_playlists**
> List[GetProjectPlaylists200ResponseInner] get_project_playlists(project_id, page=page, sort_by=sort_by, task_type_id=task_type_id)

Get project playlists

Retrieve all playlists related to given project. Result is paginated and can be sorted.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_project_playlists200_response_inner import GetProjectPlaylists200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    project_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Project unique identifier
    page = 1 # int | Page number for pagination (optional)
    sort_by = 'updated_at' # str | Field to sort by (optional)
    task_type_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Task type unique identifier to filter by (optional)

    try:
        # Get project playlists
        api_response = await api_instance.get_project_playlists(project_id, page=page, sort_by=sort_by, task_type_id=task_type_id)
        print("The response of PlaylistsApi->get_project_playlists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_project_playlists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **UUID**| Project unique identifier | 
 **page** | **int**| Page number for pagination | [optional] 
 **sort_by** | **str**| Field to sort by | [optional] 
 **task_type_id** | **UUID**| Task type unique identifier to filter by | [optional] 

### Return type

[**List[GetProjectPlaylists200ResponseInner]**](GetProjectPlaylists200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All playlists related to given project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_movie_tile_strip**
> bytes get_shared_movie_tile_strip(token, preview_file_id)

Get shared movie tile strip

Serve the filmstrip/tile image used for timeline hover previews, when the share token is valid.

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | Share link token
    preview_file_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Preview file unique identifier

    try:
        # Get shared movie tile strip
        api_response = await api_instance.get_shared_movie_tile_strip(token, preview_file_id)
        print("The response of PlaylistsApi->get_shared_movie_tile_strip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_shared_movie_tile_strip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Share link token | 
 **preview_file_id** | **UUID**| Preview file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tile sprite image |  -  |
**403** | Preview file is not part of this shared playlist |  -  |
**404** | Tile file missing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_original_movie_preview**
> bytes get_shared_original_movie_preview(token, preview_file_id)

Get shared original movie preview

Stream the original movie file for a preview, authorized by the share token. Same role as the authenticated original movie preview route, without JWT.

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | Share link token
    preview_file_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Preview file unique identifier

    try:
        # Get shared original movie preview
        api_response = await api_instance.get_shared_original_movie_preview(token, preview_file_id)
        print("The response of PlaylistsApi->get_shared_original_movie_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_shared_original_movie_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Share link token | 
 **preview_file_id** | **UUID**| Preview file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/mp4, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Movie preview file stream |  -  |
**403** | Preview file is not part of this shared playlist |  -  |
**404** | Preview file not on disk |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_original_picture_preview**
> bytes get_shared_original_picture_preview(token, preview_file_id)

Get shared original picture preview

Serve the full-size PNG for a still preview, authorized by the share token.

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | Share link token
    preview_file_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Preview file unique identifier

    try:
        # Get shared original picture preview
        api_response = await api_instance.get_shared_original_picture_preview(token, preview_file_id)
        print("The response of PlaylistsApi->get_shared_original_picture_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_shared_original_picture_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Share link token | 
 **preview_file_id** | **UUID**| Preview file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Original picture file |  -  |
**403** | Preview file is not part of this shared playlist |  -  |
**404** | Original file missing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_playlist**
> object get_shared_playlist(token, password=password)

Get shared playlist

Retrieve a playlist with preview file revisions for a secret share link. No JWT; the path token (and optional query password) is the credential.

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | Share link token
    password = 'password_example' # str | Password when the link is protected (optional)

    try:
        # Get shared playlist
        api_response = await api_instance.get_shared_playlist(token, password=password)
        print("The response of PlaylistsApi->get_shared_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_shared_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Share link token | 
 **password** | **str**| Password when the link is protected | [optional] 

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
**200** | Playlist with preview file revisions and enriched shots |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_playlist_context**
> object get_shared_playlist_context(token, password=password)

Get shared playlist context

Return minimal project and playlist context needed to render the shared playlist UI. Optional `password` query param when the link is protected.

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | Share link token
    password = 'password_example' # str | Password when the link is protected (optional)

    try:
        # Get shared playlist context
        api_response = await api_instance.get_shared_playlist_context(token, password=password)
        print("The response of PlaylistsApi->get_shared_playlist_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_shared_playlist_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Share link token | 
 **password** | **str**| Password when the link is protected | [optional] 

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
**200** | Context payload for the share page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_preview_file_metadata**
> object get_shared_preview_file_metadata(token, preview_file_id)

Get shared preview file metadata

Return preview file record when the request includes a valid share token. No JWT.

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | Share link token
    preview_file_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Preview file unique identifier

    try:
        # Get shared preview file metadata
        api_response = await api_instance.get_shared_preview_file_metadata(token, preview_file_id)
        print("The response of PlaylistsApi->get_shared_preview_file_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_shared_preview_file_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Share link token | 
 **preview_file_id** | **UUID**| Preview file unique identifier | 

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
**200** | Preview file metadata |  -  |
**403** | Preview file is not part of this shared playlist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_preview_thumbnail**
> bytes get_shared_preview_thumbnail(token, preview_file_id)

Get shared preview thumbnail

Serve the PNG thumbnail for a preview file when the share token is valid.

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | Share link token
    preview_file_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Preview file unique identifier

    try:
        # Get shared preview thumbnail
        api_response = await api_instance.get_shared_preview_thumbnail(token, preview_file_id)
        print("The response of PlaylistsApi->get_shared_preview_thumbnail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->get_shared_preview_thumbnail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Share link token | 
 **preview_file_id** | **UUID**| Preview file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thumbnail image |  -  |
**403** | Preview file is not part of this shared playlist |  -  |
**404** | Thumbnail file missing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_reviewers_to_a_shared_playlist**
> InviteReviewersToASharedPlaylist200Response invite_reviewers_to_a_shared_playlist(playlist_id, token, invite_reviewers_to_a_shared_playlist_request)

Invite reviewers to a shared playlist

Send the share URL by email to a list of recipients (raw emails and/or existing person ids).

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.invite_reviewers_to_a_shared_playlist200_response import InviteReviewersToASharedPlaylist200Response
from sometech.pykitsu._client.models.invite_reviewers_to_a_shared_playlist_request import InviteReviewersToASharedPlaylistRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    playlist_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    token = 'token_example' # str | 
    invite_reviewers_to_a_shared_playlist_request = sometech.pykitsu._client.InviteReviewersToASharedPlaylistRequest() # InviteReviewersToASharedPlaylistRequest | 

    try:
        # Invite reviewers to a shared playlist
        api_response = await api_instance.invite_reviewers_to_a_shared_playlist(playlist_id, token, invite_reviewers_to_a_shared_playlist_request)
        print("The response of PlaylistsApi->invite_reviewers_to_a_shared_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->invite_reviewers_to_a_shared_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **UUID**|  | 
 **token** | **str**|  | 
 **invite_reviewers_to_a_shared_playlist_request** | [**InviteReviewersToASharedPlaylistRequest**](InviteReviewersToASharedPlaylistRequest.md)|  | 

### Return type

[**InviteReviewersToASharedPlaylist200Response**](InviteReviewersToASharedPlaylist200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invitations dispatched |  -  |
**400** | One of the supplied emails is invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shared_playlist_comments**
> List[object] list_shared_playlist_comments(token, password=password)

List shared playlist comments

List comments for tasks that appear in the shared playlist (aggregated from each shot's preview task). Same optional `password` query param as the main shared playlist when the link is protected.

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
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | Share link token
    password = 'password_example' # str | Password when the link is protected (optional)

    try:
        # List shared playlist comments
        api_response = await api_instance.list_shared_playlist_comments(token, password=password)
        print("The response of PlaylistsApi->list_shared_playlist_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->list_shared_playlist_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Share link token | 
 **password** | **str**| Password when the link is protected | [optional] 

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
**200** | Comment entries for the playlist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_clients_playlist_ready**
> NotifyClientsPlaylistReady200Response notify_clients_playlist_ready(playlist_id, notify_clients_playlist_ready_request=notify_clients_playlist_ready_request)

Notify clients playlist ready

Notify clients that given playlist is ready for review.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.notify_clients_playlist_ready200_response import NotifyClientsPlaylistReady200Response
from sometech.pykitsu._client.models.notify_clients_playlist_ready_request import NotifyClientsPlaylistReadyRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    playlist_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Playlist unique identifier
    notify_clients_playlist_ready_request = sometech.pykitsu._client.NotifyClientsPlaylistReadyRequest() # NotifyClientsPlaylistReadyRequest |  (optional)

    try:
        # Notify clients playlist ready
        api_response = await api_instance.notify_clients_playlist_ready(playlist_id, notify_clients_playlist_ready_request=notify_clients_playlist_ready_request)
        print("The response of PlaylistsApi->notify_clients_playlist_ready:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->notify_clients_playlist_ready: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **UUID**| Playlist unique identifier | 
 **notify_clients_playlist_ready_request** | [**NotifyClientsPlaylistReadyRequest**](NotifyClientsPlaylistReadyRequest.md)|  | [optional] 

### Return type

[**NotifyClientsPlaylistReady200Response**](NotifyClientsPlaylistReady200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Clients notified successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_comment_on_shared_playlist**
> object post_comment_on_shared_playlist(token, post_comment_on_shared_playlist_request, password=password)

Post comment on shared playlist

Add a review comment as a guest. Requires `guest_id`, `task_id`, `task_status_id` and `text` when the link allows commenting. Optional `password` query param if the link is protected.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.post_comment_on_shared_playlist_request import PostCommentOnSharedPlaylistRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | Share link token
    post_comment_on_shared_playlist_request = sometech.pykitsu._client.PostCommentOnSharedPlaylistRequest() # PostCommentOnSharedPlaylistRequest | 
    password = 'password_example' # str | Password when the link is protected (optional)

    try:
        # Post comment on shared playlist
        api_response = await api_instance.post_comment_on_shared_playlist(token, post_comment_on_shared_playlist_request, password=password)
        print("The response of PlaylistsApi->post_comment_on_shared_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->post_comment_on_shared_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Share link token | 
 **post_comment_on_shared_playlist_request** | [**PostCommentOnSharedPlaylistRequest**](PostCommentOnSharedPlaylistRequest.md)|  | 
 **password** | **str**| Password when the link is protected | [optional] 

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
**201** | Comment created |  -  |
**400** | Missing required body fields, unknown task status, or task status not allowed for guest reviewers |  -  |
**403** | Comments disabled for this share link, or the task is not part of this shared playlist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_guest_annotations_for_a_preview_file**
> object update_guest_annotations_for_a_preview_file(token, update_guest_annotations_for_a_preview_file_request)

Update guest annotations for a preview file

Update preview file annotations in the context of a shared playlist. Reuses the same additions/updates/deletions diff format as the manager-facing /actions/preview-files/<id>/update-annotations route, so concurrent edits stay safe via the Redis lock.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.update_guest_annotations_for_a_preview_file_request import UpdateGuestAnnotationsForAPreviewFileRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PlaylistsApi(api_client)
    token = 'token_example' # str | Share link token
    update_guest_annotations_for_a_preview_file_request = sometech.pykitsu._client.UpdateGuestAnnotationsForAPreviewFileRequest() # UpdateGuestAnnotationsForAPreviewFileRequest | 

    try:
        # Update guest annotations for a preview file
        api_response = await api_instance.update_guest_annotations_for_a_preview_file(token, update_guest_annotations_for_a_preview_file_request)
        print("The response of PlaylistsApi->update_guest_annotations_for_a_preview_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaylistsApi->update_guest_annotations_for_a_preview_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Share link token | 
 **update_guest_annotations_for_a_preview_file_request** | [**UpdateGuestAnnotationsForAPreviewFileRequest**](UpdateGuestAnnotationsForAPreviewFileRequest.md)|  | 

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
**200** | Updated preview file with the new annotations |  -  |
**400** | Missing required body fields |  -  |
**403** | Annotations disabled for this share link, or the preview file is not part of the shared playlist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

