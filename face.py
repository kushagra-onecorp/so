import requests

# !!! FOR THIS WE NEED TO GET THE APP APROOVED

facebook_client_id = '651883032773236'
# LinkedIn CLient Secret
facebook_client_secret = '95ddc60f72d27b8cf31a5cac74de32dd'
facebook_redirect_url = 'https://onepost.sasone.in/linked-accounts/facebook/'

# ! NEEDED PERMISSIONS
# ? public_profile
# ? instagram_basic
# ? instagram_manage_comments
# ? instagram_manage_insights
# ? instagram_content_publish
# ? pages_read_engagement
# ? pages_read_user_content
# ? pages_show_list
# ? pages_manage_posts
facebook_scope = 'public_profile,email,pages_show_list,instagram_basic,instagram_manage_comments,instagram_manage_insights,instagram_content_publish,pages_read_engagement,pages_manage_posts,pages_read_user_content,publish_video'

facebook_auth_url = f'https://www.facebook.com/v14.0/dialog/oauth?response_type&client_id={facebook_client_id}&redirect_uri={facebook_redirect_url}&scope={facebook_scope}&response_type=code&state=987654321&mode=facebook'

print(f'Auth URL:{facebook_auth_url}')
print('-------------------------------------')
facebook_code = input("Enter The Code:")
print('-------------------------------------')

facebook_token_url = f"https://graph.facebook.com/v14.0/oauth/access_token?redirect_uri={facebook_redirect_url}&scope={facebook_scope}&client_id={facebook_client_id}&client_secret={facebook_client_secret}&code={facebook_code}"

facebook_token_response = requests.get(facebook_token_url)
print('Response Token')
print(facebook_token_response.json())
print('-------------------------------------')

facebook_user_access_token = facebook_token_response.json()['access_token']
print('Response User Access')
print(facebook_user_access_token)
print('-------------------------------------')

facebook_me_payload = {
    'access_token': facebook_user_access_token
}
facebook_me_url = 'https://graph.facebook.com/me?fields=id,name'
facebook_me_response = requests.get(facebook_me_url, facebook_me_payload)
print(facebook_me_response.json()['name'])
facebook_user_id = facebook_me_response.json()['id']
print('Response User ID')
print(facebook_user_id)
print('-------------------------------------')

page_token_url = f'https://graph.facebook.com/{facebook_user_id}/accounts?access_token={facebook_user_access_token}'
facebook_page_response = requests.get(page_token_url)
print('Response Page Token')
print(facebook_page_response.json())
print('-------------------------------------')

if len(facebook_page_response.json()['data']) > 0:
    facebook_page_access_token = facebook_page_response.json()[
        'data'][0]['access_token']

if facebook_page_access_token:
    facebook_page_id_payload = {
        'access_token': facebook_page_access_token
    }
    facebook_page_id_response = requests.get(
        facebook_me_url, facebook_page_id_payload)
    page_id = facebook_page_id_response.json()['id']
    print('Response Page ID')
    print(page_id)
    print('-------------------------------------')

facebook_long_token_url = f'https://graph.facebook.com/v14.0/oauth/access_token?grant_type=fb_exchange_token&client_id={facebook_client_id}&client_secret={facebook_client_secret}&fb_exchange_token={facebook_page_access_token}'
facebook_long_response = requests.get(facebook_long_token_url)
facebook_long_response.json()['access_token']
print('Response Long Token')
print(facebook_long_response.json())
facebook_page_access_token = facebook_long_response.json()['access_token']
print(facebook_page_access_token)
print('-------------------------------------')
instagram_user_url = 'https://graph.facebook.com/v10.0/{}?fields=instagram_business_account&access_token={}'
instagram_credentials = []
instagram_user_id_response = requests.get(
    instagram_user_url.format(page_id, facebook_page_access_token))
print('*****IG USer', instagram_user_id_response.text)
print('*****IG USer', instagram_user_id_response.json())
user_id = instagram_user_id_response.json()['instagram_business_account']['id']
user_name_url = 'https://graph.facebook.com/v14.0/{}?access_token={}&fields=id,media_count,username'
instagram_username_response = requests.get(
    user_name_url.format(user_id, facebook_page_access_token))
print("**********iguser resp", instagram_username_response.text)
print("**********iguser resp", instagram_username_response.json())
print("**********iguser resp", instagram_username_response.json()['username'])
print("---Instagram Authentication Is Done-----------")
