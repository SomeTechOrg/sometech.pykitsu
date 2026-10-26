# sometech.pykitsu._client.ChatApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chat_message_post_data_entities_entity_id_chat_messages**](ChatApi.md#create_chat_message_post_data_entities_entity_id_chat_messages) | **POST** /data/entities/{entity_id}/chat/messages | Create chat message
[**delete_chat_message_delete_data_entities_entity_id_chat_messages_chat_message_id**](ChatApi.md#delete_chat_message_delete_data_entities_entity_id_chat_messages_chat_message_id) | **DELETE** /data/entities/{entity_id}/chat/messages/{chat_message_id} | Delete chat message
[**get_chat_details**](ChatApi.md#get_chat_details) | **GET** /data/entities/{entity_id}/chat | Get chat details
[**get_chat_message_get_data_entities_entity_id_chat_messages_chat_message_id**](ChatApi.md#get_chat_message_get_data_entities_entity_id_chat_messages_chat_message_id) | **GET** /data/entities/{entity_id}/chat/messages/{chat_message_id} | Get chat message
[**get_chat_messages_get_data_entities_entity_id_chat_messages**](ChatApi.md#get_chat_messages_get_data_entities_entity_id_chat_messages) | **GET** /data/entities/{entity_id}/chat/messages | Get chat messages


# **create_chat_message_post_data_entities_entity_id_chat_messages**
> CreateChatMessagePostDataEntitiesEntityIdChatMessages201Response create_chat_message_post_data_entities_entity_id_chat_messages(entity_id, create_chat_message_post_data_entities_entity_id_chat_messages_request)

Create chat message

Create a new chat message for a specific entity. Supports both JSON and form data with optional file attachments. Only chat participants can send messages.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_chat_message_post_data_entities_entity_id_chat_messages201_response import CreateChatMessagePostDataEntitiesEntityIdChatMessages201Response
from sometech.pykitsu._client.models.create_chat_message_post_data_entities_entity_id_chat_messages_request import CreateChatMessagePostDataEntitiesEntityIdChatMessagesRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ChatApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | ID of the entity related to the chat
    create_chat_message_post_data_entities_entity_id_chat_messages_request = sometech.pykitsu._client.CreateChatMessagePostDataEntitiesEntityIdChatMessagesRequest() # CreateChatMessagePostDataEntitiesEntityIdChatMessagesRequest | 

    try:
        # Create chat message
        api_response = await api_instance.create_chat_message_post_data_entities_entity_id_chat_messages(entity_id, create_chat_message_post_data_entities_entity_id_chat_messages_request)
        print("The response of ChatApi->create_chat_message_post_data_entities_entity_id_chat_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->create_chat_message_post_data_entities_entity_id_chat_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| ID of the entity related to the chat | 
 **create_chat_message_post_data_entities_entity_id_chat_messages_request** | [**CreateChatMessagePostDataEntitiesEntityIdChatMessagesRequest**](CreateChatMessagePostDataEntitiesEntityIdChatMessagesRequest.md)|  | 

### Return type

[**CreateChatMessagePostDataEntitiesEntityIdChatMessages201Response**](CreateChatMessagePostDataEntitiesEntityIdChatMessages201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Chat message successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chat_message_delete_data_entities_entity_id_chat_messages_chat_message_id**
> delete_chat_message_delete_data_entities_entity_id_chat_messages_chat_message_id(entity_id, chat_message_id)

Delete chat message

Delete a specific chat message. Only the message author or administrators can delete messages.

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
    api_instance = sometech.pykitsu._client.ChatApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | ID of the entity related to the chat
    chat_message_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | ID of the chat message to delete

    try:
        # Delete chat message
        await api_instance.delete_chat_message_delete_data_entities_entity_id_chat_messages_chat_message_id(entity_id, chat_message_id)
    except Exception as e:
        print("Exception when calling ChatApi->delete_chat_message_delete_data_entities_entity_id_chat_messages_chat_message_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| ID of the entity related to the chat | 
 **chat_message_id** | **UUID**| ID of the chat message to delete | 

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
**204** | Chat message successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_details**
> GetChatDetails200Response get_chat_details(entity_id)

Get chat details

Retrieve chat information and messages for a specific entity. Returns chat metadata including participants and all associated messages.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_chat_details200_response import GetChatDetails200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ChatApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | ID of the entity related to the chat

    try:
        # Get chat details
        api_response = await api_instance.get_chat_details(entity_id)
        print("The response of ChatApi->get_chat_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_chat_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| ID of the entity related to the chat | 

### Return type

[**GetChatDetails200Response**](GetChatDetails200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat information successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_message_get_data_entities_entity_id_chat_messages_chat_message_id**
> GetChatMessageGetDataEntitiesEntityIdChatMessagesChatMessageId200Response get_chat_message_get_data_entities_entity_id_chat_messages_chat_message_id(entity_id, chat_message_id)

Get chat message

Retrieve a specific chat message by its ID. Returns detailed message information including content and metadata.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_chat_message_get_data_entities_entity_id_chat_messages_chat_message_id200_response import GetChatMessageGetDataEntitiesEntityIdChatMessagesChatMessageId200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ChatApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | ID of the entity related to the chat
    chat_message_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | ID of the chat message

    try:
        # Get chat message
        api_response = await api_instance.get_chat_message_get_data_entities_entity_id_chat_messages_chat_message_id(entity_id, chat_message_id)
        print("The response of ChatApi->get_chat_message_get_data_entities_entity_id_chat_messages_chat_message_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_chat_message_get_data_entities_entity_id_chat_messages_chat_message_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| ID of the entity related to the chat | 
 **chat_message_id** | **UUID**| ID of the chat message | 

### Return type

[**GetChatMessageGetDataEntitiesEntityIdChatMessagesChatMessageId200Response**](GetChatMessageGetDataEntitiesEntityIdChatMessagesChatMessageId200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat message successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_messages_get_data_entities_entity_id_chat_messages**
> List[GetChatMessagesGetDataEntitiesEntityIdChatMessages200ResponseInner] get_chat_messages_get_data_entities_entity_id_chat_messages(entity_id)

Get chat messages

Retrieve all chat messages for a specific entity. Returns a list of messages with sender information and timestamps.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_chat_messages_get_data_entities_entity_id_chat_messages200_response_inner import GetChatMessagesGetDataEntitiesEntityIdChatMessages200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.ChatApi(api_client)
    entity_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | ID of the entity related to the chat

    try:
        # Get chat messages
        api_response = await api_instance.get_chat_messages_get_data_entities_entity_id_chat_messages(entity_id)
        print("The response of ChatApi->get_chat_messages_get_data_entities_entity_id_chat_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_chat_messages_get_data_entities_entity_id_chat_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **UUID**| ID of the entity related to the chat | 

### Return type

[**List[GetChatMessagesGetDataEntitiesEntityIdChatMessages200ResponseInner]**](GetChatMessagesGetDataEntitiesEntityIdChatMessages200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat messages successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

