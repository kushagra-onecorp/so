import requests

# Access Token from LinkedIn API
linkedin_access_token= """AQWzYto687fM0l2nv8AxJA82d9GXCegbvv7H5c-6ONkFSoYVhu6WoXPfUVIKeoRc0mgYDa7kv6TzizKwPTHq1TnNpvUXUV2q863M422UCCdM-vkI2zlfaREMGjmVuU_jznVJuSpwB5L5xUMaCIwTKBRgTfETZitQg_Fu_kqbBQlM6Zgas9sU7BdNArmoEDfPp6Gba8U4M5ucnIS1fAH9-W7z5_3JiWHQ3pnDa2ChkuB518iMGg9B8muYq-akM-6JL4ZEnmA5jUh_S0PPdApAE-O62---daiWRmq_nr36ek_55ClZ0sDAeU-nM82PIywbwXYXFaboK81k3n9E-s7Ko-HWsVVMHA"""
# linkedin_access_token= """AQUXgjoc2xhG-he6aXfg1pkalPUAeOIZcRTCRW8mXuTjvPvAMljLfTvs10vB_c6wObKZg8IAVUY3CNZLpZ_OLpYtXEP3JCdcgENBehJecsBbnp7EN_Z7YxNsWiUagwHnFxGBdBOlANW_qMj0EwL6cshe00izXsJbbhjLCD7VvDExQNhayU-K7ROJKalcwIGv65gIi7cq8UMMX_HtJVlTMS1_wVv0WVYZyzkdF5O6yjqEzQSLa_2mKT3o88o7EJrqCRDpEgwcFMIBY0OMXWLt7PhRQSeezt02B9Dr1Galt4kyuxM5gmhreII16Kyf_ghrcso3JvFBhQhjOiXnTD__xZanhY5TTw"""
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
images_url=['./images/post_image.jpg','./images/astrolight.jpg','./images/KIWI.jpg']
linkedin_register_body={
    "registerUploadRequest": {
        "recipes": [
            "urn:li:digitalmediaRecipe:feedshare-image"
        ],
        "owner": 'urn:li:organization:82596640',
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
    "author": 'urn:li:organization:82596640',
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