import json
import os
import requests

# Access Token from LinkedIn API
linkedin_access_token = """AQXSdnLGN4Z_3ykhLaSKOs1-8omRqXnOAHW-d4jHlzF_kU-DNFcYJHwm9phFpZRBLF-p-_jsBMbURdVRVj0EYFbxjrMyOCUmTkiBxa8iPfGm0JGYwa062oCQS8ve7h8h-NkzudRA_Onqh_mY3DvaVBAolHZ1sJVQ8s9PF3BEPgRMr7MVzEZ3_6s8-cvSIXtUrDKWQNmIFnp2OQ-hwJJdbUXMxHzgsgkUuZr62paHrdsx_H6TdJonfX05EYXPnt6A9YHettCT10ZESsfIHgL6xAvt4IE-U9j3sa0oyt9dHbKCX_DEVGTB9hCJUIqD0nLWxY1uh1EP5xkylLkRL9Udz85gbCRsEQ"""
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
linkedin_profile_id = 'gXaSyTq5Tm'
#
video = './videos/test-video-2.mp4'
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
data = {
    "finalizeUploadRequest": {
        "video": linkedin_asset_id,
        "uploadToken": "",
        "uploadedPartIds": [linkedin_upload_response.headers.get('ETag')]
        }
    }
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
    linkedin_url, headers=linkedin_headers, data=json.dumps(data))
print('-------------------LinkedinPostResponse:')
print(linkedin_post_response.json())
print('-------------------LinkedinPostResponse************')
