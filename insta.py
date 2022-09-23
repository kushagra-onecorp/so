import requests

# Access Token from Facebook Graph API
instragram_access_token="EAALefOGyJXQBAAMJUr7iNYEZAmUcyJA5u3HSXjMMPIZBj1IDWBKBtN9ZAhM87hF5gzLDJI1tKV4fbTDqFn0tZAiiLzlTmfpCiZA2EamuLG21XRtMiSYhJEhiJVWZALVybb1RGR1pmozUJU5B9bXJEaeX381pCr0KYy4NZBnTss2qWvHG0FLaP5FhaJT8lEep3Fp1n2KkJzemd0OJKhnaPU3YuwwkdI5M5LrZAuhnuDT6ZAgZDZD"
# Instagram User ID
instagram_user_id='17841453883347404'
# URL of the image to post
images_url=['https://wallpaperaccess.com/full/1398313.jpg','https://wallpaperaccess.com/full/1388313.jpg','https://wallpaperaccess.com/full/1398213.jpg']
# Post Title
post_title='Post Title'
# Post Description
post_description='Post Description'
# Post Text(title+description)
post_text=f"""
{post_title}
{post_description}
"""
media_ids=[]
# API Request URL to upload the image
instagram_media_request_url = f'https://graph.facebook.com/v10.0/{instagram_user_id}/media'
for img in images_url:
    # Request payload for media request
    instagram_media_payload = {
    'image_url': img,
    'caption':post_text,
    'is_carousel_item':'true',
    'access_token': instragram_access_token
    }
    #Send POST request to media url
    instagram_media_response = requests.post(instagram_media_request_url,data=instagram_media_payload)
    print(instagram_media_response.json())
    media_ids.append(instagram_media_response.json()['id'])
instagram_carousel_payload = {
'media_type': 'CAROUSEL',
'caption':post_text,
'children':','.join(media_ids),
'access_token': instragram_access_token
}
instagram_carousel_response = requests.post(instagram_media_request_url,data=instagram_carousel_payload)
print(instagram_carousel_response.json())
# Instagram Graph API publish URL
instagram_publish_url=f'https://graph.facebook.com/v10.0/{instagram_user_id}/media_publish'
instagram_carousel_id=instagram_carousel_response.json()['id']
# Payload for publish request
instagram_publish_payload = {
'creation_id':instagram_carousel_id,
'access_token': instragram_access_token
}
#Send POST request to publish url
instagram_publish_response = requests.post(instagram_publish_url,data=instagram_publish_payload)
print(instagram_media_response.json())