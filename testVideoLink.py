import json
import os
import requests

# Access Token from LinkedIn API
linkedin_access_token = """AQUELXsoelp_FvnaNZp8zKQ1dywAbRM4BEwSfJX9SKk4j927k58cw7P7uNfymGWMBhhym4fqCSkwRRtTZdQTTlpSmu5IftwMvvGfIr-lmyAO97b2RRsR8e5GhH2MFt3AkWfLqx8Lg8ZOQbpFZelsLtKYPrABP8C9aumDAT_7qSx4nOf-hi4dWymAdM7X8OOmQGsmzD9VXJCy4kK2ghvi5-IuCoEgJsLqBvOn3bXpz6x-7duoxBZQOalbz-z9XyqDnoA6Zgu-eBC_uRwLvAIRzNmq9-DrXI4sW5wfZv3RCM9FQPdyUKI5fPgvGC38wapoEfIJUBHBY98-lGvob-jdH4E_Uxveww"""
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
video = './videos/test-video-3.mp4'
linkedin_upload_image = open(video, 'rb')
linkedin_url = "https://api.linkedin.com/v2/videos?action=finalizeUpload"
linkedin_register_url = 'https://api.linkedin.com/v2/videos?action=initializeUpload'
linkedin_register_body = {
    "initializeUploadRequest": {
        "owner": f"urn:li:person:{linkedin_profile_id}",
        "fileSizeBytes": os.path.getsize(video),
        "uploadCaptions": False,
        "uploadThumbnail": False
    }
}
print('-------------------LinkedinRegisterBody')
print(linkedin_register_body)
print('-------------------LinkedinRegisterBody')
print('<------------------------------------------------------------------->')
linkedin_headers = {
    'Authorization': f'Bearer {linkedin_access_token}',
}
media_ids = []
linkedin_register_response = requests.post(
    linkedin_register_url, headers=linkedin_headers, json=linkedin_register_body)
print('-------------------LinkedinRegisterResponse')
print(linkedin_register_response.json())
print('-------------------LinkedinRegisterResponse')
print('<------------------------------------------------------------------->')
linkedin_upload_url = linkedin_register_response.json(
)['value']['uploadInstructions'][0]['uploadUrl']
linkedin_headers = {
    'Authorization': f'Bearer {linkedin_access_token}',
}
linkedin_upload_response = requests.put(
    linkedin_upload_url, data=linkedin_upload_image, headers=linkedin_headers)
print('-------------------LinkedinUploadResponseHeader:')
print(linkedin_upload_response.headers['ETag'])
print('-------------------LinkedinUploadResponseHeader:')
print('<------------------------------------------------------------------->')
linkedin_asset_id = linkedin_register_response.json()['value']['video']
print('-------------------LinkedinAssestID')
print(linkedin_asset_id)
print('-------------------LinkedinAssestID')
print('<------------------------------------------------------------------->')
print('-------------------LinkedinUploadResponse')
print(linkedin_upload_response.text)
print('-------------------LinkedinUploadResponse')
print('<------------------------------------------------------------------->')
linkedin_post_data = {
    "finalizeUploadRequest": {
        "video": linkedin_asset_id,
        "uploadToken": "",
        "uploadedPartIds": [linkedin_upload_response.headers.get('ETag')]
    }
}
print('-------------------LinkedinPostData')
print(linkedin_post_data)
print('-------------------LinkedinPostData')
print('<------------------------------------------------------------------->')
linkedin_headers = {
    "Authorization": f"Bearer {linkedin_access_token}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0"
}
linkedin_post_response = requests.post(
    linkedin_url, headers=linkedin_headers, json=json.dumps(linkedin_post_data))
print('-------------------LinkedinPostResponse')
print(linkedin_post_response.json())
print('-------------------LinkedinPostResponse')
