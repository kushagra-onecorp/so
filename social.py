import requests

# APP DETAILS
# LinkedIn CLient ID
facebook_client_id = '1413167462458195'
# LinkedIn CLient Secret
facebook_client_secret = '7dc4593de12dfb15e973ff9ef2528f5e'
# LinkedIn CLient ID
linkedin_client_id = '78l55cr29sl11s'
# LinkedIn CLient Secret
linkedin_client_secret = 'gR78hqshNl4dimkc'
# Base URL
BASE_URL='https://onepost.sasone.in'
# Base Redirect URL
BASE_REDIRECT_URL=f'{BASE_URL}/linked-accounts'
# Facebook Redirect URL
facebook_redirect_url = f'{BASE_REDIRECT_URL}/facebook/'
# Redirect URL for LinkedIn
linkedin_redirect_url = f'{BASE_REDIRECT_URL}/linkedin/'
# LinkedIn Permission Scopes
linkedin_scopes = 'r_emailaddress,r_liteprofile,w_member_social'
# Facebook Permission Scopes
facebook_scopes = 'read_insights,public_profile,email,pages_show_list,instagram_basic,instagram_manage_comments,instagram_manage_insights,instagram_content_publish,pages_read_engagement,pages_manage_posts,pages_read_user_content'

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

# Facebook Post ID
facebook_post_id = ''
# Instagram Post ID
instagram_post_id = ''
# LinkedIn Post ID
linkedin_post_id = ''

# Names
# Name for LinkedIn
linkedin_name = ''
# Name for Facebook
facebook_name = ''
# POST DETAILS
# Post Description
post_description = """"""
# Post Text(title+description)
post_text = f"""{post_description}"""
# URL of the image to post
image_url = ''
# Image file name for download
image_name = ''
# Local Address for Image to post
local_image_url = f''

