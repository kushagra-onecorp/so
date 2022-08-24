import requests

# Access Token from LinkedIn API
linkedin_access_token= """AQUqQKZJxz97WHgCmz_CEckhGv7HTj_3xpQR_5RgS-QdXkt8EV50XboCmXqw_h67adWQgXFFlAzDoA7bp5LjOaD-0JMXJ9xFZoP9aGhRv_MsWhXzFV83R2c8wV2H8cKu9BkgpVEoRqgOzTZi00AyXyjGWNjuuZGy6fhMKkCYp2vdJ2q3ifgS5vT22LlkjU2Gk78lyf6sqKHFbV8sXOpu3CB1DdRxWNKqMle87IHATeO4b4faGDmlCIgzlwlCOnxT1XV02orBPPvEJFk7XyI9o4sne-ITmqkbZ7Ji0kiATqbm0wiKbQHA5yWS_D-7pj3WCabaqIrZLYNJNDrSUjq90QLpexZdWg"""
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
linkedin_profile_id='gXaSyTq5Tm'
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


linkedin_register_response1 = requests.post(linkedin_register_url, headers=linkedin_headers, json=linkedin_register_body)

print('-------------------')
print(linkedin_register_response1.json())

linkedin_upload_url1=linkedin_register_response1.json()['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']

print(linkedin_upload_url1)

linkedin_register_response2 = requests.post(linkedin_register_url, headers=linkedin_headers, json=linkedin_register_body)

print('-------------------')
print(linkedin_register_response2.json())

linkedin_upload_url2=linkedin_register_response2.json()['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']

print(linkedin_upload_url2)

local_image_url1='./post_image.jpg'
linkedin_upload_image1=open(local_image_url1,'rb')

linkedin_upload_response1 = requests.put(linkedin_upload_url1,data=linkedin_upload_image1, headers=linkedin_headers)
print(linkedin_upload_response1)

linkedin_asset_id1=linkedin_register_response1.json()['value']['asset']
print(linkedin_asset_id1)

local_image_url2='./social.png'
linkedin_upload_image2=open(local_image_url2,'rb')

linkedin_upload_response2 = requests.put(linkedin_upload_url2,data=linkedin_upload_image2, headers=linkedin_headers)
print(linkedin_upload_response2)

linkedin_asset_id2=linkedin_register_response2.json()['value']['asset']
print(linkedin_asset_id2)
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
                    "media": linkedin_asset_id1,
                    "title": {
                        "text": "LinkedIn Talent Connect 2021"
                    }
                },
                {
                    "status": "READY",
                    "description": {
                        "text": "Center stage!"
                    },
                    "media": linkedin_asset_id2,
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