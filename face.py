import requests

# !!! FOR THIS WE NEED TO GET THE APP APROOVED

facebook_client_id='1413167462458195'
facebook_client_secret='7dc4593de12dfb15e973ff9ef2528f5e'
facebook_redirect_url='https://social.onecorp.co.in/save-credentials/'

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
facebook_scope='public_profile,email,pages_show_list,instagram_basic,instagram_manage_comments,instagram_manage_insights,instagram_content_publish,pages_read_engagement,pages_manage_posts,pages_read_user_content'

facebook_auth_url=f'https://www.facebook.com/v14.0/dialog/oauth?response_type&client_id={facebook_client_id}&redirect_uri={facebook_redirect_url}&scope={facebook_scope}&response_type=code&state=987654321&mode=facebook'

print(f'Auth URL:{facebook_auth_url}')
print('-------------------------------------')
facebook_code=input("Enter The Code:")
print('-------------------------------------')

facebook_token_url=f"https://graph.facebook.com/v14.0/oauth/access_token?redirect_uri={facebook_redirect_url}&scope={facebook_scope}&client_id={facebook_client_id}&client_secret={facebook_client_secret}&code={facebook_code}"

facebook_token_response=requests.get(facebook_token_url)
print('Response Token')
print(facebook_token_response.json())
print('-------------------------------------')

facebook_user_access_token=facebook_token_response.json()['access_token']
print('Response User Access')
print(facebook_user_access_token)
print('-------------------------------------')

facebook_me_payload={
'access_token': facebook_user_access_token
}
facebook_me_url='https://graph.facebook.com/me?fields=id,name'
facebook_me_response=requests.get(facebook_me_url,facebook_me_payload)
print(facebook_me_response.json()['name'])
facebook_user_id=facebook_me_response.json()['id']
print('Response User ID')
print(facebook_user_id)
print('-------------------------------------')

page_token_url = f'https://graph.facebook.com/{facebook_user_id}/accounts?access_token={facebook_user_access_token}'
facebook_page_response=requests.get(page_token_url)
print('Response Page Token')
print(facebook_page_response.json())
print('-------------------------------------')

if len(facebook_page_response.json()['data']) > 0:
    facebook_page_access_token=facebook_page_response.json()['data'][0]['access_token']

if facebook_page_access_token:
    facebook_page_id_payload={
    'access_token': facebook_page_access_token
    }
    facebook_page_id_response=requests.get(facebook_me_url,facebook_page_id_payload)
    page_id=facebook_page_id_response.json()['id']
    print('Response Page ID')
    print(page_id)
    print('-------------------------------------')

facebook_long_token_url=f'https://graph.facebook.com/v14.0/oauth/access_token?grant_type=fb_exchange_token&client_id={facebook_client_id}&client_secret={facebook_client_secret}&fb_exchange_token={facebook_page_access_token}'
facebook_long_response=requests.get(facebook_long_token_url)
facebook_long_response.json()['access_token']
print('Response Long Token')
print(facebook_long_response.json())
print('-------------------------------------')
