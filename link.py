import requests

linkedin_client_id = '78l55cr29sl11s'
linkedin_client_secret = 'gR78hqshNl4dimkc'

redirect_url = 'https://onepost.sasone.in/linked-accounts/linkedin/'

linkedin_scope = 'r_emailaddress,r_liteprofile,w_member_social'

linkedin_auth_url = f'https://www.linkedin.com/oauth/v2/authorization?response_type=code&state=987654321&scope={linkedin_scope}&client_id={linkedin_client_id}&redirect_uri={redirect_url}'
print(linkedin_auth_url)
linkedin_code = input("Enter The Code:")
linkedin_auth_body = {
    "grant_type": "authorization_code",
    "code": linkedin_code,
    "redirect_uri": redirect_url,
    "client_id": linkedin_client_id,
    "client_secret": linkedin_client_secret,
}
linkedin_token_url = "https://www.linkedin.com/oauth/v2/accessToken"
linkedin_token_response = requests.post(
    linkedin_token_url, data=linkedin_auth_body)
print(linkedin_token_response.json())
linkedin_headers = {
    'Authorization': f'Bearer {linkedin_token_response.json()["access_token"]}'
}
linkedin_me_url = "https://api.linkedin.com/v2/me"
linkedin_me_response = requests.get(linkedin_me_url, headers=linkedin_headers)
print(linkedin_me_response.json())
print(linkedin_me_response.json()['localizedFirstName'])
print(linkedin_me_response.json()['localizedLastName'])
linkedin_profile_id = linkedin_me_response.json()['id']
print(linkedin_profile_id)
