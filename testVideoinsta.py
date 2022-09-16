from time import sleep
import requests

# Access Token from Facebook Graph API
instragram_access_token = "EAAJQ4liagnQBAIX22t66vAErZBZCXGZClXTyMpkiLqG3OTTW2ZAbxbNJZCWCVf1wZAeLA87DHCYVBsT5Uwuz4LKvMivz0LeQVEg2biH8KoTYUSbP1adieqsQmErsDqZBf801V9uy6SflgpAjM83dMjeYuyN4mnGZBNoRFh6fEuejLfLMdgN2zZAbcvnjqyctzDoWIosqxTJcMd8bK7en6OVRkpJVlLE2nZByeI3fnZCEW3GewZDZD"
# Instagram User ID
instagram_user_id = '17841453883347404'
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
instagram_media_request_url = f'https://graph.facebook.com/v10.0/{instagram_user_id}/media'
instagram_media_payload = {
        "media_type": "VIDEO",
        'video_url': video_url,
        'caption': post_text,
        'access_token': instragram_access_token
    }
    # Send POST request to media url
instagram_media_response = requests.post(
    instagram_media_request_url, data=instagram_media_payload)
print(instagram_media_response.json())
media_id=instagram_media_response.json()['id']
# media_id="17953640773969028"
isPosted=False
while not isPosted:
    sleep(5)
    instagram_status_url = f'https://graph.facebook.com/v10.0/{media_id}?fields=status_code&access_token={instragram_access_token}'
    instagram_publish_response = requests.get(instagram_status_url)
    print(instagram_publish_response.text)
    if instagram_publish_response.json().get('status_code',False) == 'FINISHED':
        instagram_publish_url = f'https://graph.facebook.com/v10.0/{instagram_user_id}/media_publish'
        # Payload for publish request
        instagram_publish_payload = {
            'creation_id': media_id,
            'access_token': instragram_access_token
        }
        # Send POST request to publish url
        instagram_publish_response = requests.post(
            instagram_publish_url, data=instagram_publish_payload)
        print(instagram_publish_response.json())
        isPosted=True
