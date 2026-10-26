# CreateBudget201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Budget unique identifier | [optional] 
**name** | **str** | Budget name | [optional] 
**currency** | **str** | Budget currency code | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_budget201_response import CreateBudget201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBudget201Response from a JSON string
create_budget201_response_instance = CreateBudget201Response.from_json(json)
# print the JSON string representation of the object
print(CreateBudget201Response.to_json())

# convert the object into a dict
create_budget201_response_dict = create_budget201_response_instance.to_dict()
# create an instance of CreateBudget201Response from a dict
create_budget201_response_from_dict = CreateBudget201Response.from_dict(create_budget201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


