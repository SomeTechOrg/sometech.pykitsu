# sometech.pykitsu._client.PreviewsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_preview_background_file_post_pictures_preview_background_files_instance_id**](PreviewsApi.md#create_preview_background_file_post_pictures_preview_background_files_instance_id) | **POST** /pictures/preview-background-files/{instance_id} | Create preview background file
[**create_preview_file_post_pictures_preview_files_instance_id**](PreviewsApi.md#create_preview_file_post_pictures_preview_files_instance_id) | **POST** /pictures/preview-files/{instance_id} | Create preview file
[**create_thumbnail_post_pictures_thumbnails_organisations_instance_id**](PreviewsApi.md#create_thumbnail_post_pictures_thumbnails_organisations_instance_id) | **POST** /pictures/thumbnails/organisations/{instance_id} | Create thumbnail
[**create_thumbnail_post_pictures_thumbnails_organisations_instance_id_png**](PreviewsApi.md#create_thumbnail_post_pictures_thumbnails_organisations_instance_id_png) | **POST** /pictures/thumbnails/organisations/{instance_id}.png | Create thumbnail
[**create_thumbnail_post_pictures_thumbnails_persons_instance_id**](PreviewsApi.md#create_thumbnail_post_pictures_thumbnails_persons_instance_id) | **POST** /pictures/thumbnails/persons/{instance_id} | Create thumbnail
[**create_thumbnail_post_pictures_thumbnails_persons_instance_id_png**](PreviewsApi.md#create_thumbnail_post_pictures_thumbnails_persons_instance_id_png) | **POST** /pictures/thumbnails/persons/{instance_id}.png | Create thumbnail
[**create_thumbnail_post_pictures_thumbnails_preview_background_files_instance_id_png**](PreviewsApi.md#create_thumbnail_post_pictures_thumbnails_preview_background_files_instance_id_png) | **POST** /pictures/thumbnails/preview-background-files/{instance_id}.png | Create thumbnail
[**create_thumbnail_post_pictures_thumbnails_projects_instance_id**](PreviewsApi.md#create_thumbnail_post_pictures_thumbnails_projects_instance_id) | **POST** /pictures/thumbnails/projects/{instance_id} | Create thumbnail
[**create_thumbnail_post_pictures_thumbnails_projects_instance_id_png**](PreviewsApi.md#create_thumbnail_post_pictures_thumbnails_projects_instance_id_png) | **POST** /pictures/thumbnails/projects/{instance_id}.png | Create thumbnail
[**download_preview_file**](PreviewsApi.md#download_preview_file) | **GET** /pictures/originals/preview-files/{instance_id}/download | Download preview file
[**download_preview_movie**](PreviewsApi.md#download_preview_movie) | **GET** /movies/originals/preview-files/{instance_id}/download | Download preview movie
[**extract_frame_from_preview**](PreviewsApi.md#extract_frame_from_preview) | **GET** /actions/preview-files/{preview_file_id}/extract-frame | Extract frame from preview
[**extract_tile_from_preview**](PreviewsApi.md#extract_tile_from_preview) | **GET** /actions/preview-files/{preview_file_id}/extract-tile | Extract tile from preview
[**get_attachment_thumbnail**](PreviewsApi.md#get_attachment_thumbnail) | **GET** /pictures/thumbnails/attachment-files/{attachment_file_id}.png | Get attachment thumbnail
[**get_preview_background_file_get_pictures_preview_background_files_instance_id_extension**](PreviewsApi.md#get_preview_background_file_get_pictures_preview_background_files_instance_id_extension) | **GET** /pictures/preview-background-files/{instance_id}.{extension} | Get preview background file
[**get_preview_file_get_pictures_originals_preview_files_instance_id_extension**](PreviewsApi.md#get_preview_file_get_pictures_originals_preview_files_instance_id_extension) | **GET** /pictures/originals/preview-files/{instance_id}.{extension} | Get preview file
[**get_preview_lowdef_movie**](PreviewsApi.md#get_preview_lowdef_movie) | **GET** /movies/low/preview-files/{instance_id}.mp4 | Get preview lowdef movie
[**get_preview_movie**](PreviewsApi.md#get_preview_movie) | **GET** /movies/originals/preview-files/{instance_id}.mp4 | Get preview movie
[**get_preview_thumbnail_get_movies_tiles_preview_files_instance_id_png**](PreviewsApi.md#get_preview_thumbnail_get_movies_tiles_preview_files_instance_id_png) | **GET** /movies/tiles/preview-files/{instance_id}.png | Get preview thumbnail
[**get_preview_thumbnail_get_pictures_originals_preview_files_instance_id_png**](PreviewsApi.md#get_preview_thumbnail_get_pictures_originals_preview_files_instance_id_png) | **GET** /pictures/originals/preview-files/{instance_id}.png | Get preview thumbnail
[**get_preview_thumbnail_get_pictures_previews_preview_files_instance_id_png**](PreviewsApi.md#get_preview_thumbnail_get_pictures_previews_preview_files_instance_id_png) | **GET** /pictures/previews/preview-files/{instance_id}.png | Get preview thumbnail
[**get_preview_thumbnail_get_pictures_thumbnails_preview_files_instance_id_png**](PreviewsApi.md#get_preview_thumbnail_get_pictures_thumbnails_preview_files_instance_id_png) | **GET** /pictures/thumbnails/preview-files/{instance_id}.png | Get preview thumbnail
[**get_preview_thumbnail_get_pictures_thumbnails_square_preview_files_instance_id_png**](PreviewsApi.md#get_preview_thumbnail_get_pictures_thumbnails_square_preview_files_instance_id_png) | **GET** /pictures/thumbnails-square/preview-files/{instance_id}.png | Get preview thumbnail
[**get_running_preview_files**](PreviewsApi.md#get_running_preview_files) | **GET** /data/playlists/preview-files/running | Get running preview files
[**get_thumbnail_get_pictures_thumbnails_organisations_instance_id**](PreviewsApi.md#get_thumbnail_get_pictures_thumbnails_organisations_instance_id) | **GET** /pictures/thumbnails/organisations/{instance_id} | Get thumbnail
[**get_thumbnail_get_pictures_thumbnails_organisations_instance_id_png**](PreviewsApi.md#get_thumbnail_get_pictures_thumbnails_organisations_instance_id_png) | **GET** /pictures/thumbnails/organisations/{instance_id}.png | Get thumbnail
[**get_thumbnail_get_pictures_thumbnails_persons_instance_id**](PreviewsApi.md#get_thumbnail_get_pictures_thumbnails_persons_instance_id) | **GET** /pictures/thumbnails/persons/{instance_id} | Get thumbnail
[**get_thumbnail_get_pictures_thumbnails_persons_instance_id_png**](PreviewsApi.md#get_thumbnail_get_pictures_thumbnails_persons_instance_id_png) | **GET** /pictures/thumbnails/persons/{instance_id}.png | Get thumbnail
[**get_thumbnail_get_pictures_thumbnails_preview_background_files_instance_id_png**](PreviewsApi.md#get_thumbnail_get_pictures_thumbnails_preview_background_files_instance_id_png) | **GET** /pictures/thumbnails/preview-background-files/{instance_id}.png | Get thumbnail
[**get_thumbnail_get_pictures_thumbnails_projects_instance_id**](PreviewsApi.md#get_thumbnail_get_pictures_thumbnails_projects_instance_id) | **GET** /pictures/thumbnails/projects/{instance_id} | Get thumbnail
[**get_thumbnail_get_pictures_thumbnails_projects_instance_id_png**](PreviewsApi.md#get_thumbnail_get_pictures_thumbnails_projects_instance_id_png) | **GET** /pictures/thumbnails/projects/{instance_id}.png | Get thumbnail
[**set_main_preview**](PreviewsApi.md#set_main_preview) | **PUT** /actions/preview-files/{preview_file_id}/set-main-preview | Set main preview
[**update_preview_annotations**](PreviewsApi.md#update_preview_annotations) | **PUT** /actions/preview-files/{preview_file_id}/update-annotations | Update preview annotations
[**update_preview_position**](PreviewsApi.md#update_preview_position) | **PUT** /actions/preview-files/{preview_file_id}/update-position | Update preview position


# **create_preview_background_file_post_pictures_preview_background_files_instance_id**
> CreatePreviewBackgroundFilePostPicturesPreviewBackgroundFilesInstanceId201Response create_preview_background_file_post_pictures_preview_background_files_instance_id(instance_id, file)

Create preview background file

Main resource to add a preview background file. It stores the preview background file and generates a rectangle thumbnail.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_preview_background_file_post_pictures_preview_background_files_instance_id201_response import CreatePreviewBackgroundFilePostPicturesPreviewBackgroundFilesInstanceId201Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview background file unique identifier
    file = None # bytes | HDR file to upload

    try:
        # Create preview background file
        api_response = await api_instance.create_preview_background_file_post_pictures_preview_background_files_instance_id(instance_id, file)
        print("The response of PreviewsApi->create_preview_background_file_post_pictures_preview_background_files_instance_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->create_preview_background_file_post_pictures_preview_background_files_instance_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Preview background file unique identifier | 
 **file** | **bytes**| HDR file to upload | 

### Return type

[**CreatePreviewBackgroundFilePostPicturesPreviewBackgroundFilesInstanceId201Response**](CreatePreviewBackgroundFilePostPicturesPreviewBackgroundFilesInstanceId201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Preview background file added successfully |  -  |
**400** | Wrong file format or error saving file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_preview_file_post_pictures_preview_files_instance_id**
> CreatePreviewFilePostPicturesPreviewFilesInstanceId201Response create_preview_file_post_pictures_preview_files_instance_id(instance_id, file)

Create preview file

Main resource to add a preview. It stores the preview file and generates three picture files (thumbnails) matching preview when it's possible, a square thumbnail, a rectangle thumbnail and a midsize file.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_preview_file_post_pictures_preview_files_instance_id201_response import CreatePreviewFilePostPicturesPreviewFilesInstanceId201Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier
    file = None # bytes | Preview file to upload

    try:
        # Create preview file
        api_response = await api_instance.create_preview_file_post_pictures_preview_files_instance_id(instance_id, file)
        print("The response of PreviewsApi->create_preview_file_post_pictures_preview_files_instance_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->create_preview_file_post_pictures_preview_files_instance_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Preview file unique identifier | 
 **file** | **bytes**| Preview file to upload | 

### Return type

[**CreatePreviewFilePostPicturesPreviewFilesInstanceId201Response**](CreatePreviewFilePostPicturesPreviewFilesInstanceId201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Preview file added successfully |  -  |
**400** | Wrong file format or normalization failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thumbnail_post_pictures_thumbnails_organisations_instance_id**
> CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response create_thumbnail_post_pictures_thumbnails_organisations_instance_id(instance_id, file)

Create thumbnail

Create a thumbnail for given object instance.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_thumbnail_post_pictures_thumbnails_organisations_instance_id201_response import CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Object instance unique identifier
    file = None # bytes | Image file to use as thumbnail

    try:
        # Create thumbnail
        api_response = await api_instance.create_thumbnail_post_pictures_thumbnails_organisations_instance_id(instance_id, file)
        print("The response of PreviewsApi->create_thumbnail_post_pictures_thumbnails_organisations_instance_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->create_thumbnail_post_pictures_thumbnails_organisations_instance_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Object instance unique identifier | 
 **file** | **bytes**| Image file to use as thumbnail | 

### Return type

[**CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response**](CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Thumbnail created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thumbnail_post_pictures_thumbnails_organisations_instance_id_png**
> CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response create_thumbnail_post_pictures_thumbnails_organisations_instance_id_png(instance_id, file)

Create thumbnail

Create a thumbnail for given object instance.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_thumbnail_post_pictures_thumbnails_organisations_instance_id201_response import CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Object instance unique identifier
    file = None # bytes | Image file to use as thumbnail

    try:
        # Create thumbnail
        api_response = await api_instance.create_thumbnail_post_pictures_thumbnails_organisations_instance_id_png(instance_id, file)
        print("The response of PreviewsApi->create_thumbnail_post_pictures_thumbnails_organisations_instance_id_png:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->create_thumbnail_post_pictures_thumbnails_organisations_instance_id_png: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Object instance unique identifier | 
 **file** | **bytes**| Image file to use as thumbnail | 

### Return type

[**CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response**](CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Thumbnail created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thumbnail_post_pictures_thumbnails_persons_instance_id**
> CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response create_thumbnail_post_pictures_thumbnails_persons_instance_id(instance_id, file)

Create thumbnail

Create a thumbnail for given object instance.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_thumbnail_post_pictures_thumbnails_organisations_instance_id201_response import CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Object instance unique identifier
    file = None # bytes | Image file to use as thumbnail

    try:
        # Create thumbnail
        api_response = await api_instance.create_thumbnail_post_pictures_thumbnails_persons_instance_id(instance_id, file)
        print("The response of PreviewsApi->create_thumbnail_post_pictures_thumbnails_persons_instance_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->create_thumbnail_post_pictures_thumbnails_persons_instance_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Object instance unique identifier | 
 **file** | **bytes**| Image file to use as thumbnail | 

### Return type

[**CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response**](CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Thumbnail created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thumbnail_post_pictures_thumbnails_persons_instance_id_png**
> CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response create_thumbnail_post_pictures_thumbnails_persons_instance_id_png(instance_id, file)

Create thumbnail

Create a thumbnail for given object instance.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_thumbnail_post_pictures_thumbnails_organisations_instance_id201_response import CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Object instance unique identifier
    file = None # bytes | Image file to use as thumbnail

    try:
        # Create thumbnail
        api_response = await api_instance.create_thumbnail_post_pictures_thumbnails_persons_instance_id_png(instance_id, file)
        print("The response of PreviewsApi->create_thumbnail_post_pictures_thumbnails_persons_instance_id_png:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->create_thumbnail_post_pictures_thumbnails_persons_instance_id_png: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Object instance unique identifier | 
 **file** | **bytes**| Image file to use as thumbnail | 

### Return type

[**CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response**](CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Thumbnail created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thumbnail_post_pictures_thumbnails_preview_background_files_instance_id_png**
> CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response create_thumbnail_post_pictures_thumbnails_preview_background_files_instance_id_png(instance_id, file)

Create thumbnail

Create a thumbnail for given object instance.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_thumbnail_post_pictures_thumbnails_organisations_instance_id201_response import CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Object instance unique identifier
    file = None # bytes | Image file to use as thumbnail

    try:
        # Create thumbnail
        api_response = await api_instance.create_thumbnail_post_pictures_thumbnails_preview_background_files_instance_id_png(instance_id, file)
        print("The response of PreviewsApi->create_thumbnail_post_pictures_thumbnails_preview_background_files_instance_id_png:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->create_thumbnail_post_pictures_thumbnails_preview_background_files_instance_id_png: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Object instance unique identifier | 
 **file** | **bytes**| Image file to use as thumbnail | 

### Return type

[**CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response**](CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Thumbnail created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thumbnail_post_pictures_thumbnails_projects_instance_id**
> CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response create_thumbnail_post_pictures_thumbnails_projects_instance_id(instance_id, file)

Create thumbnail

Create a thumbnail for given object instance.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_thumbnail_post_pictures_thumbnails_organisations_instance_id201_response import CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Object instance unique identifier
    file = None # bytes | Image file to use as thumbnail

    try:
        # Create thumbnail
        api_response = await api_instance.create_thumbnail_post_pictures_thumbnails_projects_instance_id(instance_id, file)
        print("The response of PreviewsApi->create_thumbnail_post_pictures_thumbnails_projects_instance_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->create_thumbnail_post_pictures_thumbnails_projects_instance_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Object instance unique identifier | 
 **file** | **bytes**| Image file to use as thumbnail | 

### Return type

[**CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response**](CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Thumbnail created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thumbnail_post_pictures_thumbnails_projects_instance_id_png**
> CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response create_thumbnail_post_pictures_thumbnails_projects_instance_id_png(instance_id, file)

Create thumbnail

Create a thumbnail for given object instance.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_thumbnail_post_pictures_thumbnails_organisations_instance_id201_response import CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Object instance unique identifier
    file = None # bytes | Image file to use as thumbnail

    try:
        # Create thumbnail
        api_response = await api_instance.create_thumbnail_post_pictures_thumbnails_projects_instance_id_png(instance_id, file)
        print("The response of PreviewsApi->create_thumbnail_post_pictures_thumbnails_projects_instance_id_png:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->create_thumbnail_post_pictures_thumbnails_projects_instance_id_png: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Object instance unique identifier | 
 **file** | **bytes**| Image file to use as thumbnail | 

### Return type

[**CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response**](CreateThumbnailPostPicturesThumbnailsOrganisationsInstanceId201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Thumbnail created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_preview_file**
> bytes download_preview_file(instance_id)

Download preview file

Download a generic file preview as attachment.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier

    try:
        # Download preview file
        api_response = await api_instance.download_preview_file(instance_id)
        print("The response of PreviewsApi->download_preview_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->download_preview_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Preview file unique identifier | 

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
**200** | Generic file preview downloaded as attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_preview_movie**
> bytes download_preview_movie(instance_id)

Download preview movie

Download a movie preview file as attachment.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier

    try:
        # Download preview movie
        api_response = await api_instance.download_preview_movie(instance_id)
        print("The response of PreviewsApi->download_preview_movie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->download_preview_movie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Preview file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/mp4

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Movie preview downloaded as attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_frame_from_preview**
> bytes extract_frame_from_preview(preview_file_id, frame_number=frame_number)

Extract frame from preview

Extract a frame from a preview file movie. Frame number can be specified as query parameter, defaults to 0.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    preview_file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier
    frame_number = 120 # int | Frame number to extract (optional)

    try:
        # Extract frame from preview
        api_response = await api_instance.extract_frame_from_preview(preview_file_id, frame_number=frame_number)
        print("The response of PreviewsApi->extract_frame_from_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->extract_frame_from_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preview_file_id** | **UUID**| Preview file unique identifier | 
 **frame_number** | **int**| Frame number to extract | [optional] 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Extracted frame as PNG image |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_tile_from_preview**
> bytes extract_tile_from_preview(preview_file_id)

Extract tile from preview

Extract a tile from a preview file movie.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    preview_file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier

    try:
        # Extract tile from preview
        api_response = await api_instance.extract_tile_from_preview(preview_file_id)
        print("The response of PreviewsApi->extract_tile_from_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->extract_tile_from_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preview_file_id** | **UUID**| Preview file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Extracted tile as PNG image |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_thumbnail**
> bytes get_attachment_thumbnail(attachment_file_id)

Get attachment thumbnail

Download the thumbnail representing given attachment file.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    attachment_file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Attachment file unique identifier

    try:
        # Get attachment thumbnail
        api_response = await api_instance.get_attachment_thumbnail(attachment_file_id)
        print("The response of PreviewsApi->get_attachment_thumbnail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_attachment_thumbnail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_file_id** | **UUID**| Attachment file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment thumbnail downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview_background_file_get_pictures_preview_background_files_instance_id_extension**
> bytes get_preview_background_file_get_pictures_preview_background_files_instance_id_extension(instance_id, extension)

Get preview background file

Download a preview background file.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview background file unique identifier
    extension = 'hdr' # str | File extension

    try:
        # Get preview background file
        api_response = await api_instance.get_preview_background_file_get_pictures_preview_background_files_instance_id_extension(instance_id, extension)
        print("The response of PreviewsApi->get_preview_background_file_get_pictures_preview_background_files_instance_id_extension:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_preview_background_file_get_pictures_preview_background_files_instance_id_extension: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Preview background file unique identifier | 
 **extension** | **str**| File extension | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/vnd.radiance

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preview background file downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview_file_get_pictures_originals_preview_files_instance_id_extension**
> bytes get_preview_file_get_pictures_originals_preview_files_instance_id_extension(instance_id, extension)

Get preview file

Download a generic file preview by extension.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier
    extension = 'png' # str | File extension

    try:
        # Get preview file
        api_response = await api_instance.get_preview_file_get_pictures_originals_preview_files_instance_id_extension(instance_id, extension)
        print("The response of PreviewsApi->get_preview_file_get_pictures_originals_preview_files_instance_id_extension:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_preview_file_get_pictures_originals_preview_files_instance_id_extension: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Preview file unique identifier | 
 **extension** | **str**| File extension | 

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
**200** | Generic file preview downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview_lowdef_movie**
> bytes get_preview_lowdef_movie(instance_id)

Get preview lowdef movie

Download a low definition movie preview file. Falls back to full quality if lowdef version is not available.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier

    try:
        # Get preview lowdef movie
        api_response = await api_instance.get_preview_lowdef_movie(instance_id)
        print("The response of PreviewsApi->get_preview_lowdef_movie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_preview_lowdef_movie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Preview file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/mp4

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Low definition movie preview downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview_movie**
> bytes get_preview_movie(instance_id)

Get preview movie

Download a movie preview file.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier

    try:
        # Get preview movie
        api_response = await api_instance.get_preview_movie(instance_id)
        print("The response of PreviewsApi->get_preview_movie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_preview_movie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Preview file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: video/mp4

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Movie preview downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview_thumbnail_get_movies_tiles_preview_files_instance_id_png**
> bytes get_preview_thumbnail_get_movies_tiles_preview_files_instance_id_png(instance_id)

Get preview thumbnail

Download a thumbnail for a preview file.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier

    try:
        # Get preview thumbnail
        api_response = await api_instance.get_preview_thumbnail_get_movies_tiles_preview_files_instance_id_png(instance_id)
        print("The response of PreviewsApi->get_preview_thumbnail_get_movies_tiles_preview_files_instance_id_png:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_preview_thumbnail_get_movies_tiles_preview_files_instance_id_png: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Preview file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preview thumbnail downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview_thumbnail_get_pictures_originals_preview_files_instance_id_png**
> bytes get_preview_thumbnail_get_pictures_originals_preview_files_instance_id_png(instance_id)

Get preview thumbnail

Download a thumbnail for a preview file.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier

    try:
        # Get preview thumbnail
        api_response = await api_instance.get_preview_thumbnail_get_pictures_originals_preview_files_instance_id_png(instance_id)
        print("The response of PreviewsApi->get_preview_thumbnail_get_pictures_originals_preview_files_instance_id_png:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_preview_thumbnail_get_pictures_originals_preview_files_instance_id_png: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Preview file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preview thumbnail downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview_thumbnail_get_pictures_previews_preview_files_instance_id_png**
> bytes get_preview_thumbnail_get_pictures_previews_preview_files_instance_id_png(instance_id)

Get preview thumbnail

Download a thumbnail for a preview file.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier

    try:
        # Get preview thumbnail
        api_response = await api_instance.get_preview_thumbnail_get_pictures_previews_preview_files_instance_id_png(instance_id)
        print("The response of PreviewsApi->get_preview_thumbnail_get_pictures_previews_preview_files_instance_id_png:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_preview_thumbnail_get_pictures_previews_preview_files_instance_id_png: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Preview file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preview thumbnail downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview_thumbnail_get_pictures_thumbnails_preview_files_instance_id_png**
> bytes get_preview_thumbnail_get_pictures_thumbnails_preview_files_instance_id_png(instance_id)

Get preview thumbnail

Download a thumbnail for a preview file.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier

    try:
        # Get preview thumbnail
        api_response = await api_instance.get_preview_thumbnail_get_pictures_thumbnails_preview_files_instance_id_png(instance_id)
        print("The response of PreviewsApi->get_preview_thumbnail_get_pictures_thumbnails_preview_files_instance_id_png:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_preview_thumbnail_get_pictures_thumbnails_preview_files_instance_id_png: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Preview file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preview thumbnail downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview_thumbnail_get_pictures_thumbnails_square_preview_files_instance_id_png**
> bytes get_preview_thumbnail_get_pictures_thumbnails_square_preview_files_instance_id_png(instance_id)

Get preview thumbnail

Download a thumbnail for a preview file.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier

    try:
        # Get preview thumbnail
        api_response = await api_instance.get_preview_thumbnail_get_pictures_thumbnails_square_preview_files_instance_id_png(instance_id)
        print("The response of PreviewsApi->get_preview_thumbnail_get_pictures_thumbnails_square_preview_files_instance_id_png:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_preview_thumbnail_get_pictures_thumbnails_square_preview_files_instance_id_png: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Preview file unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preview thumbnail downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_running_preview_files**
> List[GetRunningPreviewFiles200ResponseInner] get_running_preview_files(cursor_preview_file_id=cursor_preview_file_id, limit=limit)

Get running preview files

Retrieve all preview files from open productions with states equal to processing or broken.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_running_preview_files200_response_inner import GetRunningPreviewFiles200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    cursor_preview_file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | ID of the last preview file from previous page for cursor-based pagination (optional)
    limit = 100 # int | Maximum number of preview files to return (optional)

    try:
        # Get running preview files
        api_response = await api_instance.get_running_preview_files(cursor_preview_file_id=cursor_preview_file_id, limit=limit)
        print("The response of PreviewsApi->get_running_preview_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_running_preview_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor_preview_file_id** | **UUID**| ID of the last preview file from previous page for cursor-based pagination | [optional] 
 **limit** | **int**| Maximum number of preview files to return | [optional] 

### Return type

[**List[GetRunningPreviewFiles200ResponseInner]**](GetRunningPreviewFiles200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All preview files from open productions with processing or broken states |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thumbnail_get_pictures_thumbnails_organisations_instance_id**
> bytes get_thumbnail_get_pictures_thumbnails_organisations_instance_id(instance_id)

Get thumbnail

Download the thumbnail linked to given object instance.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Object instance unique identifier

    try:
        # Get thumbnail
        api_response = await api_instance.get_thumbnail_get_pictures_thumbnails_organisations_instance_id(instance_id)
        print("The response of PreviewsApi->get_thumbnail_get_pictures_thumbnails_organisations_instance_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_thumbnail_get_pictures_thumbnails_organisations_instance_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Object instance unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thumbnail downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thumbnail_get_pictures_thumbnails_organisations_instance_id_png**
> bytes get_thumbnail_get_pictures_thumbnails_organisations_instance_id_png(instance_id)

Get thumbnail

Download the thumbnail linked to given object instance.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Object instance unique identifier

    try:
        # Get thumbnail
        api_response = await api_instance.get_thumbnail_get_pictures_thumbnails_organisations_instance_id_png(instance_id)
        print("The response of PreviewsApi->get_thumbnail_get_pictures_thumbnails_organisations_instance_id_png:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_thumbnail_get_pictures_thumbnails_organisations_instance_id_png: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Object instance unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thumbnail downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thumbnail_get_pictures_thumbnails_persons_instance_id**
> bytes get_thumbnail_get_pictures_thumbnails_persons_instance_id(instance_id)

Get thumbnail

Download the thumbnail linked to given object instance.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Object instance unique identifier

    try:
        # Get thumbnail
        api_response = await api_instance.get_thumbnail_get_pictures_thumbnails_persons_instance_id(instance_id)
        print("The response of PreviewsApi->get_thumbnail_get_pictures_thumbnails_persons_instance_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_thumbnail_get_pictures_thumbnails_persons_instance_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Object instance unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thumbnail downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thumbnail_get_pictures_thumbnails_persons_instance_id_png**
> bytes get_thumbnail_get_pictures_thumbnails_persons_instance_id_png(instance_id)

Get thumbnail

Download the thumbnail linked to given object instance.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Object instance unique identifier

    try:
        # Get thumbnail
        api_response = await api_instance.get_thumbnail_get_pictures_thumbnails_persons_instance_id_png(instance_id)
        print("The response of PreviewsApi->get_thumbnail_get_pictures_thumbnails_persons_instance_id_png:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_thumbnail_get_pictures_thumbnails_persons_instance_id_png: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Object instance unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thumbnail downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thumbnail_get_pictures_thumbnails_preview_background_files_instance_id_png**
> bytes get_thumbnail_get_pictures_thumbnails_preview_background_files_instance_id_png(instance_id)

Get thumbnail

Download the thumbnail linked to given object instance.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Object instance unique identifier

    try:
        # Get thumbnail
        api_response = await api_instance.get_thumbnail_get_pictures_thumbnails_preview_background_files_instance_id_png(instance_id)
        print("The response of PreviewsApi->get_thumbnail_get_pictures_thumbnails_preview_background_files_instance_id_png:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_thumbnail_get_pictures_thumbnails_preview_background_files_instance_id_png: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Object instance unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thumbnail downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thumbnail_get_pictures_thumbnails_projects_instance_id**
> bytes get_thumbnail_get_pictures_thumbnails_projects_instance_id(instance_id)

Get thumbnail

Download the thumbnail linked to given object instance.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Object instance unique identifier

    try:
        # Get thumbnail
        api_response = await api_instance.get_thumbnail_get_pictures_thumbnails_projects_instance_id(instance_id)
        print("The response of PreviewsApi->get_thumbnail_get_pictures_thumbnails_projects_instance_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_thumbnail_get_pictures_thumbnails_projects_instance_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Object instance unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thumbnail downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thumbnail_get_pictures_thumbnails_projects_instance_id_png**
> bytes get_thumbnail_get_pictures_thumbnails_projects_instance_id_png(instance_id)

Get thumbnail

Download the thumbnail linked to given object instance.

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
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    instance_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Object instance unique identifier

    try:
        # Get thumbnail
        api_response = await api_instance.get_thumbnail_get_pictures_thumbnails_projects_instance_id_png(instance_id)
        print("The response of PreviewsApi->get_thumbnail_get_pictures_thumbnails_projects_instance_id_png:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->get_thumbnail_get_pictures_thumbnails_projects_instance_id_png: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **UUID**| Object instance unique identifier | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thumbnail downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_main_preview**
> SetMainPreview200Response set_main_preview(preview_file_id, frame_number=frame_number)

Set main preview

Set given preview as main preview of the related entity. This preview will be used to illustrate the entity.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.set_main_preview200_response import SetMainPreview200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    preview_file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier
    frame_number = 120 # int | Frame number for movie previews (optional)

    try:
        # Set main preview
        api_response = await api_instance.set_main_preview(preview_file_id, frame_number=frame_number)
        print("The response of PreviewsApi->set_main_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->set_main_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preview_file_id** | **UUID**| Preview file unique identifier | 
 **frame_number** | **int**| Frame number for movie previews | [optional] 

### Return type

[**SetMainPreview200Response**](SetMainPreview200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preview set as main preview |  -  |
**400** | Cannot use frame number on non-movie preview |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_preview_annotations**
> UpdatePreviewAnnotations200Response update_preview_annotations(preview_file_id, update_preview_annotations_request)

Update preview annotations

Allow to modify the annotations stored at the preview level. Modifications are applied via three fields, additions to give all the annotations that need to be added, updates that list annotations that needs to be modified, and deletions to list the IDs of annotations that needs to be removed.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.update_preview_annotations200_response import UpdatePreviewAnnotations200Response
from sometech.pykitsu._client.models.update_preview_annotations_request import UpdatePreviewAnnotationsRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    preview_file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier
    update_preview_annotations_request = sometech.pykitsu._client.UpdatePreviewAnnotationsRequest() # UpdatePreviewAnnotationsRequest | 

    try:
        # Update preview annotations
        api_response = await api_instance.update_preview_annotations(preview_file_id, update_preview_annotations_request)
        print("The response of PreviewsApi->update_preview_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->update_preview_annotations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preview_file_id** | **UUID**| Preview file unique identifier | 
 **update_preview_annotations_request** | [**UpdatePreviewAnnotationsRequest**](UpdatePreviewAnnotationsRequest.md)|  | 

### Return type

[**UpdatePreviewAnnotations200Response**](UpdatePreviewAnnotations200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preview annotations updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_preview_position**
> UpdatePreviewPosition200Response update_preview_position(preview_file_id, update_preview_position_request=update_preview_position_request)

Update preview position

Allow to change orders of previews for a single revision.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.update_preview_position200_response import UpdatePreviewPosition200Response
from sometech.pykitsu._client.models.update_preview_position_request import UpdatePreviewPositionRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PreviewsApi(api_client)
    preview_file_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Preview file unique identifier
    update_preview_position_request = sometech.pykitsu._client.UpdatePreviewPositionRequest() # UpdatePreviewPositionRequest |  (optional)

    try:
        # Update preview position
        api_response = await api_instance.update_preview_position(preview_file_id, update_preview_position_request=update_preview_position_request)
        print("The response of PreviewsApi->update_preview_position:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PreviewsApi->update_preview_position: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preview_file_id** | **UUID**| Preview file unique identifier | 
 **update_preview_position_request** | [**UpdatePreviewPositionRequest**](UpdatePreviewPositionRequest.md)|  | [optional] 

### Return type

[**UpdatePreviewPosition200Response**](UpdatePreviewPosition200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preview position updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

