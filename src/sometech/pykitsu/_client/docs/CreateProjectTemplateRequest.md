# CreateProjectTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**fps** | **str** |  | [optional] 
**ratio** | **str** |  | [optional] 
**resolution** | **str** |  | [optional] 
**production_type** | **str** |  | [optional] 
**production_style** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_project_template_request import CreateProjectTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectTemplateRequest from a JSON string
create_project_template_request_instance = CreateProjectTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectTemplateRequest.to_json())

# convert the object into a dict
create_project_template_request_dict = create_project_template_request_instance.to_dict()
# create an instance of CreateProjectTemplateRequest from a dict
create_project_template_request_from_dict = CreateProjectTemplateRequest.from_dict(create_project_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


