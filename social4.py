import requests
import shutil

# !!! CHANGES
# !!! User URL 82
# !!! User ID Function
# !!! 280 288 296 300

# APP DETAILS
# LinkedIn CLient ID
facebook_client_id = '1413167462458195'
# LinkedIn CLient Secret
facebook_client_secret = '7dc4593de12dfb15e973ff9ef2528f5e'
# LinkedIn CLient ID
linkedin_client_id = '77g7j0cw1gufop'
# LinkedIn CLient Secret
linkedin_client_secret = 'YI0ZnUNymYaJ42az'
# Facebook Redirect URL
facebook_redirect_url = 'https://social.onecorp.co.in/save-credentials/'
# Redirect URL for LinkedIn
linkedin_redirect_url = 'http://localhost:3000/save-credentials/'
# LinkedIn Permission Scopes
linkedin_scope = 'r_emailaddress,r_liteprofile,w_member_social'
# Facebook Permission Scopes
facebook_scope = 'public_profile,email,pages_show_list,instagram_basic,instagram_manage_comments,instagram_manage_insights,instagram_content_publish,pages_read_engagement,pages_manage_posts,pages_read_user_content'

# TOKENS
# Access Token from LinkedIn API
linkedin_access_token = ""
# User Access Token from Facebook Graph API
facebook_user_access_token = ""
# Page Access Token from Facebook Graph API
facebook_page_access_token = """"""


# LinkedIn Authentication Code
facebook_code = ''
# LinkedIn Authentication Code
linkedin_code = ''
# LinkedIn Asset Id
linkedin_asset_id = ''
# Instagram Creation Id
instagram_creation_id = ''


# IDs
# LinkedIn Profile ID
linkedin_profile_id = ''
# Facebook User ID
facebook_user_id = ''
# Facebook Page ID
facebook_page_id = ''
# Instagram User ID
instagram_user_id = ''

# Names
# Name for LinkedIn
linkedin_name = ''
# Name for Facebook
facebook_name = ''

# POST DETAILS
# Post Title
post_title = ''
# Post Description
post_description = """
"""
# Post Text(title+description)
post_text = f"""
{post_title}
{post_description}
"""
# URL of the image to post
image_url = 'https://images.unsplash.com/photo-1604922824961-87cefb2e4b07?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80'
# Image file name for download
image_name = 'post_image.jpg'
# Local Address for Image to post
local_image_url = f'./{image_name}'

# URLs
# API Request URL to get user id
instagram_user_url = f'https://graph.facebook.com/v10.0/{facebook_page_id}?fields=instagram_business_account&access_token={facebook_page_access_token}'
# API Request URL to upload the image
instagram_media_request_url = f'https://graph.facebook.com/v10.0/{instagram_user_id}/media'
# Instagram Graph API publish URL
instagram_publish_url = f'https://graph.facebook.com/v10.0/{instagram_user_id}/media_publish'
# Facebook API Request URL
facebook_request_url = f'https://graph.facebook.com/{facebook_page_id}/photos'
# Facebook Authentication URL
facebook_auth_url = f'https://www.facebook.com/v14.0/dialog/oauth?response_type&client_id={facebook_client_id}&redirect_uri={facebook_redirect_url}&scope={facebook_scope}&response_type=code&state=987654321'
# Facebook Token URL
facebook_token_url = f"https://graph.facebook.com/v14.0/oauth/facebook_page_access_tokeni={facebook_redirect_url}&scope={facebook_scope}&client_id={facebook_client_id}&client_secret={facebook_client_secret}&code={facebook_code}"
# Facebook Me URL
facebook_me_url = 'https://graph.facebook.com/me?fields=id,name'
# Facebook Page Token URL
facebook_page_token_url = f'https://graph.facebook.com/{facebook_user_id}/accounts?access_token={facebook_user_access_token}'
# Facebook Long Page Token URL
facebook_long_token_url = f'https://graph.facebook.com/v14.0/oauth/access_token?grant_type=fb_exchange_token&client_id={facebook_client_id}&client_secret={facebook_client_secret}&fb_exchange_token={facebook_page_access_token}'
# LinkedIn Authentication URL
linkedin_auth_url = f'https://www.linkedin.com/oauth/v2/authorization?response_type=code&state=987654321&scope={linkedin_scope}&client_id={linkedin_client_id}&redirect_uri={linkedin_redirect_url}'
# LinkedIn URL to get token
linkedin_token_url = "https://www.linkedin.com/oauth/v2/accessToken"
# LinkedIn URL to get account info
linkedin_me_url = "https://api.linkedin.com/v2/me"
# LinkedIn API URL to Post
linkedin_url = "https://api.linkedin.com/v2/ugcPosts"
# LinkedIn API URL to Register Media
linkedin_register_url = 'https://api.linkedin.com/v2/assets?action=registerUpload'
# LinkedIn API URL to Upload Image
linkedin_upload_url = ''

