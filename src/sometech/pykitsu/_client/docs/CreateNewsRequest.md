# CreateNewsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**project_id** | **UUID** |  | 
**content** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_news_request import CreateNewsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewsRequest from a JSON string
create_news_request_instance = CreateNewsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNewsRequest.to_json())

# convert the object into a dict
create_news_request_dict = create_news_request_instance.to_dict()
# create an instance of CreateNewsRequest from a dict
create_news_request_from_dict = CreateNewsRequest.from_dict(create_news_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


