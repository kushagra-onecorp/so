import json
import requests

# Access Token from Facebook Graph API
facebook_access_token="EAAUFRLCbo1MBAAOGRYE9Uju7W9iUZBScmL1CaBvO96JyJqX2L5ajM7h4HxpOKtlcxOZC6wRqedPSPiZC9GhEeL4et61NNjXNuUupLUhpD4X4tt0thyFLZCol9d9I5OMfr0UFxhjaZAZBYlxEUACgoq00mMYQjGWkLenujQw9S0Vo0wz3lMkZClA"
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
image_url='https://wallpaperaccess.com/full/1398313.jpg'
image2='https://images.unsplash.com/photo-1453728013993-6d66e9c9123a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80'
facebook_photo_upload_url=f'https://graph.facebook.com/v14.0/{facebook_page_id}/photos'
facebook_upload_body1={
        'url':image_url,
        'published':'false',
        'access_token':facebook_access_token
        }
facebook_upload_body2={
        'url':image2,
        'published':'false',
        'access_token':facebook_access_token
        }
print(facebook_photo_upload_url)
print(facebook_upload_body1)
print(facebook_upload_body2)
facebook_image1= requests.post(facebook_photo_upload_url,data=facebook_upload_body1)
print(facebook_image1.text)
facebook_image2= requests.post(facebook_photo_upload_url,data=facebook_upload_body2)
print(facebook_image2.text)
# Facebook API Request URL
facebook_request_url = f'https://graph.facebook.com/{facebook_page_id}/feed'
# Facebook Request Payload
facebook_post_payload = {
'message':post_text,
'attached_media':json.dumps([
        {'media_fbid':facebook_image1.json()['id']},
        {'media_fbid':facebook_image2.json()['id']}]),
'access_token': facebook_access_token
}
print(facebook_request_url)
print(facebook_post_payload)
#Send POST request to Facebook API
facebook_resonse = requests.post(facebook_request_url,data=facebook_post_payload)

print(facebook_resonse.json())
