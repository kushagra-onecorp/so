import requests;

facebook_client_id = '1413167462458195'
facebook_client_secret = '7dc4593de12dfb15e973ff9ef2528f5e'
instagram_redirect_url = 'https://onepost.sasone.in/linked-accounts/facebook/'


instagram_scopes = 'user_profile,user_media'

instagram_auth_url = f'https://api.instagram.com/oauth/authorize?client_id={facebook_client_id}&redirect_uri={instagram_redirect_url}&scope={instagram_scopes}&response_type=code&state=instagram'

print(f'Auth URL:{instagram_auth_url}')
print('-------------------------------------')
instagram_code = input("Enter The Code:")
print('-------------------------------------')

instagram_token_url = f"https://api.instagram.com/oauth/access_token"

instagram_token_body={
    'client_id':facebook_client_id,
    'client_secret':facebook_client_secret,
    'code':instagram_code,
    'grant_type':'authorization_code',
    'redirect_uri':instagram_redirect_url,
}

instagram_token_response = requests.post(instagram_token_url)
print('Response Token')
print(instagram_token_response.json())
print('-------------------------------------')

instagram_user_access_token = instagram_token_response.json()['access_token']
print('Response User Access')
print(instagram_user_access_token)
print('-------------------------------------')

instagram_user_id = instagram_token_response.json()['user_id']
print('Response User ID')
print(instagram_user_id)
print('-------------------------------------')

instagram_long_token_url = f'https://graph.facebook.com/v14.0/oauth/access_token?grant_type=fb_exchange_token&client_id={facebook_client_id}&client_secret={facebook_client_secret}&fb_exchange_token={instagram_user_access_token}'
instagram_long_response = requests.get(instagram_long_token_url)
instagram_long_response.json()['access_token']
print('Response Long Token')
print(instagram_long_response.json())