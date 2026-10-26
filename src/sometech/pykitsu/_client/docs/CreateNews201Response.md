# CreateNews201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**title** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**content** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_news201_response import CreateNews201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNews201Response from a JSON string
create_news201_response_instance = CreateNews201Response.from_json(json)
# print the JSON string representation of the object
print(CreateNews201Response.to_json())

# convert the object into a dict
create_news201_response_dict = create_news201_response_instance.to_dict()
# create an instance of CreateNews201Response from a dict
create_news201_response_from_dict = CreateNews201Response.from_dict(create_news201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


