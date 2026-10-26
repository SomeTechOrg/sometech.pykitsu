# GetContext200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **object** | Current user information | [optional] 
**projects** | **List[object]** | Available projects | [optional] 
**departments** | **List[object]** | Available departments | [optional] 
**asset_types** | **List[object]** | Available asset types | [optional] 
**task_types** | **List[object]** | Available task types | [optional] 
**task_status** | **List[object]** | Available task statuses | [optional] 
**custom_actions** | **List[object]** | Available custom actions | [optional] 
**status_automations** | **List[object]** | Available status automations | [optional] 
**studios** | **List[object]** | Available studios | [optional] 
**notification_count** | **int** | Number of unread notifications | [optional] 
**persons** | **List[object]** | Available persons | [optional] 
**project_status** | **List[object]** | Available project statuses | [optional] 
**search_filters** | **List[object]** | Available search filters | [optional] 
**search_filter_groups** | **List[object]** | Available search filter groups | [optional] 
**preview_background_files** | **List[object]** | Available preview background files | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_context200_response import GetContext200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetContext200Response from a JSON string
get_context200_response_instance = GetContext200Response.from_json(json)
# print the JSON string representation of the object
print(GetContext200Response.to_json())

# convert the object into a dict
get_context200_response_dict = get_context200_response_instance.to_dict()
# create an instance of GetContext200Response from a dict
get_context200_response_from_dict = GetContext200Response.from_dict(get_context200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


