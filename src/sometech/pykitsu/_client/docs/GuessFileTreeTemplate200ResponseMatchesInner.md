# GuessFileTreeTemplate200ResponseMatchesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **str** | Template name | [optional] 
**confidence** | **float** | Confidence score | [optional] 
**data** | [**GuessFileTreeTemplate200ResponseMatchesInnerData**](GuessFileTreeTemplate200ResponseMatchesInnerData.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.guess_file_tree_template200_response_matches_inner import GuessFileTreeTemplate200ResponseMatchesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GuessFileTreeTemplate200ResponseMatchesInner from a JSON string
guess_file_tree_template200_response_matches_inner_instance = GuessFileTreeTemplate200ResponseMatchesInner.from_json(json)
# print the JSON string representation of the object
print(GuessFileTreeTemplate200ResponseMatchesInner.to_json())

# convert the object into a dict
guess_file_tree_template200_response_matches_inner_dict = guess_file_tree_template200_response_matches_inner_instance.to_dict()
# create an instance of GuessFileTreeTemplate200ResponseMatchesInner from a dict
guess_file_tree_template200_response_matches_inner_from_dict = GuessFileTreeTemplate200ResponseMatchesInner.from_dict(guess_file_tree_template200_response_matches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


