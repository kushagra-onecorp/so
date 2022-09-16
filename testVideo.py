import json
import requests

# Access Token from Facebook Graph API
facebook_access_token = "EAALefOGyJXQBAMDZAbmDHtujY2U2PuZAlBM5YREr1Y0aA37TFHYsYfoSPEwEzZAAsSaPexU6jwqfPgShGOUZC8LKy1fJb1ZAK3DI795EnvAvWjiCHinJGZCFhZCKEW9h4hagZCvZAcTxn38GLHmfqCEy1XdVXeCxZAohjr46tYZCBz19BtlX85TZCZB5A"
# Facebook Page ID
facebook_page_id = '101434159376809'
# Post Title
post_title = 'Post Title'
# Post Description
post_description = 'Post Description'
# Post Text(title+description)
post_text = f"""
{post_title}
{post_description}
"""
# URL of the video to post
video_url = 'https://promote.onecorp.co.in/media/test-video-2.mp4'
facebook_video_upload_url = f'https://graph.facebook.com/v15.0/{facebook_page_id}/videos'
facebook_upload_body = {
    'file_url': video_url,
    "description": post_text,
    "title": 'title',
    'access_token': facebook_access_token
}
print(facebook_video_upload_url)
print(facebook_upload_body)
facebook_video_response = requests.post(
    facebook_video_upload_url, data=facebook_upload_body)
print(facebook_video_response.json())
