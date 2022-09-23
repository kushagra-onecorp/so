import json
import requests


facebook_access_token="EAALefOGyJXQBAGoDupBmoTICG6Vt4nd8D0heXGfo0D4P4aOK4MW7CCW0Rq7etOZAOj6qnn2XwLZBER2llOeSlK4zJXUoMRCIlaVqaoNNRiPWhJBoRykhwJui2MMDV3ixZAkt0Sr0zVB870aoIa9lPDkBB978OS2ll3BBkJz4kaJko4HmEED"
facebook_page_id= "103995469037355"
#facebook_access_token="EAALefOGyJXQBAIKCMyUWuZBSAy5tc9MLyfWkVrxZAvJqMh4ZCTmhv38ZBNvH8Pzl9kIpkQM0pSVOjTFM9EFZBRFn4StlrdnEYs7wkgElo1rLDwZB3MZCDOVhd5x4Buipu0NaWZBa25hNJuRPotVLavg1bNBgMp4yXT8OuPtUGDUKZC9vo3Oe6IFJm"
# facebook_page_id= "102068252597979"
#facebook_access_token="EAALefOGyJXQBAFwr42zVZC4KyEKwhzgW1BZAYnBzZBVO7QELp6pB2KLBufJw0n7oBWAtdrBL5LlNcXVkWctVuXFGSS8szsHYU067z5IYzwdqhnV9QnLRnrCNBDvlPLJrCwjjmuT6orqeW97exoQZB2ZBaiZA9QpaaIiPLL7PIBYDpQoaSDZAcz7"
# facebook_page_id= "101434159376809"

# Post Title
post_title='Post Title'
# Post Description
post_description='Post Description'
# Post Text(title+description)
post_text=f"""
{post_title}
{post_description}
"""
# URL of the image to post
images_url=['https://wallpaperaccess.com/full/1398313.jpg','https://wallpaperaccess.com/full/1388313.jpg','https://wallpaperaccess.com/full/1398213.jpg']
facebook_photo_upload_url=f'https://graph.facebook.com/v14.0/{facebook_page_id}/photos'
media_ids=[]
for img in images_url:
        facebook_upload_body={
                'url':img,
                'published':'false',
                'access_token':facebook_access_token
                }
        print(facebook_photo_upload_url)
        print(facebook_upload_body)
        facebook_image= requests.post(facebook_photo_upload_url,data=facebook_upload_body)
        print(facebook_image.text)
        media_ids.append(facebook_image.json()['id'])
attached_medias=[{'media_fbid':id} for id in media_ids]
# Facebook API Request URL
facebook_request_url = f'https://graph.facebook.com/{facebook_page_id}/feed'
# Facebook Request Payload
facebook_post_payload = {
'message':post_text,
'attached_media':json.dumps(attached_medias),
'access_token': facebook_access_token
}
print(facebook_request_url)
print(facebook_post_payload)
#Send POST request to Facebook API
facebook_resonse = requests.post(facebook_request_url,data=facebook_post_payload)

print(facebook_resonse.json())
