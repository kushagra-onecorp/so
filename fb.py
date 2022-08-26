import json
import requests

# Access Token from Facebook Graph API
facebook_access_token="EAAUFRLCbo1MBAFBqn8NWk3UWe1ZA5GUIIvleMmSZCfRa4f7oc4l6X99NNuHtbrmKQFFPi5Ofjviz3SiW3YFboptnPJjMSQ6uuvZBZBkcbj7lGnA2o5x26ooY38mFavZANbrKw7KtwFQo8NVWHzASCXWDck82M1EUghzYNfhh2Ij9y9gpXY5YN"
# Facebook Page ID
facebook_page_id='102068252597979'
# Post Title
post_title='Post Title'
# Post Description
post_description='Post Description'
# Post Text(title+description)
post_text=f"""
{post_title}
{post_description}
"""
# URL of the image to post
images_url=['https://wallpaperaccess.com/full/1398313.jpg','https://wallpaperaccess.com/full/1388313.jpg','https://wallpaperaccess.com/full/1398213.jpg']
facebook_photo_upload_url=f'https://graph.facebook.com/v14.0/{facebook_page_id}/photos'
media_ids=[]
for img in images_url:
        facebook_upload_body={
                'url':img,
                'published':'false',
                'access_token':facebook_access_token
                }
        print(facebook_photo_upload_url)
        print(facebook_upload_body)
        facebook_image= requests.post(facebook_photo_upload_url,data=facebook_upload_body)
        print(facebook_image.text)
        media_ids.append(facebook_image.json()['id'])
attached_medias=[{'media_fbid':id} for id in media_ids]
# Facebook API Request URL
facebook_request_url = f'https://graph.facebook.com/{facebook_page_id}/feed'
# Facebook Request Payload
facebook_post_payload = {
'message':post_text,
'attached_media':json.dumps(attached_medias),
'access_token': facebook_access_token
}
print(facebook_request_url)
print(facebook_post_payload)
#Send POST request to Facebook API
facebook_resonse = requests.post(facebook_request_url,data=facebook_post_payload)

print(facebook_resonse.json())
