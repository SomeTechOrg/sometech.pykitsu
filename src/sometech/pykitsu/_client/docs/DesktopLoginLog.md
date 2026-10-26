# DesktopLoginLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**person_id** | **UUID** | Person ID | [optional] 

## Example

```python
from sometech.pykitsu._client.models.desktop_login_log import DesktopLoginLog

# TODO update the JSON string below
json = "{}"
# create an instance of DesktopLoginLog from a JSON string
desktop_login_log_instance = DesktopLoginLog.from_json(json)
# print the JSON string representation of the object
print(DesktopLoginLog.to_json())

# convert the object into a dict
desktop_login_log_dict = desktop_login_log_instance.to_dict()
# create an instance of DesktopLoginLog from a dict
desktop_login_log_from_dict = DesktopLoginLog.from_dict(desktop_login_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


