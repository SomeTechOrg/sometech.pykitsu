# sometech.pykitsu._client.PersonsApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_person_to_department**](PersonsApi.md#add_person_to_department) | **POST** /actions/persons/{person_id}/departments/add | Add person to department
[**change_person_password**](PersonsApi.md#change_person_password) | **POST** /actions/persons/{person_id}/change-password | Change person password
[**clear_person_avatar**](PersonsApi.md#clear_person_avatar) | **DELETE** /actions/persons/{person_id}/clear-avatar | Clear person avatar
[**create_desktop_login_log_post_data_persons_person_id_desktop_login_logs**](PersonsApi.md#create_desktop_login_log_post_data_persons_person_id_desktop_login_logs) | **POST** /data/persons/{person_id}/desktop-login-logs | Create desktop login log
[**disable_two_factor_authentication**](PersonsApi.md#disable_two_factor_authentication) | **DELETE** /actions/persons/{person_id}/disable-two-factor-authentication | Disable two factor authentication
[**get_all_month_time_spents**](PersonsApi.md#get_all_month_time_spents) | **GET** /data/persons/{person_id}/time-spents/month/all/{year}/{month} | Get all month time spents
[**get_day_off_get_data_persons_person_id_day_offs_date**](PersonsApi.md#get_day_off_get_data_persons_person_id_day_offs_date) | **GET** /data/persons/{person_id}/day-offs/{date} | Get day off
[**get_day_offs_for_month**](PersonsApi.md#get_day_offs_for_month) | **GET** /data/persons/day-offs/{year}/{month} | Get day offs for month
[**get_day_quota_shots**](PersonsApi.md#get_day_quota_shots) | **GET** /data/persons/{person_id}/quota-shots/day/{year}/{month}/{day} | Get day quota shots
[**get_day_time_spents**](PersonsApi.md#get_day_time_spents) | **GET** /data/persons/{person_id}/time-spents/day/{year}/{month}/{day} | Get day time spents
[**get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs**](PersonsApi.md#get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs) | **GET** /data/persons/{person_id}/desktop-login-logs | Get desktop login logs
[**get_month_quota_shots**](PersonsApi.md#get_month_quota_shots) | **GET** /data/persons/{person_id}/quota-shots/month/{year}/{month} | Get month quota shots
[**get_month_time_spents**](PersonsApi.md#get_month_time_spents) | **GET** /data/persons/{person_id}/time-spents/month/{year}/{month} | Get month time spents
[**get_person_day_offs**](PersonsApi.md#get_person_day_offs) | **GET** /data/persons/{person_id}/day-offs | Get person day offs
[**get_person_month_day_offs**](PersonsApi.md#get_person_month_day_offs) | **GET** /data/persons/{person_id}/day-offs/month/{year}/{month} | Get person month day offs
[**get_person_week_day_offs**](PersonsApi.md#get_person_week_day_offs) | **GET** /data/persons/{person_id}/day-offs/week/{year}/{week} | Get person week day offs
[**get_person_year_day_offs**](PersonsApi.md#get_person_year_day_offs) | **GET** /data/persons/{person_id}/day-offs/year/{year} | Get person year day offs
[**get_presence_logs**](PersonsApi.md#get_presence_logs) | **GET** /data/persons/presence-logs/{month_date} | Get presence logs
[**get_time_spent_month_table**](PersonsApi.md#get_time_spent_month_table) | **GET** /data/persons/time-spents/day-table/{year}/{month} | Get time spent month table
[**get_time_spent_months_table**](PersonsApi.md#get_time_spent_months_table) | **GET** /data/persons/time-spents/month-table/{year} | Get time spent months table
[**get_time_spent_weeks_table**](PersonsApi.md#get_time_spent_weeks_table) | **GET** /data/persons/time-spents/week-table/{year} | Get time spent weeks table
[**get_time_spent_years_table**](PersonsApi.md#get_time_spent_years_table) | **GET** /data/persons/time-spents/year-table/ | Get time spent years table
[**get_time_spents_for_date**](PersonsApi.md#get_time_spents_for_date) | **GET** /data/persons/{person_id}/time-spents/{date} | Get time spents for date
[**get_time_spents_get_data_persons_person_id_time_spents**](PersonsApi.md#get_time_spents_get_data_persons_person_id_time_spents) | **GET** /data/persons/{person_id}/time-spents | Get time spents
[**get_week_quota_shots**](PersonsApi.md#get_week_quota_shots) | **GET** /data/persons/{person_id}/quota-shots/week/{year}/{week} | Get week quota shots
[**get_week_time_spents**](PersonsApi.md#get_week_time_spents) | **GET** /data/persons/{person_id}/time-spents/week/{year}/{week} | Get week time spents
[**get_year_time_spents**](PersonsApi.md#get_year_time_spents) | **GET** /data/persons/{person_id}/time-spents/year/{year} | Get year time spents
[**invite_person**](PersonsApi.md#invite_person) | **GET** /actions/persons/{person_id}/invite | Invite person
[**remove_person_from_department**](PersonsApi.md#remove_person_from_department) | **DELETE** /actions/persons/{person_id}/departments/{department_id} | Remove person from department


# **add_person_to_department**
> AddPersonToDepartment201Response add_person_to_department(person_id, add_person_to_department_request)

Add person to department

Add a user to given department.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.add_person_to_department201_response import AddPersonToDepartment201Response
from sometech.pykitsu._client.models.add_person_to_department_request import AddPersonToDepartmentRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    add_person_to_department_request = sometech.pykitsu._client.AddPersonToDepartmentRequest() # AddPersonToDepartmentRequest | 

    try:
        # Add person to department
        api_response = await api_instance.add_person_to_department(person_id, add_person_to_department_request)
        print("The response of PersonsApi->add_person_to_department:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->add_person_to_department: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **add_person_to_department_request** | [**AddPersonToDepartmentRequest**](AddPersonToDepartmentRequest.md)|  | 

### Return type

[**AddPersonToDepartment201Response**](AddPersonToDepartment201Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User added to given department |  -  |
**400** | Invalid department ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_person_password**
> ChangePersonPassword200Response change_person_password(person_id, change_person_password_request)

Change person password

Allow admin to change password for given user. An admin can't change other admins password. The new password requires a confirmation to ensure that the admin didn't make a mistake by typing the new password.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.change_person_password200_response import ChangePersonPassword200Response
from sometech.pykitsu._client.models.change_person_password_request import ChangePersonPasswordRequest
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    change_person_password_request = sometech.pykitsu._client.ChangePersonPasswordRequest() # ChangePersonPasswordRequest | 

    try:
        # Change person password
        api_response = await api_instance.change_person_password(person_id, change_person_password_request)
        print("The response of PersonsApi->change_person_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->change_person_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **change_person_password_request** | [**ChangePersonPasswordRequest**](ChangePersonPasswordRequest.md)|  | 

### Return type

[**ChangePersonPassword200Response**](ChangePersonPassword200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password changed successfully |  -  |
**400** | Invalid password or inactive user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_person_avatar**
> clear_person_avatar(person_id)

Clear person avatar

Set has_avatar flag to False for current user and remove its avatar file.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier

    try:
        # Clear person avatar
        await api_instance.clear_person_avatar(person_id)
    except Exception as e:
        print("Exception when calling PersonsApi->clear_person_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**204** | Avatar file deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_desktop_login_log_post_data_persons_person_id_desktop_login_logs**
> GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner create_desktop_login_log_post_data_persons_person_id_desktop_login_logs(person_id, create_desktop_login_log_post_data_persons_person_id_desktop_login_logs_request)

Create desktop login log

Add a new log entry for desktop logins for a person.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.create_desktop_login_log_post_data_persons_person_id_desktop_login_logs_request import CreateDesktopLoginLogPostDataPersonsPersonIdDesktopLoginLogsRequest
from sometech.pykitsu._client.models.get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs200_response_inner import GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    create_desktop_login_log_post_data_persons_person_id_desktop_login_logs_request = sometech.pykitsu._client.CreateDesktopLoginLogPostDataPersonsPersonIdDesktopLoginLogsRequest() # CreateDesktopLoginLogPostDataPersonsPersonIdDesktopLoginLogsRequest | 

    try:
        # Create desktop login log
        api_response = await api_instance.create_desktop_login_log_post_data_persons_person_id_desktop_login_logs(person_id, create_desktop_login_log_post_data_persons_person_id_desktop_login_logs_request)
        print("The response of PersonsApi->create_desktop_login_log_post_data_persons_person_id_desktop_login_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->create_desktop_login_log_post_data_persons_person_id_desktop_login_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **create_desktop_login_log_post_data_persons_person_id_desktop_login_logs_request** | [**CreateDesktopLoginLogPostDataPersonsPersonIdDesktopLoginLogsRequest**](CreateDesktopLoginLogPostDataPersonsPersonIdDesktopLoginLogsRequest.md)|  | 

### Return type

[**GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner**](GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Desktop login log entry created |  -  |
**400** | Invalid date format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_two_factor_authentication**
> ChangePersonPassword200Response disable_two_factor_authentication(person_id)

Disable two factor authentication

Allow admin to disable two factor authentication for given user. An admin can't disable two factor authentication for other admins.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.change_person_password200_response import ChangePersonPassword200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier

    try:
        # Disable two factor authentication
        api_response = await api_instance.disable_two_factor_authentication(person_id)
        print("The response of PersonsApi->disable_two_factor_authentication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->disable_two_factor_authentication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 

### Return type

[**ChangePersonPassword200Response**](ChangePersonPassword200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Two factor authentication disabled successfully |  -  |
**400** | Inactive user or two factor authentication not enabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_month_time_spents**
> List[object] get_all_month_time_spents(person_id, year, month)

Get all month time spents

Get all time spents for a given person and month.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    year = 2022 # int | Year to get time spents for
    month = 7 # int | Month to get time spents for

    try:
        # Get all month time spents
        api_response = await api_instance.get_all_month_time_spents(person_id, year, month)
        print("The response of PersonsApi->get_all_month_time_spents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_all_month_time_spents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **year** | **int**| Year to get time spents for | 
 **month** | **int**| Month to get time spents for | 

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
**200** | All time spents for the given person and month |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_day_off_get_data_persons_person_id_day_offs_date**
> GetDayOffGetDataPersonsPersonIdDayOffsDate200Response get_day_off_get_data_persons_person_id_day_offs_date(person_id, var_date)

Get day off

Get day off object for given person and date.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_day_off_get_data_persons_person_id_day_offs_date200_response import GetDayOffGetDataPersonsPersonIdDayOffsDate200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    var_date = '2022-07-12' # date | Date to get day off for

    try:
        # Get day off
        api_response = await api_instance.get_day_off_get_data_persons_person_id_day_offs_date(person_id, var_date)
        print("The response of PersonsApi->get_day_off_get_data_persons_person_id_day_offs_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_day_off_get_data_persons_person_id_day_offs_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **var_date** | **date**| Date to get day off for | 

### Return type

[**GetDayOffGetDataPersonsPersonIdDayOffsDate200Response**](GetDayOffGetDataPersonsPersonIdDayOffsDate200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Day off object for given person and date |  -  |
**400** | Wrong date format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_day_offs_for_month**
> List[object] get_day_offs_for_month(year, month)

Get day offs for month

Return all day off recorded for given month. Admins get all day offs, regular users get only their own.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    year = 2022 # int | Year to get day offs for
    month = 7 # int | Month to get day offs for

    try:
        # Get day offs for month
        api_response = await api_instance.get_day_offs_for_month(year, month)
        print("The response of PersonsApi->get_day_offs_for_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_day_offs_for_month: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year to get day offs for | 
 **month** | **int**| Month to get day offs for | 

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
**200** | All day off recorded for given month |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_day_quota_shots**
> List[object] get_day_quota_shots(person_id, year, month, day, count_mode=count_mode)

Get day quota shots

Get ended shots used for quota calculation of this day.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    year = 2022 # int | Year to get quota shots for
    month = 7 # int | Month to get quota shots for
    day = 12 # int | Day to get quota shots for
    count_mode = 'weighted' # str | Count mode for quota calculation (optional)

    try:
        # Get day quota shots
        api_response = await api_instance.get_day_quota_shots(person_id, year, month, day, count_mode=count_mode)
        print("The response of PersonsApi->get_day_quota_shots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_day_quota_shots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **year** | **int**| Year to get quota shots for | 
 **month** | **int**| Month to get quota shots for | 
 **day** | **int**| Day to get quota shots for | 
 **count_mode** | **str**| Count mode for quota calculation | [optional] 

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
**200** | Ended shots used for quota calculation of this day |  -  |
**400** | Wrong date format or invalid count mode |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_day_time_spents**
> GetDayTimeSpents200Response get_day_time_spents(person_id, year, month, day)

Get day time spents

Get aggregated time spents for given person and day.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_day_time_spents200_response import GetDayTimeSpents200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    year = 2022 # int | Year to get aggregated time spents for
    month = 7 # int | Month to get aggregated time spents for
    day = 12 # int | Day to get aggregated time spents for

    try:
        # Get day time spents
        api_response = await api_instance.get_day_time_spents(person_id, year, month, day)
        print("The response of PersonsApi->get_day_time_spents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_day_time_spents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **year** | **int**| Year to get aggregated time spents for | 
 **month** | **int**| Month to get aggregated time spents for | 
 **day** | **int**| Day to get aggregated time spents for | 

### Return type

[**GetDayTimeSpents200Response**](GetDayTimeSpents200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Aggregated time spents for given person and day |  -  |
**400** | Wrong date format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs**
> List[GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner] get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs(person_id)

Get desktop login logs

Retrieve desktop login logs for a person. Desktop login logs can only be created by current user.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs200_response_inner import GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier

    try:
        # Get desktop login logs
        api_response = await api_instance.get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs(person_id)
        print("The response of PersonsApi->get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 

### Return type

[**List[GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner]**](GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Desktop login logs for the person |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_month_quota_shots**
> List[object] get_month_quota_shots(person_id, year, month, count_mode=count_mode)

Get month quota shots

Get ended shots used for quota calculation of this month.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    year = 2022 # int | Year to get quota shots for
    month = 7 # int | Month to get quota shots for
    count_mode = 'weighted' # str | Count mode for quota calculation (optional)

    try:
        # Get month quota shots
        api_response = await api_instance.get_month_quota_shots(person_id, year, month, count_mode=count_mode)
        print("The response of PersonsApi->get_month_quota_shots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_month_quota_shots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **year** | **int**| Year to get quota shots for | 
 **month** | **int**| Month to get quota shots for | 
 **count_mode** | **str**| Count mode for quota calculation | [optional] 

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
**200** | Ended shots used for quota calculation of this month |  -  |
**400** | Wrong date format or invalid count mode |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_month_time_spents**
> GetMonthTimeSpents200Response get_month_time_spents(person_id, year, month)

Get month time spents

Get aggregated time spents for given person and month.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_month_time_spents200_response import GetMonthTimeSpents200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    year = 2022 # int | Year to get aggregated time spents for
    month = 7 # int | Month to get aggregated time spents for

    try:
        # Get month time spents
        api_response = await api_instance.get_month_time_spents(person_id, year, month)
        print("The response of PersonsApi->get_month_time_spents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_month_time_spents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **year** | **int**| Year to get aggregated time spents for | 
 **month** | **int**| Month to get aggregated time spents for | 

### Return type

[**GetMonthTimeSpents200Response**](GetMonthTimeSpents200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Aggregated time spents for given person and month |  -  |
**400** | Wrong date format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_day_offs**
> List[object] get_person_day_offs(person_id)

Get person day offs

Return all day offs recorded for given person.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier

    try:
        # Get person day offs
        api_response = await api_instance.get_person_day_offs(person_id)
        print("The response of PersonsApi->get_person_day_offs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_person_day_offs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 

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
**200** | All day off recorded for given person |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_month_day_offs**
> List[object] get_person_month_day_offs(person_id, year, month)

Get person month day offs

Return all day off recorded for given month and person.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    year = 2022 # int | Year to get day offs for
    month = 7 # int | Month to get day offs for

    try:
        # Get person month day offs
        api_response = await api_instance.get_person_month_day_offs(person_id, year, month)
        print("The response of PersonsApi->get_person_month_day_offs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_person_month_day_offs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **year** | **int**| Year to get day offs for | 
 **month** | **int**| Month to get day offs for | 

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
**200** | All day off recorded for given month and person |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_week_day_offs**
> List[object] get_person_week_day_offs(person_id, year, week)

Get person week day offs

Return all day off recorded for given week and person.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    year = 2022 # int | Year to get day offs for
    week = 35 # int | Week number to get day offs for

    try:
        # Get person week day offs
        api_response = await api_instance.get_person_week_day_offs(person_id, year, week)
        print("The response of PersonsApi->get_person_week_day_offs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_person_week_day_offs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **year** | **int**| Year to get day offs for | 
 **week** | **int**| Week number to get day offs for | 

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
**200** | All day off recorded for given week and person |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_year_day_offs**
> List[object] get_person_year_day_offs(person_id, year)

Get person year day offs

Return all day off recorded for given year and person.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    year = 2022 # int | Year to get day offs for

    try:
        # Get person year day offs
        api_response = await api_instance.get_person_year_day_offs(person_id, year)
        print("The response of PersonsApi->get_person_year_day_offs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_person_year_day_offs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **year** | **int**| Year to get day offs for | 

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
**200** | All day off recorded for given year and person |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_presence_logs**
> bytes get_presence_logs(month_date)

Get presence logs

Return a CSV file containing the presence logs based on a daily basis for the given month.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    month_date = '2022-07' # date | Month in YYYY-MM format

    try:
        # Get presence logs
        api_response = await api_instance.get_presence_logs(month_date)
        print("The response of PersonsApi->get_presence_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_presence_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month_date** | **date**| Month in YYYY-MM format | 

### Return type

**bytes**

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV file containing the presence logs based on daily basis |  -  |
**400** | Invalid date format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_spent_month_table**
> object get_time_spent_month_table(year, month)

Get time spent month table

Return a table giving time spent by user and by day for given year and month.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    year = 2022 # int | Year to get time spent table for
    month = 7 # int | Month to get time spent table for

    try:
        # Get time spent month table
        api_response = await api_instance.get_time_spent_month_table(year, month)
        print("The response of PersonsApi->get_time_spent_month_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_time_spent_month_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year to get time spent table for | 
 **month** | **int**| Month to get time spent table for | 

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
**200** | Table giving time spent by user and by day for given year and month |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_spent_months_table**
> object get_time_spent_months_table(year)

Get time spent months table

Return a table giving time spent by user and by month for given year.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    year = 2022 # int | Year to get time spent table for

    try:
        # Get time spent months table
        api_response = await api_instance.get_time_spent_months_table(year)
        print("The response of PersonsApi->get_time_spent_months_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_time_spent_months_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year to get time spent table for | 

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
**200** | Table giving time spent by user and by month for given year |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_spent_weeks_table**
> object get_time_spent_weeks_table(year)

Get time spent weeks table

Return a table giving time spent by user and by week for given year.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    year = 2022 # int | Year to get time spent table for

    try:
        # Get time spent weeks table
        api_response = await api_instance.get_time_spent_weeks_table(year)
        print("The response of PersonsApi->get_time_spent_weeks_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_time_spent_weeks_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year to get time spent table for | 

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
**200** | Table giving time spent by user and by week for given year |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_spent_years_table**
> object get_time_spent_years_table()

Get time spent years table

Return a table giving time spent by user and by month for all years.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)

    try:
        # Get time spent years table
        api_response = await api_instance.get_time_spent_years_table()
        print("The response of PersonsApi->get_time_spent_years_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_time_spent_years_table: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Table giving time spent by user and by month for all years |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_spents_for_date**
> List[TimeSpent] get_time_spents_for_date(person_id, var_date)

Get time spents for date

Get time spents for given person and specific date.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.time_spent import TimeSpent
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    var_date = '2022-07-12' # date | Date to get time spents for

    try:
        # Get time spents for date
        api_response = await api_instance.get_time_spents_for_date(person_id, var_date)
        print("The response of PersonsApi->get_time_spents_for_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_time_spents_for_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **var_date** | **date**| Date to get time spents for | 

### Return type

[**List[TimeSpent]**](TimeSpent.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time spents for given person and date |  -  |
**400** | Wrong date format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_spents_get_data_persons_person_id_time_spents**
> List[TimeSpent] get_time_spents_get_data_persons_person_id_time_spents(person_id, start_date=start_date, end_date=end_date)

Get time spents

Get all time spents for the given person. Optionally can accept date range parameters.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.time_spent import TimeSpent
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    start_date = '2022-07-01' # date | Start date for date range filter (optional)
    end_date = '2022-07-31' # date | End date for date range filter (optional)

    try:
        # Get time spents
        api_response = await api_instance.get_time_spents_get_data_persons_person_id_time_spents(person_id, start_date=start_date, end_date=end_date)
        print("The response of PersonsApi->get_time_spents_get_data_persons_person_id_time_spents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_time_spents_get_data_persons_person_id_time_spents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **start_date** | **date**| Start date for date range filter | [optional] 
 **end_date** | **date**| End date for date range filter | [optional] 

### Return type

[**List[TimeSpent]**](TimeSpent.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All time spents for the given person |  -  |
**400** | Invalid date range parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_week_quota_shots**
> List[object] get_week_quota_shots(person_id, year, week, count_mode=count_mode)

Get week quota shots

Get ended shots used for quota calculation of this week.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    year = 2022 # int | Year to get quota shots for
    week = 35 # int | Week number to get quota shots for
    count_mode = 'weighted' # str | Count mode for quota calculation (optional)

    try:
        # Get week quota shots
        api_response = await api_instance.get_week_quota_shots(person_id, year, week, count_mode=count_mode)
        print("The response of PersonsApi->get_week_quota_shots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_week_quota_shots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **year** | **int**| Year to get quota shots for | 
 **week** | **int**| Week number to get quota shots for | 
 **count_mode** | **str**| Count mode for quota calculation | [optional] 

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
**200** | Ended shots used for quota calculation of this week |  -  |
**400** | Wrong date format or invalid count mode |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_week_time_spents**
> GetWeekTimeSpents200Response get_week_time_spents(person_id, year, week)

Get week time spents

Get aggregated time spents for given person and week.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_week_time_spents200_response import GetWeekTimeSpents200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    year = 2022 # int | Year to get aggregated time spents for
    week = 35 # int | Week number to get aggregated time spents for

    try:
        # Get week time spents
        api_response = await api_instance.get_week_time_spents(person_id, year, week)
        print("The response of PersonsApi->get_week_time_spents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_week_time_spents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **year** | **int**| Year to get aggregated time spents for | 
 **week** | **int**| Week number to get aggregated time spents for | 

### Return type

[**GetWeekTimeSpents200Response**](GetWeekTimeSpents200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Aggregated time spents for given person and week |  -  |
**400** | Wrong date format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_year_time_spents**
> GetYearTimeSpents200Response get_year_time_spents(person_id, year)

Get year time spents

Get aggregated time spents for given person and year.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.get_year_time_spents200_response import GetYearTimeSpents200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    year = 2022 # int | Year to get aggregated time spents for

    try:
        # Get year time spents
        api_response = await api_instance.get_year_time_spents(person_id, year)
        print("The response of PersonsApi->get_year_time_spents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->get_year_time_spents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **year** | **int**| Year to get aggregated time spents for | 

### Return type

[**GetYearTimeSpents200Response**](GetYearTimeSpents200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Aggregated time spents for given person and year |  -  |
**400** | Wrong date format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_person**
> InvitePerson200Response invite_person(person_id)

Invite person

Sends an email to given person to invite him or her to connect to Kitsu.

### Example

* Api Key Authentication (JWTAuthorization):

```python
import sometech.pykitsu._client
from sometech.pykitsu._client.models.invite_person200_response import InvitePerson200Response
from sometech.pykitsu._client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sometech.pykitsu._client.Configuration(
    host = "http://localhost:8080/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWTAuthorization
configuration.api_key['JWTAuthorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWTAuthorization'] = 'Bearer'

# Enter a context with an instance of the API client
async with sometech.pykitsu._client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier

    try:
        # Invite person
        api_response = await api_instance.invite_person(person_id)
        print("The response of PersonsApi->invite_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->invite_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 

### Return type

[**InvitePerson200Response**](InvitePerson200Response.md)

### Authorization

[JWTAuthorization](../README.md#JWTAuthorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Email sent successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_person_from_department**
> remove_person_from_department(person_id, department_id)

Remove person from department

Remove a user from given department.

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
    api_instance = sometech.pykitsu._client.PersonsApi(api_client)
    person_id = UUID('a24a6ea4-ce75-4665-a070-57453082c25') # UUID | Person unique identifier
    department_id = UUID('b35b7fb5-df86-5776-b181-68564193d36') # UUID | Department unique identifier

    try:
        # Remove person from department
        await api_instance.remove_person_from_department(person_id, department_id)
    except Exception as e:
        print("Exception when calling PersonsApi->remove_person_from_department: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **UUID**| Person unique identifier | 
 **department_id** | **UUID**| Department unique identifier | 

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
**204** | User removed from given department |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

