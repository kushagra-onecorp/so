import requests

# Access Token from Facebook Graph API
instragram_access_token="EAAUFRLCbo1MBAG36jYRZAXglCkumUbZBWmISO3GojsZA81ZAazEFkX6AJcqGOaxTStAkZAM8YAL2aO05RatdQBRUtiLbrXl8kICy30DqiYiL2TcEmBEoa9ODnSaBstFZCimNswHuvlPeplqjjQNig7jDaOw2bzyjuzF2DcSFZC04gfyPxStSA4kwrPbAeGLpjToYWIfEnv0kN0Q4dwO2uMa"
# Instagram User ID
instagram_user_id='17841453883347404'
# URL of the image to post
image_url='https://wallpaperaccess.com/full/1398313.jpg'
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
instagram_media_payload = {
'image_url': image_url,
'caption':post_text,
'access_token': instragram_access_token
}
#Send POST request to media url
instagram_media_response = requests.post(instagram_media_request_url,data=instagram_media_payload)
print(instagram_media_response.json())

# Instagram Graph API publish URL
instagram_publish_url=f'https://graph.facebook.com/v10.0/{instagram_user_id}/media_publish'
# Payload for publish request
instagram_publish_payload = {
'creation_id':instagram_media_response.json()['id'],
'access_token': instragram_access_token
}

#Send POST request to publish url
instagram_publish_response = requests.post(instagram_publish_url,data=instagram_publish_payload)
print(instagram_media_response.json())