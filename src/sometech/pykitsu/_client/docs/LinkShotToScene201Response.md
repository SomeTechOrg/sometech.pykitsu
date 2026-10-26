# LinkShotToScene201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scene_id** | **UUID** |  | [optional] 
**shot_id** | **UUID** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.link_shot_to_scene201_response import LinkShotToScene201Response

# TODO update the JSON string below
json = "{}"
# create an instance of LinkShotToScene201Response from a JSON string
link_shot_to_scene201_response_instance = LinkShotToScene201Response.from_json(json)
# print the JSON string representation of the object
print(LinkShotToScene201Response.to_json())

# convert the object into a dict
link_shot_to_scene201_response_dict = link_shot_to_scene201_response_instance.to_dict()
# create an instance of LinkShotToScene201Response from a dict
link_shot_to_scene201_response_from_dict = LinkShotToScene201Response.from_dict(link_shot_to_scene201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