# DATA & Headers
# Request payload for Instagram media request
instagram_media_payload = {
    'image_url': image_url,
    'caption': post_text,
    'access_token': facebook_page_access_token
}
# Payload for Instagram publish request
instagram_publish_payload = {
    'creation_id': instagram_creation_id,
    'access_token': facebook_page_access_token
}
# Facebook Request Payload
facebook_post_payload = {
    'message': post_text,
    'url': image_url,
    'access_token': facebook_page_access_token
}
# Facebook Me Payload
facebook_me_payload = {
    'access_token': facebook_user_access_token
}
# Facebook Page ID Payload
facebook_page_id_payload = {
    'access_token': facebook_page_access_token
}
# Request Payload for LinkedIn Authentication
linkedin_auth_body = {
    "grant_type": "authorization_code",
    "code": linkedin_code,
    "redirect_uri": linkedin_redirect_url,
    "client_id": linkedin_client_id,
    "client_secret": linkedin_client_secret,
}
# Request payload for LinkedIn Register
linkedin_register_body = {
    "registerUploadRequest": {
        "recipes": [
            "urn:li:digitalmediaRecipe:feedshare-image"
        ],
        "owner": f"urn:li:person:{linkedin_profile_id}",
        "serviceRelationships": [
            {
                "relationshipType": "OWNER",
                "identifier": "urn:li:userGeneratedContent"
            }
        ]
    }
}
# Request Header for LinkedIn
linkedin_headers = {
    'Authorization': f'Bearer {linkedin_access_token}'
}
# Request payload for LinkedIn Post
linkedin_post_data = {
    "author": f"urn:li:person:{linkedin_profile_id}",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": post_text
            },
            "shareMediaCategory": "IMAGE",
            "media": [
                {
                    "status": "READY",
                    "description": {
                        "text": "Center stage!"
                    },
                    "media": linkedin_asset_id,
                    "title": {
                        "text": "LinkedIn Talent Connect 2021"
                    }
                }
            ]
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

# FUNCTIONS
# ! This function is for debugging purposes


def print_response(resonse, is_json=True):
    """
    This Function Prints the Response it gets
    """
    if(is_json):
        print(resonse.json())
    else:
        print(resonse)


def download_image():
    """
    This Function downloads the image from image_url
    """
    resonse = requests.get(image_url, stream=True)
    image_raw = resonse.raw
    with open(image_name, 'wb') as f:
        shutil.copyfileobj(image_raw, f)
    print(f"Image sucessfully Downloaded:{image_name}")


