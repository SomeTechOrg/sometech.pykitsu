# GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Login log unique identifier | [optional] 
**person_id** | **UUID** | Person identifier | [optional] 
**var_date** | **date** | Login date | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_desktop_login_logs_get_data_user_desktop_login_logs200_response_inner import GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner from a JSON string
get_desktop_login_logs_get_data_user_desktop_login_logs200_response_inner_instance = GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner.to_json())

# convert the object into a dict
get_desktop_login_logs_get_data_user_desktop_login_logs200_response_inner_dict = get_desktop_login_logs_get_data_user_desktop_login_logs200_response_inner_instance.to_dict()
# create an instance of GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner from a dict
get_desktop_login_logs_get_data_user_desktop_login_logs200_response_inner_from_dict = GetDesktopLoginLogsGetDataUserDesktopLoginLogs200ResponseInner.from_dict(get_desktop_login_logs_get_data_user_desktop_login_logs200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