# URLs
# API Request URL to get user name and detials
instagram_user_name_url = 'https://graph.facebook.com/v14.0/{}?access_token={}&fields=id,media_count,username'
# API Request URL to get user id
instagram_user_url ='https://graph.facebook.com/v10.0/{}?fields=instagram_business_account&access_token={}'
# API Request URL to upload the image
instagram_media_request_url ='https://graph.facebook.com/v10.0/{}/media'
# Instagram Graph API publish URL
instagram_publish_url ='https://graph.facebook.com/v10.0/{}/media_publish'
# Facebook API Request URL
facebook_request_url ='https://graph.facebook.com/{}/photos'
# Facebook Authentication URL
facebook_auth_url ='https://www.facebook.com/v14.0/dialog/oauth?response_type&client_id={}&redirect_uri={}&scope={}&response_type=code&state=987654321'
# Facebook Token URL
facebook_token_url = "https://graph.facebook.com/v14.0/oauth/access_token?redirect_uri={}&scope={}&client_id={}&client_secret={}&code={}"
# Facebook Me URL
facebook_me_url = 'https://graph.facebook.com/me?fields=id,name'
# Facebook Page Token URL
facebook_page_token_url ='https://graph.facebook.com/{}/accounts?access_token={}'
# Facebook Long Page Token URL
facebook_long_token_url ='https://graph.facebook.com/v14.0/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}'
# LinkedIn Authentication URL
linkedin_auth_url ='https://www.linkedin.com/oauth/v2/authorization?response_type=code&state=987654321&scope={}&client_id={}&redirect_uri={}'
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
# Facebook Page ID Payload
facebook_page_id_payload = {
    'access_token': facebook_page_access_token
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


def save_values(description, path, url, facebookToken, linkedinToken, pageId, userId):
    """
    This Function saves the values of description, file path, image url, facebook access token, linkedin access token, pageId and text 
    """
    global post_text, post_description, local_image_url, image_url, instagram_media_payload, facebook_post_payload, facebook_page_access_token, facebook_page_token_url, linkedin_access_token, linkedin_headers, instagram_publish_payload, facebook_page_id, facebook_request_url, instagram_user_url, facebook_user_id, instagram_publish_url, instagram_media_request_url
    post_description = description
    local_image_url = path
    image_url = url
    facebook_page_access_token = facebookToken
    linkedin_access_token = linkedinToken
    instagram_user_id = userId
    post_text = f"""{post_description}"""
    instagram_media_payload['caption'] = post_text
    facebook_post_payload['message'] = post_text
    linkedin_post_data['specificContent']['com.linkedin.ugc.ShareContent']['shareCommentary']['text'] = post_text
    instagram_media_payload['image_url'] = image_url
    facebook_post_payload['url'] = image_url
    instagram_media_payload['access_token'] = facebook_page_access_token
    instagram_publish_payload['access_token'] = facebook_page_access_token
    facebook_post_payload['access_token'] = facebook_page_access_token
    facebook_page_token_url = f'https://graph.facebook.com/{facebook_user_id}?fields=access_token&access_token={facebook_user_access_token}&scope={facebook_scopes}'
    linkedin_headers['Authorization'] = f'Bearer {linkedin_access_token}'
    facebook_page_id = pageId
    facebook_user_id = pageId
    facebook_request_url = f'https://graph.facebook.com/{facebook_page_id}/photos'
    instagram_user_url = f'https://graph.facebook.com/v10.0/{facebook_page_id}?fields=instagram_business_account&access_token={facebook_page_access_token}'
    instagram_media_request_url = f'https://graph.facebook.com/v10.0/{instagram_user_id}/media'
    instagram_publish_url = f'https://graph.facebook.com/v10.0/{instagram_user_id}/media_publish'
    print('-------Saved Values DONE-------')

#  ! Unused
def facebook_get_code(code):
    """
    This Function Recieves the facebook_code and then saves it
    """
    global facebook_code, facebook_token_url
    facebook_code = code
    facebook_token_url = f"https://graph.facebook.com/v14.0/oauth/access_token?redirect_uri={facebook_redirect_url}&scope={facebook_scopes}&client_id={facebook_client_id}&client_secret={facebook_client_secret}&code={facebook_code}"
    print('-------Facebook Authentication Code-DONE-------')

# * Used
def facebook_get_user_auth(code):
    """
    This Function calls the facebook Authentication api to get User Access Token
    """
    url=facebook_token_url.format(facebook_redirect_url,facebook_scopes,facebook_client_id,facebook_client_secret,code)
    facebook_token_response = requests.get(url)
    facebook_user_access_token = facebook_token_response.json()['access_token']
    print('-------Facebook User Authentication DONE-------')
    return facebook_user_access_token


def facebook_get_user_id(token):
    """
    This Function gets the facebook_user_id
    """
    # Facebook Me Payload
    facebook_me_payload = {
    'access_token': token
    }
    facebook_me_response = requests.get(facebook_me_url,  facebook_me_payload)
    facebook_user_id = facebook_me_response.json()['id']
    facebook_name = facebook_me_response.json()['name']
    print('-------Facebook User ID DONE-------')
    return {'id':facebook_user_id,'name':facebook_name}

# !Unused


def facebook_get_page_id(token):
    """
    This Function gets the facebook_page_id
    """
    global facebook_page_id, facebook_request_url, instagram_user_url, facebook_user_id
    # Facebook Me Payload
    facebook_me_payload = {
    'access_token': token
    }
    facebook_me_response = requests.get(facebook_me_url,  facebook_me_payload)
    facebook_page_id = facebook_me_response.json()['id']
    facebook_user_id = facebook_me_response.json()['id']
    facebook_request_url = f'https://graph.facebook.com/{facebook_page_id}/photos'
    instagram_user_url = f'https://graph.facebook.com/v10.0/{facebook_page_id}?fields=instagram_business_account&access_token={facebook_page_access_token}'
    print('-------Facebook Page ID DONE-------')

# * Used
def facebook_page_auth(uid,token):
    """
    This Function gets the facebook_page_access_token(s) for all the pages user has
    returns: array of facebook page credentials(token,id,name)
    """
    facebook_credentials = []
    url=facebook_page_token_url.format(uid,token)
    facebook_page_responses = requests.get(url)
    for response in facebook_page_responses.json()['data']:
        print(f'-------Authenticating For Page:{response["name"]}-------')
        page_creds = {
            'access_token': facebook_get_long_token(response['access_token']),
            'page_id': response['id'],
            'page_name': response['name'],
        }
        facebook_credentials.append(page_creds)
        print(f'-------Authentication For Page:{response["name"]} DONE-------')
    print('-------Facebook Pages Authentication DONE-------')
    return facebook_credentials


def facebook_get_long_token(token):
    """
    This Function exchanges Short Lived Token with a Long Lived Token
    arguments: token
    """
    url =facebook_long_token_url.format(facebook_client_id,facebook_client_secret,token)
    facebook_long_response = requests.get(url)
    long_token = facebook_long_response.json()['access_token']
    print('-------Facebook Page Long Token DONE-------')
    return long_token


def post_facebook():
    """
    This Function Posts the data to Facebook
    """
    # Send POST request to Facebook API
    global facebook_post_id
    facebook_resonse = requests.post(
        facebook_request_url, data=facebook_post_payload)
    if facebook_resonse.json().get('error', False):
        print('-------Facebook Post-ERROR-------')
        print(facebook_resonse.json()['error'])
        return facebook_resonse.json()['error']
    facebook_post_id = facebook_resonse.json()['id']
    print('-------Facebook Post-DONE-------')

# ! Unused


def instagram_get_user_id():
    """
    This Function gets the Instagram User ID
    """
    global instagram_user_id, instagram_media_request_url, instagram_publish_url
    instagram_user_id_response = requests.get(instagram_user_url)
    instagram_user_id = instagram_user_id_response.json()[
        'instagram_business_account']['id']
    instagram_media_request_url = f'https://graph.facebook.com/v10.0/{instagram_user_id}/media'
    instagram_publish_url = f'https://graph.facebook.com/v10.0/{instagram_user_id}/media_publish'
    print('-------Get ID Instagram-DONE-------')


# * Used
def instagram_get_username(id, token):
    """
    This function returns instagram username
    Args:
        id : instagram user ID
        token: Access Token
    """
    print("---Getting Instagram Username---------")
    url=instagram_user_name_url.format(id,token)
    instagram_username_response = requests.get(url)
    print("---Instagram Username Found---------")
    return instagram_username_response.json().get('username', '')


def instagram_media_post():
    """
    This Function uploads the image to Instagram
    """
    global instagram_creation_id, instagram_publish_payload
    # Send POST request to media url
    instagram_media_response = requests.post(
        instagram_media_request_url, data=instagram_media_payload)
    instagram_creation_id = instagram_media_response.json()['id']
    instagram_publish_payload['creation_id'] = instagram_creation_id
    print('-------Image Upload Instagram-DONE-------')


def post_instagram():
    """
    This Function Posts the data to Instagram
    it uses the creation_id returned from instagram_media_post to attach image
    """
    global instagram_post_id
    instagram_publish_response = requests.post(
        instagram_publish_url, data=instagram_publish_payload)
    if instagram_publish_response.json().get('error', False):
        print('-------Instagram Post-ERROR-------')
        print(instagram_publish_response.json()['error'])
        return instagram_publish_response.json()['error']

    instagram_post_id = instagram_publish_response.json()['id']
    print('-------Instagram Post-DONE-------')
    return instagram_post_id

#  ! Unused
def linkedin_get_code(code):
    """
    This Function Recieves the linkedin_code and then saves it
    """
    global linkedin_code, linkedin_auth_body
    linkedin_code = code
    linkedin_auth_body['code'] = linkedin_code
    print('-------LinkedIn Authentication Code-DONE-------')


#  * Used
def linkedin_authenticate(code):
    """
    This Function Uses the code and then gets the access token
    """
    # Request Payload for LinkedIn Authentication
    linkedin_auth_body = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": linkedin_redirect_url,
        "client_id": linkedin_client_id,
        "client_secret": linkedin_client_secret,
    }
    linkedin_token_response = requests.post(linkedin_token_url, data=linkedin_auth_body)
    linkedin_access_token = linkedin_token_response.json()["access_token"]
    linkedin_headers['Authorization'] = f'Bearer {linkedin_access_token}'
    print('-------LinkedIn Authentication-DONE-------')
    return {'token':linkedin_access_token,'headers':linkedin_headers}


