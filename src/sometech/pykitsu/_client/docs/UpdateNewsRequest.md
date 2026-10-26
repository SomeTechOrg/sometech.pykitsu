# UpdateNewsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_news_request import UpdateNewsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNewsRequest from a JSON string
update_news_request_instance = UpdateNewsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateNewsRequest.to_json())

# convert the object into a dict
update_news_request_dict = update_news_request_instance.to_dict()
# create an instance of UpdateNewsRequest from a dict
update_news_request_from_dict = UpdateNewsRequest.from_dict(update_news_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


