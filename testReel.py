from time import sleep
import requests

# Access Token from Facebook Graph API
instragram_access_token = "EAALefOGyJXQBAGIMNYnZA11z2EyqCd0b86JdPiZCKBzWbJopaaWy1zlgaLcmGNTizAV5yTQPf6Nq1g4Nap5NeBaJq0IpzESdXL40WHWPDLQU5SkHL1TfhWJSIAmbdny6LTRZAqZCMb1tL5ibs7eQsVKv66ZCtofOOvOUjBQn7LJ8LZAwn7DPkt "
# Instagram User ID
instagram_user_id = '103995469037355'
# URL of the image to post
video_url = 'https://promote.onecorp.co.in/media/test-video-2.mp4'
# Post Title
post_title = 'Post Title'
# Post Description
post_description = 'Post Description'
# Post Text(title+description)
post_text = f"""
{post_title}
{post_description}
"""
media_id = []
# API Request URL to upload the image
instagram_upload_request_url = f'https://graph.facebook.com/v13.0/{instagram_user_id}/video_reels'
instagram_upload_params = {
    "upload_phase": "start",
    "access_token": instragram_access_token
}
# Send POST request to media url
instagram_upload_response = requests.post(
    instagram_upload_request_url, params=instagram_upload_params)
print(instagram_upload_response.text)
media_id = instagram_upload_response.json()['video_id']
# media_id="17953640773969028"
instagram_upload_url = instagram_upload_response.json()['upload_url']
instagram_upload_headers = {
    "Authorization": f"OAuth {instragram_access_token}",
    "file_url": video_url
}
instagram_upload_response = requests.post(
    instagram_upload_url, headers=instagram_upload_headers)
print(instagram_upload_response.text)
instagram_status_headers = {
    "Authorization": f"OAuth {instragram_access_token}"
}
isPosted = False
while not isPosted:
    sleep(5)
    instagram_status_url = f'https://graph.facebook.com/v13.0/{media_id}?fields=status&access_token={instragram_access_token}'
    instagram_publish_response = requests.get(
        instagram_status_url, headers=instagram_status_headers)
    print(instagram_publish_response.text)
    if instagram_publish_response.json().get('status', False).get("uploading_phase", False).get('status',False) == 'complete':
        instagram_publish_url = f'https://graph.facebook.com/v13.0/{instagram_user_id}/video_reels'
        # Payload for publish request
        instagram_publish_payload = {
            'video_id': media_id,
            'upload_phase': 'finish',
            'video_state': 'PUBLISHED',
            "description":post_description,
            'access_token': instragram_access_token
        }
        # Send POST request to publish url
        instagram_publish_response = requests.post(
            instagram_publish_url, data=instagram_publish_payload)
        print(instagram_publish_response.json())
        isPosted = True
