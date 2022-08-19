import requests

# Access Token from LinkedIn API
linkedin_access_token= """AQTJPt-8nykDzYZ55K4f9SmkNjsfPN0Cw1v2VaVWrChCo3OKhhhPHNrIAa-yamCVTLv0_9BJoG5izswDCJgorY2Ra-Ii1vWte17j-bwxUVsxU57aO38h17hT_GENORoIUHGR1wxmXbGzy5dKNmo11cM3OhHAkOGYZ6QIJP5_1HbnANmtjegyikNjL1VBMvm-HX8x6JUhj9qn5WUkdtY"""
# Post Title
post_title='Post Title'
# Post Description
post_description='Post Description'
# Post Text(title+description)
post_text=f"""
{post_title}
{post_description}
"""
# LinkedIn Profile ID
linkedin_profile_id='c3XjDWEQZr'
# 
linkedin_url = "https://api.linkedin.com/v2/ugcPosts"
linkedin_register_url='https://api.linkedin.com/v2/assets?action=registerUpload'
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
linkedin_headers = {
           'Authorization': f'Bearer {linkedin_access_token}'
           }
local_image_url='./post_image.jpg'


linkedin_register_response = requests.post(linkedin_register_url, headers=linkedin_headers, json=linkedin_register_body)

print('-------------------')
print(linkedin_register_response.json())

linkedin_upload_url=linkedin_register_response.json()['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']

print(linkedin_upload_url)

linkedin_upload_image=open(local_image_url,'rb')

linkedin_upload_response = requests.put(linkedin_upload_url,data=linkedin_upload_image, headers=linkedin_headers)
print(linkedin_upload_response)

linkedin_asset_id=linkedin_register_response.json()['value']['asset']
print(linkedin_asset_id)
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

linkedin_post_response = requests.post(linkedin_url, headers=linkedin_headers, json=linkedin_post_data)

print(linkedin_post_response.json())