def save_values(title, description, path, url, facebookToken, linkedinToken):
    """
    This Function saves the values of title, description, file path, image url, facebook access token, linkedin access token and text 
    """
    global post_text, post_description, post_title, local_image_url, image_url, instagram_media_payload, facebook_post_payload, facebook_page_access_token, facebook_page_token_url, linkedin_access_token, linkedin_headers
    post_title = title
    post_description = description
    post_text = f"""{post_title}
    {post_description}"""
    instagram_media_payload['caption'] = post_text
    facebook_post_payload['message'] = post_text
    linkedin_post_data['specificContent']['com.linkedin.ugc.ShareContent']['shareCommentary']['text'] = post_text
    local_image_url = path
    image_url = url
    instagram_media_payload['image_url'] = image_url
    facebook_post_payload['url'] = image_url
    facebook_page_access_token = facebookToken
    facebook_me_payload['access_token'] = facebook_page_access_token
    facebook_page_token_url = f'https://graph.facebook.com/{facebook_user_id}?fields=access_token&access_token={facebook_user_access_token}&scope={facebook_scope}'
    linkedin_access_token = linkedinToken
    linkedin_headers['Authorization'] = f'Bearer {linkedin_access_token}'
    print('-------Saved Values DONE-------')


def facebook_get_code(code):
    """
    This Function Recieves the facebook_code and then saves it
    """
    global facebook_code, facebook_token_url
    facebook_code = code
    facebook_token_url = f"https://graph.facebook.com/v14.0/oauth/access_token?redirect_uri={facebook_redirect_url}&scope={facebook_scope}&client_id={facebook_client_id}&client_secret={facebook_client_secret}&code={facebook_code}"
    print('-------Facebook Authentication Code-DONE-------')


def facebook_get_user_auth():
    """
    This Function calls the facebook Authentication api to get User Access Token
    """
    global facebook_user_access_token, facebook_page_token_url
    facebook_token_response = requests.get(facebook_token_url)
    facebook_user_access_token = facebook_token_response.json()['access_token']
    facebook_me_payload['access_token'] = facebook_user_access_token
    facebook_page_token_url = f'https://graph.facebook.com/{facebook_user_id}?fields=access_token&access_token={facebook_user_access_token}&scope={facebook_scope}'
    print('-------Facebook User Authentication DONE-------')


def facebook_get_user_id():
    """
    This Function gets the facebook_user_id
    """
    global facebook_user_id, facebook_page_token_url, facebook_name
    facebook_me_response = requests.get(facebook_me_url,  facebook_me_payload)
    facebook_user_id = facebook_me_response.json()['id']
    facebook_name = facebook_me_response.json()['name']
    facebook_page_token_url = f'https://graph.facebook.com/{facebook_user_id}?fields=access_token&access_token={facebook_user_access_token}&scope={facebook_scope}'
    print('-------Facebook User ID DONE-------')


def facebook_page_auth():
    """
    This Function gets the facebook_page_access_token
    """
    global facebook_page_access_token, facebook_page_id_payload, instagram_media_payload, instagram_publish_payload, facebook_post_payload, facebook_long_token_url
    facebook_page_response = requests.get(facebook_page_token_url)
    facebook_page_access_token = facebook_page_response.json()[
        'data'][0]['access_token']
    facebook_page_id_payload['access_token'] = facebook_page_access_token
    facebook_post_payload['access_token'] = facebook_page_access_token
    instagram_publish_payload['access_token'] = facebook_page_access_token
    instagram_media_payload['access_token'] = facebook_page_access_token
    facebook_long_token_url = f'https://graph.facebook.com/v14.0/oauth/access_token?grant_type=fb_exchange_token&client_id={facebook_client_id}&client_secret={facebook_client_secret}&fb_exchange_token={facebook_page_access_token}'
    print('-------Facebook Page Authentication DONE-------')


def facebook_get_page_id():
    """
    This Function gets the facebook_page_id
    """
    global facebook_page_id, facebook_request_url, instagram_user_url
    facebook_me_response = requests.get(facebook_me_url,  facebook_me_payload)
    facebook_page_id = facebook_me_response.json()['id']
    facebook_request_url = f'https://graph.facebook.com/{facebook_page_id}/photos'
    instagram_user_url = f'https://graph.facebook.com/v10.0/{facebook_page_id}?fields=instagram_business_account&access_token={facebook_page_access_token}'
    print('-------Facebook Page ID DONE-------')


