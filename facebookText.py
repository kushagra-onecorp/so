import json
import requests


facebook_access_token="EAAJQ4liagnQBAO3UOHIfuExtsri4EoXKX9gINz846YnM2qwrt35UIsygfcbZBEaHTbWZCxt3IQJOl7WXSoydWfl8TVAW0Rh57q5VZBoHUMDy3jqDssNuN1ztRDzWTXK9PvZAqqojh5EsS4TWebHPfqlGksHOoytgc212hZA2KQD2jvAUszBKt"
facebook_page_id= "103995469037355"

# Post Description
post_text='Post Description'

# Facebook API Request URL
facebook_request_url = f'https://graph.facebook.com/{facebook_page_id}/feed'
# Facebook Request Payload
facebook_post_payload = {
'message':post_text,
'access_token': facebook_access_token
}
print(facebook_request_url)
print(facebook_post_payload)
#Send POST request to Facebook API
facebook_resonse = requests.post(facebook_request_url,data=facebook_post_payload)

print(facebook_resonse.json())