def linkedin_get_id(headers):
    """
    This Function Gets LinkedIn Profile ID
    """
    linkedin_me_response = requests.get(linkedin_me_url, headers=headers)
    linkedin_profile_id = linkedin_me_response.json()['id']
    linkedin_name = f"{linkedin_me_response.json()['localizedFirstName']} {linkedin_me_response.json()['localizedLastName']}"
    print('-------LinkedIn Profile ID-DONE-------')
    return {'name':linkedin_name,'id':linkedin_profile_id}


def linkedin_register():
    """
    This Function calls the register API from LinkedIn to get asset_id and upload_url
    """
    global linkedin_asset_id, linkedin_upload_url, linkedin_post_data
    linkedin_register_response = requests.post(
        linkedin_register_url, headers=linkedin_headers, json=linkedin_register_body)
    linkedin_upload_url = linkedin_register_response.json(
    )['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']
    linkedin_asset_id = linkedin_register_response.json()['value']['asset']
    linkedin_post_data["specificContent"]["com.linkedin.ugc.ShareContent"]["media"][0]["media"] = linkedin_asset_id
    print('-------LinkedIn Register-DONE-------')


def linkedin_upload_image():
    """
    This Function uploads the image to LinkedIn using the upload_url returned by linkedin_register
    """
    linkedin_image = open(local_image_url, 'rb')
    linkedin_upload_response = requests.put(
        linkedin_upload_url, data=linkedin_image, headers=linkedin_headers)
    print('-------Image Upload LinkedIn-DONE-------')


