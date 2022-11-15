import json
import os
import requests

# Access Token from LinkedIn API
linkedin_access_token = """AQXXi-OtP2vmDU5s1hDPafx5ywKFY5uEg3MzPazm8vAEMH5nKbTTTXLzYMSxzMqIDj9Way2XWtFW2s3iNMvAudIS-Ya_hD0OyTZBQlUv6JlYhFzwPh4assPVK3rbW--CHwkij8Kc2wroBooNhsMeliOQQyBeELKngQrmAiRKIbCLzIL4CxGPYmV4kYLRh4tDDO6UV64OwAze4-9s-NMw3AK8d6d2pmJWQufKm-LPRbBNi1O2pF_1cQ4ikatMKHxSRp48ncoBw8YuZrSr--Mn3QkluTPoXGs2B3Uu4F5vfA8zbUIY3HX4neD_rgg3-j37a_e3o6851bt2SFnlWQ26GJHqSeW7NQ"""
# Post Title
post_title = 'Post Title'
# Post Description
post_description = 'Post Description'
# Post Text(title+description)
post_text = f"""
{post_title}
{post_description}
"""
# LinkedIn Profile ID
linkedin_profile_id = 'iyflcZ2ma3'
#
video = './videos/test-video-2.mp4'
linkedin_post_url = "https://api.linkedin.com/v2/posts"
linkedin_url = "https://api.linkedin.com/v2/videos?action=finalizeUpload"
linkedin_register_url = 'https://api.linkedin.com/v2/videos?action=initializeUpload'
linkedin_register_body = {
    "initializeUploadRequest": {
        "owner": f"urn:li:person:{linkedin_profile_id}",
        "fileSizeBytes": os.path.getsize(video),
        "purpose": "FEED_VIDEO",
        "uploadCaptions": False,
        "uploadThumbnail": False
    }
}
print('-------------------LinkedinRegisterBody:')
print(linkedin_register_body)
print('-------------------LinkedinRegisterBody************')
print('<------------------------------------------------------------------->')
linkedin_headers = {
    'Authorization': f'Bearer {linkedin_access_token}',
    'X-Restli-Protocol-Version': '2.0.0'
}
media_ids = []
linkedin_register_response = requests.post(
    linkedin_register_url, headers=linkedin_headers, json=linkedin_register_body)
print('-------------------LinkedinRegisterResponse:')
print(linkedin_register_response.json())
print('-------------------LinkedinRegisterResponse************')
print('<------------------------------------------------------------------->')
linkedin_upload_url = linkedin_register_response.json(
)['value']['uploadInstructions'][0]['uploadUrl']
linkedin_upload_token = linkedin_register_response.json(
)['value']['uploadToken']
linkedin_headers = {
    'Authorization': f'Bearer {linkedin_access_token}',
    'Content-Type': 'application/octet-stream',
    'X-Restli-Protocol-Version': '2.0.0'
}
with open(video, 'rb') as linkedin_upload_image:
    data = linkedin_upload_image.read()
    linkedin_upload_response = requests.put(
        linkedin_upload_url, headers=linkedin_headers, data=data)
print('-------------------LinkedinUploadResponseStatus:')
print(linkedin_upload_response)
print('-------------------LinkedinUploadResponseStatus************')
print('<------------------------------------------------------------------->')
print('-------------------LinkedinUploadResponseHeaderETag:')
print(linkedin_upload_response.headers.get('ETag'))
print('-------------------LinkedinUploadResponseHeaderETagv')
print('<------------------------------------------------------------------->')
linkedin_asset_id = linkedin_register_response.json()['value']['video']
print('-------------------LinkedinAssestID:')
print(linkedin_asset_id)
print('-------------------LinkedinAssestID************')
print('<------------------------------------------------------------------->')
print('-------------------LinkedinUploadResponse:')
print(linkedin_upload_response.text)
print('-------------------LinkedinUploadResponse************')
print('<------------------------------------------------------------------->')
data = json.dumps({
    "finalizeUploadRequest": {
        "video": linkedin_asset_id,
        "uploadToken": "",
        "uploadedPartIds": [linkedin_upload_response.headers.get('ETag')]
        }
    })
print(type(linkedin_upload_response.headers.get('ETag')))
# linkedin_post_data=json.dumps(linkedin_post_data)
print('-------------------LinkedinPostData:')
print(data)
print('-------------------LinkedinPostData************')
print('<------------------------------------------------------------------->')
linkedin_headers = {
    "Authorization": f"Bearer {linkedin_access_token}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0"
}
linkedin_post_response = requests.post(
    linkedin_url, headers=linkedin_headers, data=data)
print('-------------------LinkedinFinalizeResponse:')
print(linkedin_post_response.text)
print('-------------------LinkedinFinalizeResponse************')
data={
  "author": f"urn:li:person:{linkedin_profile_id}",
  "commentary": post_text,
  "visibility": "PUBLIC",
  "distribution": {
    "feedDistribution": "MAIN_FEED",
    "targetEntities": [],
    "thirdPartyDistributionChannels": []
  },
  "content": {
    "media": {
      "title":post_text[0:20],
      "id": linkedin_asset_id
    }
  },
  "lifecycleState": "PUBLISHED",
}
linkedin_headers = {
    "Authorization": f"Bearer {linkedin_access_token}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0"
}
linkedin_post_response = requests.post(
    linkedin_post_url, headers=linkedin_headers, data=json.dumps(data))
print('-------------------LinkedinPostResponse:')
print(linkedin_post_response.text)
print('-------------------LinkedinPostResponse************')


