# GetLoginLogs200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Login log unique identifier | [optional] 
**created_at** | **datetime** | Login timestamp | [optional] 
**ip_address** | **str** | IP address of the login | [optional] 
**person_id** | **UUID** | Person identifier | [optional] 
**origin** | **str** | Login origin | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_login_logs200_response_inner import GetLoginLogs200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoginLogs200ResponseInner from a JSON string
get_login_logs200_response_inner_instance = GetLoginLogs200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetLoginLogs200ResponseInner.to_json())

# convert the object into a dict
get_login_logs200_response_inner_dict = get_login_logs200_response_inner_instance.to_dict()
# create an instance of GetLoginLogs200ResponseInner from a dict
get_login_logs200_response_inner_from_dict = GetLoginLogs200ResponseInner.from_dict(get_login_logs200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


