# sometech.pykitsu._client.DepartmentsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_hardware_item_to_department**](DepartmentsApi.md#add_hardware_item_to_department) | **POST** /data/departments/{department_id}/hardware-items | Add hardware item to department
[**add_software_license_to_department**](DepartmentsApi.md#add_software_license_to_department) | **POST** /data/departments/{department_id}/software-licenses | Add software license to department
[**get_all_department_hardware_items**](DepartmentsApi.md#get_all_department_hardware_items) | **GET** /data/departments/hardware-items | Get all department hardware items
[**get_all_department_software_licenses**](DepartmentsApi.md#get_all_department_software_licenses) | **GET** /data/departments/software-licenses | Get all department software licenses
[**get_department_hardware_items**](DepartmentsApi.md#get_department_hardware_items) | **GET** /data/departments/{department_id}/hardware-items/{hardware_item_id} | Get department hardware items
[**get_department_software_licenses**](DepartmentsApi.md#get_department_software_licenses) | **GET** /data/departments/{department_id}/software-licenses/{software_id} | Get department software licenses
[**remove_hardware_item_from_department**](DepartmentsApi.md#remove_hardware_item_from_department) | **DELETE** /data/departments/{department_id}/hardware-items/{hardware_item_id} | Remove hardware item from department
[**remove_software_license_from_department**](DepartmentsApi.md#remove_software_license_from_department) | **DELETE** /data/departments/{department_id}/software-licenses/{software_id} | Remove software license from department


# **add_hardware_item_to_department**
> AddHardwareItemToDepartment201Response add_hardware_item_to_department(department_id, add_hardware_item_to_department_request)

Add hardware item to department

Associate a hardware item with a specific department. This allows the department to use the specified hardware in budget forecasting.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_hardware_item_to_department201_response import AddHardwareItemToDepartment201Response
from sometech.pykitsu._client.models.add_hardware_item_to_department_request import AddHardwareItemToDepartmentRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.DepartmentsApi(api_client)
    department_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the department
    add_hardware_item_to_department_request = sometech.pykitsu._client.AddHardwareItemToDepartmentRequest() # AddHardwareItemToDepartmentRequest | 

    try:
        # Add hardware item to department
        api_response = await api_instance.add_hardware_item_to_department(department_id, add_hardware_item_to_department_request)
        print("The response of DepartmentsApi->add_hardware_item_to_department:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->add_hardware_item_to_department: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **UUID**| Unique identifier of the department | 
 **add_hardware_item_to_department_request** | [**AddHardwareItemToDepartmentRequest**](AddHardwareItemToDepartmentRequest.md)|  | 

### Return type

[**AddHardwareItemToDepartment201Response**](AddHardwareItemToDepartment201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Hardware item successfully added to department |  -  |
**400** | Hardware item ID matches no hardware item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_software_license_to_department**
> AddSoftwareLicenseToDepartment201Response add_software_license_to_department(department_id, add_software_license_to_department_request)

Add software license to department

Associate a software license with a specific department. This allows the department to use the specified software in budget forecasting.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_software_license_to_department201_response import AddSoftwareLicenseToDepartment201Response
from sometech.pykitsu._client.models.add_software_license_to_department_request import AddSoftwareLicenseToDepartmentRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.DepartmentsApi(api_client)
    department_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the department
    add_software_license_to_department_request = sometech.pykitsu._client.AddSoftwareLicenseToDepartmentRequest() # AddSoftwareLicenseToDepartmentRequest | 

    try:
        # Add software license to department
        api_response = await api_instance.add_software_license_to_department(department_id, add_software_license_to_department_request)
        print("The response of DepartmentsApi->add_software_license_to_department:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->add_software_license_to_department: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **UUID**| Unique identifier of the department | 
 **add_software_license_to_department_request** | [**AddSoftwareLicenseToDepartmentRequest**](AddSoftwareLicenseToDepartmentRequest.md)|  | 

### Return type

[**AddSoftwareLicenseToDepartment201Response**](AddSoftwareLicenseToDepartment201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Software license successfully added to department |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_department_hardware_items**
> Dict[str, List[GetAllDepartmentHardwareItems200ResponseValueInner]] get_all_department_hardware_items()

Get all department hardware items

Retrieve all hardware items organized by department. Returns a dictionary where each department contains its associated hardware items.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_all_department_hardware_items200_response_value_inner import GetAllDepartmentHardwareItems200ResponseValueInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.DepartmentsApi(api_client)

    try:
        # Get all department hardware items
        api_response = await api_instance.get_all_department_hardware_items()
        print("The response of DepartmentsApi->get_all_department_hardware_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->get_all_department_hardware_items: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, List[GetAllDepartmentHardwareItems200ResponseValueInner]]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Department hardware items successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_department_software_licenses**
> Dict[str, List[GetAllDepartmentSoftwareLicenses200ResponseValueInner]] get_all_department_software_licenses()

Get all department software licenses

Retrieve all software licenses organized by department. Returns a dictionary where each department contains its associated software licenses.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_all_department_software_licenses200_response_value_inner import GetAllDepartmentSoftwareLicenses200ResponseValueInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.DepartmentsApi(api_client)

    try:
        # Get all department software licenses
        api_response = await api_instance.get_all_department_software_licenses()
        print("The response of DepartmentsApi->get_all_department_software_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->get_all_department_software_licenses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, List[GetAllDepartmentSoftwareLicenses200ResponseValueInner]]**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Department software licenses successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_department_hardware_items**
> List[GetAllDepartmentHardwareItems200ResponseValueInner] get_department_hardware_items(department_id, hardware_item_id)

Get department hardware items

Retrieve all hardware items that are associated with a specific department.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_all_department_hardware_items200_response_value_inner import GetAllDepartmentHardwareItems200ResponseValueInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.DepartmentsApi(api_client)
    department_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the department
    hardware_item_id = 'hardware_item_id_example' # str | 

    try:
        # Get department hardware items
        api_response = await api_instance.get_department_hardware_items(department_id, hardware_item_id)
        print("The response of DepartmentsApi->get_department_hardware_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->get_department_hardware_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **UUID**| Unique identifier of the department | 
 **hardware_item_id** | **str**|  | 

### Return type

[**List[GetAllDepartmentHardwareItems200ResponseValueInner]**](GetAllDepartmentHardwareItems200ResponseValueInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Department hardware items successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_department_software_licenses**
> List[GetAllDepartmentSoftwareLicenses200ResponseValueInner] get_department_software_licenses(department_id, software_id)

Get department software licenses

Retrieve all software items that are associated with a specific department.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_all_department_software_licenses200_response_value_inner import GetAllDepartmentSoftwareLicenses200ResponseValueInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.DepartmentsApi(api_client)
    department_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the department
    software_id = 'software_id_example' # str | 

    try:
        # Get department software licenses
        api_response = await api_instance.get_department_software_licenses(department_id, software_id)
        print("The response of DepartmentsApi->get_department_software_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->get_department_software_licenses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **UUID**| Unique identifier of the department | 
 **software_id** | **str**|  | 

### Return type

[**List[GetAllDepartmentSoftwareLicenses200ResponseValueInner]**](GetAllDepartmentSoftwareLicenses200ResponseValueInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Department software licenses successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_hardware_item_from_department**
> remove_hardware_item_from_department(department_id, hardware_item_id)

Remove hardware item from department

Remove a hardware item from a specific department. This disassociates the hardware from the department.

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
    api_instance = sometech.pykitsu._client.DepartmentsApi(api_client)
    department_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the department
    hardware_item_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Unique identifier of the hardware item to remove

    try:
        # Remove hardware item from department
        await api_instance.remove_hardware_item_from_department(department_id, hardware_item_id)
    except Exception as e:
        print("Exception when calling DepartmentsApi->remove_hardware_item_from_department: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **UUID**| Unique identifier of the department | 
 **hardware_item_id** | **UUID**| Unique identifier of the hardware item to remove | 

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
**204** | Hardware item successfully removed from department |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_software_license_from_department**
> remove_software_license_from_department(department_id, software_id)

Remove software license from department

Remove a software license from a specific department. This disassociates the software license from the department.

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
    api_instance = sometech.pykitsu._client.DepartmentsApi(api_client)
    department_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Unique identifier of the department
    software_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Unique identifier of the software license to remove

    try:
        # Remove software license from department
        await api_instance.remove_software_license_from_department(department_id, software_id)
    except Exception as e:
        print("Exception when calling DepartmentsApi->remove_software_license_from_department: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **UUID**| Unique identifier of the department | 
 **software_id** | **UUID**| Unique identifier of the software license to remove | 

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
**204** | Software license successfully removed from department |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

