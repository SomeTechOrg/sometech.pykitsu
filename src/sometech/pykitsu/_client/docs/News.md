# News


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change** | **bool** |  | [optional] [default to False]
**author_id** | **UUID** | Person who wrote the comment | [optional] 
**comment_id** | **UUID** | Posted comment ID | [optional] 
**task_id** | **UUID** | Task ID | [optional] 
**preview_file_id** | **UUID** | Preview file ID | [optional] 
**id** | **UUID** | News unique identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.news import News

# TODO update the JSON string below
json = "{}"
# create an instance of News from a JSON string
news_instance = News.from_json(json)
# print the JSON string representation of the object
print(News.to_json())

# convert the object into a dict
news_dict = news_instance.to_dict()
# create an instance of News from a dict
news_from_dict = News.from_dict(news_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


