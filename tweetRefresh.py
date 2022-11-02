import base64
import requests


def url_encode(str):
    return str.replace(',', '%20')


def encode_base_64(string):
    sample_string_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


twitter_client_id = 'cXFQbG1nQWkybmhrRkFzM25MTzg6MTpjaQ'
twitter_client_secret = 'jMkuH3RssjI_KUVRDKRWK2gA2gEmDK_ALmP_NTtarYQXSqZmtR'

refresh_token = input("Enter Twitter Auth Refresh Token:")

twitter_refresh_access_token_url = "https://api.twitter.com/2/oauth2/token?grant_type=refresh_token&client_id={}&refresh_token={}"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'Basic {encode_base_64( f"{twitter_client_id}:{twitter_client_secret}")}'
}

response = requests.post(twitter_refresh_access_token_url.format(
    twitter_client_id, refresh_token), headers=headers)

if response.json().get('error', False):
    print("Error:>>")
    print(response.json())
    exit()

print('Response::>>', response.json())
twitter_access_token = response.json().get('access_token', '')
print('Acces Token::>>', twitter_access_token)

header = {
    "Authorization": f'Bearer {twitter_access_token}'
}
params = {
    "user.fields": "id,location,name,profile_image_url,public_metrics,url,username"
}
twitter_me_url = 'https://api.twitter.com/2/users/me'
response = requests.get(twitter_me_url, params=params, headers=header)
# print(response.json())
profile_image = response.json().get('data', '').get('profile_image_url', '')
page_name = response.json().get('data', '').get('username', '')
name = response.json().get('data', '').get('name', '')
page_id = response.json().get('data', '').get('id', '')
print("Profile Image::>>", profile_image)
print("Page ID::>>", page_id)
print("Page Name::>>", page_name)
print("Name::>>", name)
