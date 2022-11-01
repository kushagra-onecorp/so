import json
import os
import requests

twitter_access_token = "RVdYTUFRbG9sN2hBV3BYdDJ6bWw1cFhiY1BJUHc0TU5sSGFXak9OM0NMNXI4OjE2NjcxOTI2NjQzNTY6MTowOmF0OjE"

upload_url = 'https://upload.twitter.com/1.1/media/upload.json'

images_url = ['./images/post_image.jpg']

file = open(images_url[0], 'rb')
data = file.read()
resource_url = 'https://upload.twitter.com/1.1/media/upload.json'
upload_image = {
    'media': data,
}
post_data = {
    'media_category': 'tweet_image'
}
image_headers = {
    'Authorization': 'Bearer {}'.format(twitter_access_token)
}


media_id = requests.post(
    resource_url, headers=image_headers, params=post_data, files=upload_image)

print(media_id)
print(media_id.text)
# header = {
#     "Authorization": f'Bearer {twitter_access_token}',
#     "Content-type": "application/json"
# }
# post_payload = {
#     "text": post_text
#     }

# print(json.dumps(post_payload))
# response = requests.post(
#     post_url, data=json.dumps(post_payload), headers=header)
# print(response)
# print(response.text)
# print(response.json())
