import requests

# Access Token from Facebook Graph API
instragram_access_token="EAAUFRLCbo1MBAAOGRYE9Uju7W9iUZBScmL1CaBvO96JyJqX2L5ajM7h4HxpOKtlcxOZC6wRqedPSPiZC9GhEeL4et61NNjXNuUupLUhpD4X4tt0thyFLZCol9d9I5OMfr0UFxhjaZAZBYlxEUACgoq00mMYQjGWkLenujQw9S0Vo0wz3lMkZClA"
# Instagram User ID
instagram_user_id='17841453883347404'
# URL of the image to post
image_url='https://wallpaperaccess.com/full/1398313.jpg'
image2='https://images.unsplash.com/photo-1453728013993-6d66e9c9123a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80'
# Post Title
post_title='Post Title'
# Post Description
post_description='Post Description'
# Post Text(title+description)
post_text=f"""
{post_title}
{post_description}
"""
# API Request URL to upload the image
instagram_media_request_url = f'https://graph.facebook.com/v10.0/{instagram_user_id}/media'
# Request payload for media request
instagram_media_payload1 = {
'image_url': image_url,
'caption':post_text,
'is_carousel_item':'true',
'access_token': instragram_access_token
}
instagram_media_payload2 = {
'image_url': image2,
'caption':post_text,
'is_carousel_item':'true',
'access_token': instragram_access_token
}
#Send POST request to media url
instagram_media_response1 = requests.post(instagram_media_request_url,data=instagram_media_payload1)
print(instagram_media_response1.json())
instagram_media_response2 = requests.post(instagram_media_request_url,data=instagram_media_payload2)
print(instagram_media_response2.json())


instagram_media_payload3 = {
'media_type': 'CAROUSEL',
'caption':post_text,
'children':','.join([instagram_media_response1.json()['id'],instagram_media_response2.json()['id']]),
'access_token': instragram_access_token
}
instagram_media_response3 = requests.post(instagram_media_request_url,data=instagram_media_payload3)
print(instagram_media_response3.json())
# Instagram Graph API publish URL
instagram_publish_url=f'https://graph.facebook.com/v10.0/{instagram_user_id}/media_publish'
# Payload for publish request
instagram_publish_payload = {
'creation_id':instagram_media_response3.json()['id'],
'access_token': instragram_access_token
}

#Send POST request to publish url
instagram_publish_response = requests.post(instagram_publish_url,data=instagram_publish_payload)
print(instagram_media_response1.json())