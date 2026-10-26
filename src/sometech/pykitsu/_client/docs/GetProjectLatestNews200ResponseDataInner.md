# GetProjectLatestNews200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique news item identifier | [optional] 
**title** | **str** | News item title | [optional] 
**content** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**author_id** | **UUID** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_project_latest_news200_response_data_inner import GetProjectLatestNews200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectLatestNews200ResponseDataInner from a JSON string
get_project_latest_news200_response_data_inner_instance = GetProjectLatestNews200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectLatestNews200ResponseDataInner.to_json())

# convert the object into a dict
get_project_latest_news200_response_data_inner_dict = get_project_latest_news200_response_data_inner_instance.to_dict()
# create an instance of GetProjectLatestNews200ResponseDataInner from a dict
get_project_latest_news200_response_data_inner_from_dict = GetProjectLatestNews200ResponseDataInner.from_dict(get_project_latest_news200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


