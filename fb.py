import json
import requests

# Access Token from Facebook Graph API
facebook_access_token="EAAUFRLCbo1MBAD2tiZBY8IgGIOTJ7PqkZB77ojOzqU3YsU3vONrgd8hAfgL5g3pZAAzKBKiBTv8G0RpxFBrZBhN5Gi1vNiFtBL5VCTQo4V5D9DcFxm54ImP1PLssRw4pBNmUEwIb3ATbpPW51ZCqY1OvZBNFiDapwmpfvr8EQ0rK5EmlE6WZByn"
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
