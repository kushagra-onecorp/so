import requests

# Access Token from Facebook Graph API
facebook_access_token="EAAUFRLCbo1MBAG36jYRZAXglCkumUbZBWmISO3GojsZA81ZAazEFkX6AJcqGOaxTStAkZAM8YAL2aO05RatdQBRUtiLbrXl8kICy30DqiYiL2TcEmBEoa9ODnSaBstFZCimNswHuvlPeplqjjQNig7jDaOw2bzyjuzF2DcSFZC04gfyPxStSA4kwrPbAeGLpjToYWIfEnv0kN0Q4dwO2uMa"
# Facebook Page ID
facebook_page_id='103995469037355'
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
# Facebook API Request URL
facebook_request_url = f'https://graph.facebook.com/{facebook_page_id}/photos'
# Facebook Request Payload
facebook_post_payload = {
'message':post_text,
'url': image_url,
'access_token': facebook_access_token
}

#Send POST request to Facebook API
facebook_resonse = requests.post(facebook_request_url,data=facebook_post_payload)

print(facebook_resonse.json())
