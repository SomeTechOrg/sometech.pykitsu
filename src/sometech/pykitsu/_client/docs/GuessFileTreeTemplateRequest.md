# GuessFileTreeTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** | Project unique identifier | 
**file_path** | **str** | File path to analyze | 
**sep** | **str** | Path separator | [optional] [default to '/']

## Example

```python
from sometech.pykitsu._client.models.guess_file_tree_template_request import GuessFileTreeTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GuessFileTreeTemplateRequest from a JSON string
guess_file_tree_template_request_instance = GuessFileTreeTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(GuessFileTreeTemplateRequest.to_json())

# convert the object into a dict
guess_file_tree_template_request_dict = guess_file_tree_template_request_instance.to_dict()
# create an instance of GuessFileTreeTemplateRequest from a dict
guess_file_tree_template_request_from_dict = GuessFileTreeTemplateRequest.from_dict(guess_file_tree_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


