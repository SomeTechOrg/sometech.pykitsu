# LoginLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin** | **str** | web, script | [optional] 
**ip_address** | **str** | IP address of device used to login | [optional] 
**person_id** | **UUID** | Person ID | [optional] 
**id** | **UUID** | Login log unique identifier | [optional] 
**created_at** | **datetime** | Login timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.login_log import LoginLog

# TODO update the JSON string below
json = "{}"
# create an instance of LoginLog from a JSON string
login_log_instance = LoginLog.from_json(json)
# print the JSON string representation of the object
print(LoginLog.to_json())

# convert the object into a dict
login_log_dict = login_log_instance.to_dict()
# create an instance of LoginLog from a dict
login_log_from_dict = LoginLog.from_dict(login_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