def post_linkedin():
    """
    This Function posts the data to LinkedIn 
    It uses the asset_id returned by linkedin_register to attach image
    """
    global linkedin_post_id
    linkedin_post_response = requests.post(
        linkedin_url, headers=linkedin_headers, json=linkedin_post_data)
    linkedin_post_id = linkedin_post_response.json()['id']
    print('-------LinkedIn Post-DONE-------')


def authenticate_linkedin(code):
    """
    This Function calls necessary functions to Authenticate with LinkedIn
    """
    resp=linkedin_authenticate(code)
    resp.update(linkedin_get_id(resp['headers']))
    return resp


def authenticate_facebook(code):
    """
    This Function calls necessary functions to Authenticate on Facebook
    """
    token=facebook_get_user_auth(code)
    resp=facebook_get_user_id(token)
    return {'credentials':facebook_page_auth(resp['id'],token),'name':resp['name']}


def authenticate_instagram(credentials):
    """
    This Function calls necessary functions to Authenticate on Instagram
    """
    instagram_credentials = []
    for credential in credentials:
        url=instagram_user_url.format(credential['page_id'], credential['access_token'])
        instagram_user_id_response = requests.get(url)
        if instagram_user_id_response.json().get('instagram_business_account'):
            user_creds = {
                'access_token': credential['access_token'],
                'user_id': instagram_user_id_response.json()['instagram_business_account']['id'],
                'user_name': instagram_get_username(instagram_user_id_response.json()['instagram_business_account']['id'], credential['access_token'])
            }
            instagram_credentials.append(user_creds)
    print("---Instagram Authentication Is Done-----------")
    return instagram_credentials


def make_post_facebook():
    """
    This Function calls necessary functions to make a Facebook post
    """
    post_facebook()