def facebook_get_long_token():
    """
    This Function exchanges Short Lived Token with a Long Lived Token
    """
    global facebook_page_access_token, facebook_page_id_payload, instagram_media_payload, instagram_publish_payload, facebook_post_payload, facebook_long_token_url, instagram_user_url
    facebook_long_response = requests.get(facebook_long_token_url)
    facebook_page_access_token = facebook_long_response.json()['access_token']
    facebook_page_id_payload['access_token'] = facebook_page_access_token
    facebook_post_payload['access_token'] = facebook_page_access_token
    instagram_publish_payload['access_token'] = facebook_page_access_token
    instagram_media_payload['access_token'] = facebook_page_access_token
    facebook_long_token_url = f'https://graph.facebook.com/v14.0/oauth/access_token?grant_type=fb_exchange_token&client_id={facebook_client_id}&client_secret={facebook_client_secret}&fb_exchange_token={facebook_page_access_token}'
    instagram_user_url = f'https://graph.facebook.com/v10.0/{facebook_page_id}?fields=instagram_business_account&access_token={facebook_page_access_token}'
    print('-------Facebook Page Long Token DONE-------')


def post_facebook():
    """
    This Function Posts the data to Facebook
    """
    # Send POST request to Facebook API
    facebook_resonse = requests.post(
        facebook_request_url, data=facebook_post_payload)
    # print_response(facebook_resonse)
    print('-------Facebook Post-DONE-------')


def instagram_get_user_id():
    """
    This Function gets the Instagram User ID
    """
    global instagram_user_id
    instagram_user_id_response = requests.get(instagram_user_url)
    instagram_user_id = instagram_user_id_response.json()[
        'instagram_business_account']['id']


def instagram_media_post():
    """
    This Function uploads the image to Instagram
    """
    global instagram_creation_id, instagram_publish_payload
    # Send POST request to media url
    instagram_media_response = requests.post(
        instagram_media_request_url, data=instagram_media_payload)
    # print_response(instagram_media_response)
    print('-------Image Upload Instagram-DONE-------')
    instagram_creation_id = instagram_media_response.json()['id']
    instagram_publish_payload['creation_id'] = instagram_creation_id


def post_instagram():
    """
    This Function Posts the data to Instagram
    it uses the creation_id returned from instagram_media_post to attach image
    """
    instagram_publish_response = requests.post(
        instagram_publish_url, data=instagram_publish_payload)
    # print_response(instagram_publish_response)
    print('-------Instagram Post-DONE-------')


def linkedin_get_code(code):
    """
    This Function Recieves the linkedin_code and then saves it
    """
    global linkedin_code, linkedin_auth_body
    linkedin_code = code
    linkedin_auth_body['code'] = linkedin_code
    print('-------LinkedIn Authentication Code-DONE-------')


def linkedin_authenticate():
    """
    This Function Uses the code and then gets the access token
    """
    global linkedin_access_token, linkedin_headers
    print('Linkedin Body', linkedin_auth_body)
    print('Linkedin Code:'+linkedin_code)
    linkedin_token_response = requests.post(
        linkedin_token_url, data=linkedin_auth_body)
    print(linkedin_token_response.json())
    linkedin_access_token = linkedin_token_response.json()["access_token"]
    linkedin_headers['Authorization'] = f'Bearer {linkedin_access_token}'
    # print(linkedin_access_token)
    print('-------LinkedIn Authentication-DONE-------')


