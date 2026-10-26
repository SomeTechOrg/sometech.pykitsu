# GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Log entry unique identifier | [optional] 
**person_id** | **UUID** | Person unique identifier | [optional] 
**var_date** | **datetime** | Login date and time | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs200_response_inner import GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner from a JSON string
get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs200_response_inner_instance = GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner.to_json())

# convert the object into a dict
get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs200_response_inner_dict = get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs200_response_inner_instance.to_dict()
# create an instance of GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner from a dict
get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs200_response_inner_from_dict = GetDesktopLoginLogsGetDataPersonsPersonIdDesktopLoginLogs200ResponseInner.from_dict(get_desktop_login_logs_get_data_persons_person_id_desktop_login_logs200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