def make_post_instagram():
    """
    This Function calls necessary functions to make a Instagram post
    """
    # instagram_get_user_id()
    instagram_media_post()
    instagram_post_id = post_instagram()
    return instagram_post_id


def make_post_linkedin():
    """
    This Function calls necessary functions to make a LinkedIn post
    """
    linkedin_get_id()
    linkedin_register()
    linkedin_upload_image()
    post_linkedin()


def make_linkedin_post(linkedinToken, description, path, url, socials):
    """
    This Function Calls the other linkedin functions to make post
    """
    is_post_done = []
    save_values(description, path, url,
                '', linkedinToken, '', '')
    if(not(len(linkedinToken) == 0)):
        make_post_linkedin()
        is_post_done.append('linkedin')
    else:
        return
    print("---LinkedIn Post Is Done-----------")
    if type(linkedin_post_id) == dict:
        return linkedin_post_id
    return f'{linkedin_profile_id}_{linkedin_post_id}'


def make_facebook_posts(facebookToken, pageId, description, path, url):
    """
    This Function Calls the other facebook functions to make post
    """
    is_post_done = []
    save_values(description, path, url, facebookToken, '', pageId, '')
    if(not(len(facebookToken) == 0)):
        make_post_facebook()
        is_post_done.append('facebook')
    else:
        return
    print("---Facebook Post Is Done-----------")
    if type(facebook_post_id) == dict:
        return facebook_post_id
    return f'{pageId}_{facebook_post_id}'


def make_instagram_posts(instagramToken, pageId, userId, description, path, url):
    """
    This Function Calls the other instagram functions to make post
    """
    is_post_done = []
    save_values(description, path, url, instagramToken, '', '', userId)
    if(not(len(instagramToken) == 0)):
        instagram_post_id = make_post_instagram()
        is_post_done.append('instagram')
    else:
        return
    print("---Instagram Post Is Done-----------")
    if type(instagram_post_id) == dict:
        return instagram_post_id
    return f'{userId}_{instagram_post_id}'


def authenticate_social(linkedinCode, facebookCode):
    """
    This Function Calls functions to authenticate users
    Args:
        linkedinCode (string): LinkedIn Authentication Token Generated Using OAuth
        facebookCode (string): Facebook Authentication Token Generated Using OAuth
    """
    facebook_credentials = {}
    instagram_credentials = []
    linkedin_credentials = {}
    if not(len(linkedinCode) == 0):
        linkedin_credentials=authenticate_linkedin(linkedinCode)
    if not(len(facebookCode) == 0):
        facebook_credentials = authenticate_facebook(facebookCode)
    if len(facebook_credentials) > 0:
        instagram_credentials = authenticate_instagram(facebook_credentials['credentials'])
    print("--------Social Authentication Is Done-----------")
    return {'linkedin_access_token': linkedin_credentials.get('token',''), 'linkedin_profile_id': linkedin_credentials.get('id',''), 'linkedin_name':linkedin_credentials.get('name',''), 'facebook_name': facebook_credentials.get('name',''), 'facebook_credentials': facebook_credentials.get('credentials',''), 'instagram_credentials': instagram_credentials}


# * Insights Functions

# * All Posts


def facebook_get_all_posts(credential):
    all_facebook_posts = []
    posts_response = {}
    url = f"""https://graph.facebook.com/v14.0/{credential['PageId']}/feed?access_token={credential['SocialMediaAccessToken']}"""
    posts_response = requests.get(url)
    all_facebook_posts = posts_response.json()['data']
    while posts_response.json().get('paging', False).get('next', False):
        posts_response = requests.get(posts_response.json()['paging']['next'])
        all_facebook_posts = all_facebook_posts + posts_response.json()['data']
    print('--Got Facebook Posts--------')
    return all_facebook_posts


