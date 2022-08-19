import requests
import shutil

# TOKENS
# Access Token from LinkedIn API
linkedin_access_token= """AQUkL2iAkfnIaPcwi4LxZuXkbYvA8mLvSPFzryFlOxnIXn_QoCHuWdfPSvUAts_ldEhfg3uOa7tHWck03667pxYYyH49K2NRyiD7gXJopuiskDV7u71nb-WYN82lPsVw-6Du2TN9EEKzqO7ngOtirfdbVqcT5_hiG2Fk6tFACymeS78Q_qQ423FkGc8K7_FYSvPSoBGYmV89UKEWwiptvKPOmO_pPV1Y30VW45xDlrUDQyGzoaBjCt1prIw380q_7dh-ERsjxpxIwmHP3RHcW0v_EWetRqFFi_YN3lg8v_drxAz9gpNbwOT5o0qfCzL9bal2B_uB1BWMSjUrc_n9wp_Gjse4aA"""
# Access Token from Facebook Graph API
facebook_access_token="""EAAUFRLCbo1MBANO0nNiHJZCRzBOhgr4NMZAFNlTtRxjej1l2wKgRvxGeP9BdFYs9ULZBQG6ArDLkgXqqR9Q5uwrwrWokj2mkWcfEg8XtbD277tEr53GjOCoOGIsstdPjsWaJka7VXooBoyL7tMWTrlv74qvi1qzNMwxYxZA1MoKFza8EqZCUIUuzG9PBFjegZD"""
# IDs
# LinkedIn Profile ID
linkedin_profile_id='rsDN01ubPC'
# Facebook Page ID
facebook_page_id='103995469037355'
# Instagram User ID
instagram_user_id='17841453883347404'

# POST DETAILS
# Post Title
post_title='AI Posted'
# Post Description
post_description="""Python Made this post
#HelloWorl #AI #python #social #future
"""
# Post Text(title+description)
post_text=f"""
{post_title}
{post_description}
"""
# URL of the image to post
image_url='https://images.unsplash.com/photo-1604922824961-87cefb2e4b07?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80'
# Image file name for download
image_name='post_image.jpg'
# Local Address for Image to post
local_image_url=f'./{image_name}'

# URLs
# API Request URL to upload the image
instagram_media_request_url = f'https://graph.facebook.com/v10.0/{instagram_user_id}/media'
# Instagram Graph API publish URL
instagram_publish_url=f'https://graph.facebook.com/v10.0/{instagram_user_id}/media_publish'
# Facebook API Request URL
facebook_request_url = f'https://graph.facebook.com/{facebook_page_id}/photos'
# LinkedIn API URL to Post
linkedin_url = "https://api.linkedin.com/v2/ugcPosts"
# LinkedIn API URL to Register Media
linkedin_register_url='https://api.linkedin.com/v2/assets?action=registerUpload'
# LinkedIn API URL to Upload Image
linkedin_upload_url=''

# LinkedIn Asset Id
linkedin_asset_id=''
# Instagram Creation Id
instagram_creation_id=''

# DATA
# Request payload for Instagram media request
instagram_media_payload = {
'image_url': image_url,
'caption':post_text,
'access_token': facebook_access_token
}
# Payload for Instagram publish request
instagram_publish_payload= {
'creation_id':instagram_creation_id,
'access_token': facebook_access_token
}
# Facebook Request Payload
facebook_post_payload = {
'message':post_text,
'url': image_url,
'access_token': facebook_access_token
}
# Request payload for LinkedIn Register
linkedin_register_body={
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
                "text":post_text
            },
            "shareMediaCategory": "IMAGE",
             "media":[
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
def print_response(resonse,is_json=True):
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
    image_raw=resonse.raw
    with open(image_name,'wb') as f:
        shutil.copyfileobj(image_raw, f)
    print(f"Image sucessfully Downloaded:{image_name}")

def post_facebook():
    """
    This Function Posts the data to Facebook
    """
    #Send POST request to Facebook API
    facebook_resonse = requests.post(facebook_request_url,data=facebook_post_payload)
    # print_response(facebook_resonse)
    print('-------Facebook Post-DONE-------')

def instagram_media_post():
    """
    This Function uploads the image to Instagram
    """
    global instagram_creation_id, instagram_publish_payload
    #Send POST request to media url
    instagram_media_response = requests.post(instagram_media_request_url,data=instagram_media_payload)
    # print_response(instagram_media_response)
    print('-------Image Upload Instagram-DONE-------')
    instagram_creation_id = instagram_media_response.json()['id']
    instagram_publish_payload['creation_id']=instagram_creation_id

def post_instagram():
    """
    This Function Posts the data to Instagram
    it uses the creation_id returned from instagram_media_post to attach image
    """
    instagram_publish_response = requests.post(instagram_publish_url,data=instagram_publish_payload)
    # print_response(instagram_publish_response)
    print('-------Instagram Post-DONE-------')

def linkedin_register():
    """
    This Function calls the register API from LinkedIn to get asset_id and upload_url
    """
    global linkedin_asset_id, linkedin_upload_url, linkedin_post_data
    linkedin_register_response = requests.post(linkedin_register_url, headers=linkedin_headers, json=linkedin_register_body)
    # print_response(linkedin_register_response)
    print('-------LinkedIn Register-DONE-------')
    linkedin_upload_url = linkedin_register_response.json()['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']
    linkedin_asset_id = linkedin_register_response.json()['value']['asset']
    linkedin_post_data["specificContent"]["com.linkedin.ugc.ShareContent"]["media"][0]["media"]=linkedin_asset_id

def linkedin_upload_image():
    """
    This Function uploads the image to LinkedIn using the upload_url returned by linkedin_register
    """
    linkedin_image=open(local_image_url,'rb')
    linkedin_upload_response = requests.put(linkedin_upload_url,data=linkedin_image, headers=linkedin_headers)
    # print_response(linkedin_upload_response,False)
    print('-------Image Upload LinkedIn-DONE-------')

def post_linkedin():
    """
    This Function posts the data to LinkedIn 
    It uses the asset_id returned by linkedin_register to attach image
    """
    linkedin_post_response = requests.post(linkedin_url, headers=linkedin_headers, json=linkedin_post_data)
    # print_response(linkedin_post_response)
    print('-------LinkedIn Post-DONE-------')

def make_post_facebook():
    """
    This Function calls necessary functions to make a Facebook post
    """
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
    linkedin_register()
    linkedin_upload_image()
    post_linkedin()

def make_posts():
    """
    This Function Calls the other social functions to make post
    """
    download_image()
    make_post_facebook()
    make_post_instagram()
    make_post_linkedin()

make_posts()