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
images_url=['./post_image.jpg','./social.png']
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
media_ids=[]
for img in images_url:
    linkedin_register_response = requests.post(linkedin_register_url, headers=linkedin_headers, json=linkedin_register_body)
    print('-------------------')
    print(linkedin_register_response.json())
    linkedin_upload_url=linkedin_register_response.json()['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']
    print(linkedin_upload_url)
    linkedin_upload_image=open(img,'rb')
    linkedin_upload_response = requests.put(linkedin_upload_url,data=linkedin_upload_image, headers=linkedin_headers)
    print(linkedin_upload_response)
    linkedin_asset_id=linkedin_register_response.json()['value']['asset']
    media_ids.append(linkedin_asset_id)
    print(media_ids)

medias=[]
for id in media_ids:
    media={
                    "status": "READY",
                    "description": {
                        "text": post_text
                    },
                    "media": id,
                    "title": {
                        "text": post_text
                    }
                }
    print(media)
    medias.append(media)
    print(medias)

linkedin_post_data = {
    "author": f"urn:li:person:{linkedin_profile_id}",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text":post_text
            },
            "shareMediaCategory": "IMAGE",
             "media":medias
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

linkedin_post_response = requests.post(linkedin_url, headers=linkedin_headers, json=linkedin_post_data)

print(linkedin_post_response.json())