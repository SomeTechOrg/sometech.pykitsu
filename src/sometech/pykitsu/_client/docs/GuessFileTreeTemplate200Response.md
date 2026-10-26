# GuessFileTreeTemplate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | [**List[GuessFileTreeTemplate200ResponseMatchesInner]**](GuessFileTreeTemplate200ResponseMatchesInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.guess_file_tree_template200_response import GuessFileTreeTemplate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GuessFileTreeTemplate200Response from a JSON string
guess_file_tree_template200_response_instance = GuessFileTreeTemplate200Response.from_json(json)
# print the JSON string representation of the object
print(GuessFileTreeTemplate200Response.to_json())

# convert the object into a dict
guess_file_tree_template200_response_dict = guess_file_tree_template200_response_instance.to_dict()
# create an instance of GuessFileTreeTemplate200Response from a dict
guess_file_tree_template200_response_from_dict = GuessFileTreeTemplate200Response.from_dict(guess_file_tree_template200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