def instagram_get_all_posts(credentials):
    all_instagram_posts = []
    posts_response = {}
    url = f"""https://graph.facebook.com/v14.0/{credentials['PageId']}?access_token={credentials['SocialMediaAccessToken']}&fields=id,media_count,username,media"""
    posts_response = requests.get(url)
    all_instagram_posts = posts_response.json()['media']['data']
    posts_response = posts_response.json().get('media')
    while posts_response.get('paging', False).get('next', False):
        posts_response = requests.get(posts_response['paging']['next']).json()
        all_instagram_posts = all_instagram_posts + posts_response['data']
    print("---Instagram Posts Found---------")
    return all_instagram_posts


def facebook_get_post_details(token, id):
    url = f"""https://graph.facebook.com/v14.0/{id}?access_token={token}&fields=permalink_url,full_picture,message"""
    posts_response = requests.get(url)
    details = posts_response.json()
    likeComment = {
        "likes": facebook_get_post_likes(token, id),
        "comment": facebook_get_post_comments(token, id),
        "reach": facebook_get_post_reach(token, id),
        "impression": facebook_get_post_impressions(token, id)
    }
    details.update(likeComment)
    print("---Facebook Post Detials Found---------")
    return details


def instagram_get_post_details(token, id):
    url = f"""https://graph.facebook.com/v14.0/{id}/?access_token={token}&fields=media_url,caption,timestamp,permalink,like_count,comments_count"""
    posts_response = requests.get(url)
    print(url)
    print(posts_response)
    details = posts_response.json()
    # comments = facebook_get_post_comments(token, id)
    # likes = abs(instagram_get_post_likes(token, id)-comments)
    insights = {
        "reach": instagram_get_post_reach(token, id),
        "impressions": instagram_get_post_impressions(token, id)
    }
    details.update(insights)
    print("---Facebook Post Detials Found---------")
    return details


def facebook_get_page_insights(token, id):
    url = f"""https://graph.facebook.com/v14.0/{id}/insights?metric=page_engaged_users,page_posts_impressions,page_post_engagements&access_token={token}&period=lifetime"""
    posts_response = requests.get(url)
    print("---Facebook Post Insights Found---------")
    return posts_response.json()


def instagram_get_page_insights(token, id):
    url = f"""https://graph.facebook.com/v14.0/{id}/insights?metric=impressions,reach,engagement&period=lifetime&access_token={token}"""
    posts_response = requests.get(url)
    print("---Instagram Post Insights Found---------")
    return posts_response.json()


def facebook_get_post_likes(token, id):
    url = f"""https://graph.facebook.com/v14.0/{id}/reactions?access_token={token}"""
    posts_response = requests.get(url)
    print("---Facebook Post Likes Found---------")
    return len(posts_response.json().get('data', []))


def facebook_get_post_comments(token, id):
    url = f"""https://graph.facebook.com/v14.0/{id}/comments?access_token={token}"""
    posts_response = requests.get(url)
    print("---Facebook Post Comments Found---------")
    return len(posts_response.json().get('data', []))


# !getting likes from post detials
def instagram_get_post_likes(token, id):
    url = f"""https://graph.facebook.com/v14.0/{id}/insights/engagement?access_token={token}"""
    posts_response = requests.get(url)
    print("---Instagram Post Likes Found---------")
    return posts_response.json().get('data', [])[0].get('values', [])[0].get('value')


def instagram_get_post_impressions(token, id):
    url = f"""https://graph.facebook.com/v14.0/{id}/insights/impressions?access_token={token}&period=days_28"""
    posts_response = requests.get(url)
    print("---Instagram Post Impressions Found---------")
    return posts_response.json().get('data', [])[0].get('values', [])[0].get('value')


def instagram_get_post_reach(token, id):
    url = f"""https://graph.facebook.com/v14.0/{id}/insights/reach?access_token={token}&period=days_28"""
    posts_response = requests.get(url)
    print("---Instagram Post Reach Found---------")
    return posts_response.json().get('data', [])[0].get('values', [])[0].get('value')


def facebook_get_post_reach(token, id):
    url = f"""https://graph.facebook.com/v14.0/{id}/insights?metric=post_engaged_users&access_token={token}"""
    posts_response = requests.get(url)
    print("---Facebook Post Reach Found---------")
    return posts_response.json().get('data', [])[0].get('values', [])[0].get('value')


