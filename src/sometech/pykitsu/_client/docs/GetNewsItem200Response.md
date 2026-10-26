# GetNewsItem200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique news item identifier | [optional] 
**title** | **str** | News item title | [optional] 
**content** | **str** | News item content | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**author_id** | **UUID** | Author&#39;s user ID | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_news_item200_response import GetNewsItem200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNewsItem200Response from a JSON string
get_news_item200_response_instance = GetNewsItem200Response.from_json(json)
# print the JSON string representation of the object
print(GetNewsItem200Response.to_json())

# convert the object into a dict
get_news_item200_response_dict = get_news_item200_response_instance.to_dict()
# create an instance of GetNewsItem200Response from a dict
get_news_item200_response_from_dict = GetNewsItem200Response.from_dict(get_news_item200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


