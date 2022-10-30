
import requests

access_token = 'YmhmazQ0YS1RRzNHLWlYU2VzaXlaRlRYbC1ZYi1pamFtczFYT3lPZXMyZ1dROjE2NjcxMzMwMzM0MDE6MTowOmF0OjE'

file = open('./images/artronaut.jpg', 'rb')
data = file.read()
resource_url = 'https://upload.twitter.com/1.1/media/upload.json'
upload_image = {
    'media': data,
    'media_category': 'tweet_image'
}
post_data = {
}
image_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}


media_id = requests.post(
    resource_url, headers=image_headers, params=post_data, data=upload_image)

print(media_id)
print(media_id.text)
