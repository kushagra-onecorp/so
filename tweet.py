import base64
import requests


def url_encode(str):
    return str.replace(',', '%20')


def encode_base_64(string):
    sample_string_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


twitter_api_key = 'ie0yFTgq4XwLSBAFOWdBoBIAR'
twitter_api_secret = 'cOicl85MHBFBWGVNVrZWn87RPJs0Fq1OBLsXPO1cgcSxeNyUXO'
twitter_client_id = 'cXFQbG1nQWkybmhrRkFzM25MTzg6MTpjaQ'
twitter_client_secret = 'jMkuH3RssjI_KUVRDKRWK2gA2gEmDK_ALmP_NTtarYQXSqZmtR'
twitter_token = 'AAAAAAAAAAAAAAAAAAAAADsEhQEAAAAAYN2%2FUttYw%2FZlEm1gzJPayCdpa8M%3Dnk39WWxIy9wBO5NvMJe9XoBqVvvVZZZDOUb9Vu0zPcmoAZj721'

redirect_url = 'https://onepost.sasone.in/linked-accounts/twitter/'

twitter_scope = 'tweet.read,tweet.write,users.read,offline.access'

state = 'f'


url = """
https://twitter.com/i/oauth2/authorize?response_type=code&client_id={}&redirect_uri={}&scope={}&state={}&code_challenge=challenge&code_challenge_method=plain
"""

twitter_client_id = 'cXFQbG1nQWkybmhrRkFzM25MTzg6MTpjaQ'
twitter_client_secret = 'jMkuH3RssjI_KUVRDKRWK2gA2gEmDK_ALmP_NTtarYQXSqZmtR'

print(url.format(twitter_client_id, redirect_url, url_encode(twitter_scope), state))

code = input("Enter Twitter Auth Code:")

twitter_access_token_url = "https://api.twitter.com/2/oauth2/token?grant_type=authorization_code&client_id={}&redirect_uri={}&code_verifier=challenge&code={}"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'Basic {encode_base_64( f"{twitter_client_id}:{twitter_client_secret}")}'
}

response = requests.post(twitter_access_token_url.format(
    twitter_client_id, redirect_url, code), headers=headers)

print(response.json())
twitter_acces_token = response.json().get('access_token', '')
print('Acces Token::>>', twitter_acces_token)

header = {
    "Authorization": f'Bearer {twitter_acces_token}'
}
params = {
    "user.fields": "id,location,name,profile_image_url,public_metrics,url,username"
}
twitter_me_url = 'https://api.twitter.com/2/users/me'
response = requests.get(twitter_me_url, params=params, headers=header)
# print(response.json())
profile_image=response.json().get('data','').get('profile_image_url','')
page_name=response.json().get('data','').get('username','')
name=response.json().get('data','').get('name','')
page_id=response.json().get('data','').get('id','')
print("Profile Image::>>",profile_image)
print("Page ID::>>",page_id)
print("Page Name::>>",page_name)
print("Name::>>",name)