def facebook_get_post_impressions(token, id):
    url = f"""https://graph.facebook.com/v14.0/{id}/insights?metric=post_impressions&access_token={token}"""
    posts_response = requests.get(url)
    print("---Facebook Post Impression Found---------")
    return posts_response.json().get('data', [])[0].get('values', [])[0].get('value')


def facebook_get_page_insights(token, id, name):
    url = f"""https://graph.facebook.com/v14.0/{id}/insights?metric=page_posts_impressions,page_post_engagements&access_token={token}&period=days_28"""
    page_response = requests.get(url)
    impressions = page_response.json().get('data', [])[0].get('values', [])[0].get(
        'value', 0)+page_response.json().get('data', [])[0].get('values', [])[1].get('value', 0)
    reach = page_response.json().get('data', [])[1].get('values', [])[0].get('value', 0) + \
        page_response.json().get('data', [])[1].get('values', [])[1].get('value', 0)
    insights = {
        "page_id": id,
        "user_name": name,
        "impression": impressions,
        "reach": reach
    }
    print("---Facebook Page Insights Found---------")
    return insights


def instagram_get_page_insights(token, id, name):
    url = f"""https://graph.facebook.com/v14.0/{id}/insights?metric=impressions,reach&access_token={token}&period=days_28"""
    page_response = requests.get(url)
    impressions = page_response.json().get('data', [])[0].get('values', [])[0].get(
        'value', 0)+page_response.json().get('data', [])[0].get('values', [])[1].get('value', 0)
    reach = page_response.json().get('data', [])[1].get('values', [])[0].get('value', 0) + \
        page_response.json().get('data', [])[1].get('values', [])[1].get('value', 0)
    insights = {
        "page_id": id,
        "user_name": name,
        "impression": impressions,
        "reach": reach
    }
    print("---Instagram Page Insights Found---------")
    return insights


# ! Hashtag Functions

def code_from_hashtag(hashtag, id, token):
    url = f"https://graph.facebook.com/v14.0/ig_hashtag_search?user_id={id}&q={hashtag}&access_token={token}"
    resp = requests.get(url)
    print("---Instagram Hashtag Code Found---------")
    return resp.json().get('data', [])[0].get('id', 0)


def get_recent_from_hashtag(tag_id, id, token, pages):
    fields = "id,media_type,comments_count,like_count,caption,media_url,permalink,timestamp "
    url = f"""https://graph.facebook.com/{tag_id}/recent_media?user_id={id}&fields={fields}"""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    resp = requests.get(url, headers=headers)
    all_instagram_posts = resp.json().get('data', [])
    resp = resp.json()
    if len(all_instagram_posts) <= 0:
        return all_instagram_posts
    i = 0
    while resp.get('paging', False).get('next', False):
        print('resp.json()???')
        resp = requests.get(resp['paging']['next'], headers=headers).json()
        all_instagram_posts = all_instagram_posts + resp.get('data', [])
        i += 1
        if i >= pages:
            break
    print("---Instagram Posts Found---------")
    return all_instagram_posts


def get_top_from_hashtag(tag_id, id, token, pages):
    fields = "id,media_type,comments_count,like_count,caption,media_url,permalink,timestamp "
    url = f"""https://graph.facebook.com/{tag_id}/top-media?user_id={id}&fields={fields}"""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    resp = requests.get(url, headers=headers)
    all_instagram_posts = resp.json().get('data', [])
    resp = resp.json()
    i = 0
    while resp.get('paging', False).get('next', False):
        resp = requests.get(resp['paging']['next'], headers=headers).json()
        all_instagram_posts = all_instagram_posts + resp.get('data', [])
        print('******', len(all_instagram_posts))
        print('****', i)
        i += 1
        print('*****', i)
        if i >= pages:
            break
    print("---Instagram Posts Found---------")
    return all_instagram_posts