def linkedin_get_id():
    """
    This Function Gets LinkedIn Profile ID
    """
    global linkedin_profile_id, linkedin_name
    linkedin_me_response = requests.get(
        linkedin_me_url, headers=linkedin_headers)
    print(linkedin_me_response.json())
    linkedin_profile_id = linkedin_me_response.json()['id']
    linkedin_name = f"{linkedin_me_response.json()['localizedFirstName']} {linkedin_me_response.json()['localizedLastName']}"
    linkedin_register_body["registerUploadRequest"][
        'owner'] = f"urn:li:person:{linkedin_profile_id}"
    linkedin_post_data['author'] = f"urn:li:person:{linkedin_profile_id}"
    print(linkedin_register_body, "============")
    print(linkedin_post_data, "===========")
    print('-------LinkedIn Profile ID-DONE-------')


def linkedin_register():
    """
    This Function calls the register API from LinkedIn to get asset_id and upload_url
    """
    global linkedin_asset_id, linkedin_upload_url, linkedin_post_data
    linkedin_register_response = requests.post(
        linkedin_register_url, headers=linkedin_headers, json=linkedin_register_body)
    print_response(linkedin_register_response)
    print('-------LinkedIn Register-DONE-------')
    linkedin_upload_url = linkedin_register_response.json(
    )['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']
    linkedin_asset_id = linkedin_register_response.json()['value']['asset']
    linkedin_post_data["specificContent"]["com.linkedin.ugc.ShareContent"]["media"][0]["media"] = linkedin_asset_id


def linkedin_upload_image():
    """
    This Function uploads the image to LinkedIn using the upload_url returned by linkedin_register
    """
    linkedin_image = open(local_image_url, 'rb')
    linkedin_upload_response = requests.put(
        linkedin_upload_url, data=linkedin_image, headers=linkedin_headers)
    print(linkedin_upload_response)
    print('-------Image Upload LinkedIn-DONE-------')


def post_linkedin():
    """
    This Function posts the data to LinkedIn 
    It uses the asset_id returned by linkedin_register to attach image
    """
    linkedin_post_response = requests.post(
        linkedin_url, headers=linkedin_headers, json=linkedin_post_data)
    print_response(linkedin_post_response)
    print('-------LinkedIn Post-DONE-------')


def authenticate_linkedin():
    """
    This Function calls necessary functions to Authenticate with LinkedIn
    """
    linkedin_authenticate()


def authenticate_facebook():
    """
    This Function calls necessary functions to Authenticate on Facebook
    """
    facebook_get_code()
    facebook_get_user_auth()
    facebook_get_user_id()
    facebook_page_auth()
    facebook_get_page_id()
    facebook_get_long_token()


def make_post_facebook():
    """
    This Function calls necessary functions to make a Facebook post
    """
    facebook_get_page_id()
    post_facebook()


def make_post_instagram():
    """
    This Function calls necessary functions to make a Instagram post
    """
    instagram_media_post()
    post_instagram()


def make_post_linkedin():
    """
    This Function calls necessary functions to make a LinkedIn post
    """
    linkedin_get_id()
    linkedin_register()
    linkedin_upload_image()
    post_linkedin()


def make_posts(facebookToken, linkedinToken, title, description, path, url, socials):
    """
    This Function Calls the other social functions to make post
    """
    save_values(title, description, path, url, facebookToken, linkedinToken)
    if('facebook' in socials):
        make_post_facebook()
    if('instagram' in socials):
        make_post_instagram()
    if('linkedin' in socials):
        make_post_linkedin()


def authenticate_social(linkedinCode, facebookCode):
    """
    This Function Calls functions to authenticate users
    Args:
        linkedinCode (string): LinkedIn Authentication Token Generated Using OAuth
        facebookCode (string): Facebook Authentication Token Generated Using OAuth
    """
    if linkedinCode:
        linkedin_get_code(linkedinCode)
        authenticate_linkedin()
    if facebookCode:
        facebook_get_code(facebookCode)
        authenticate_facebook()
    return [linkedin_access_token, facebook_page_access_token, facebook_page_id, linkedin_profile_id, linkedin_name, facebook_name]
