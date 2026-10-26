# PostCommentOnSharedPlaylistRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_id** | **UUID** |  | 
**task_id** | **UUID** |  | 
**task_status_id** | **UUID** |  | 
**text** | **str** |  | [optional] 
**checklist** | **List[object]** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.post_comment_on_shared_playlist_request import PostCommentOnSharedPlaylistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCommentOnSharedPlaylistRequest from a JSON string
post_comment_on_shared_playlist_request_instance = PostCommentOnSharedPlaylistRequest.from_json(json)
# print the JSON string representation of the object
print(PostCommentOnSharedPlaylistRequest.to_json())

# convert the object into a dict
post_comment_on_shared_playlist_request_dict = post_comment_on_shared_playlist_request_instance.to_dict()
# create an instance of PostCommentOnSharedPlaylistRequest from a dict
post_comment_on_shared_playlist_request_from_dict = PostCommentOnSharedPlaylistRequest.from_dict(post_comment_on_shared_playlist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


