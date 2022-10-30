import requests


linkedin_access_token = """AQVyIPmv23iKRnpJdNfe2iKCsoqP2GBlXYVZyWYe-0Cr0R0SlmqsEZDMFgwdyrxoXpX2P8biLRp-P0bz7AJEFUe8Xncggbf6Ay3NvTVbj5ChK6hZe68OUG5SoHmMjX5dtKp3qtC4_y_pbHuToX7sZ8YHdAC6Y5zw_mjoOeaEjfqVEEv1KYbuY_6GXolAg6UkB0Nj3BBqldDPr0LPAryJjcy32oD9mFW_Mc5oed2IThqa3QJL-uqGIhinFBnRj7Wf8WDmP5BOl8VXvPsifJHbqBj_hbH6YCljXTfBjUERMNzF17rPQUxDR7qdAVS2Yz3UgITE2KQZWIabuwjJ5L4a5Gj2gHbl3A"""


linkedin_headers = {
    "Authorization": f"Bearer {linkedin_access_token}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0"
}

linkedin_me_url = "https://api.linkedin.com/v2/me"
linkedin_me_response = requests.get(linkedin_me_url, headers=linkedin_headers)
linkedin_profile_id = f"urn:li:person:{linkedin_me_response.json()['id']}"
print(linkedin_profile_id)


orgUrl = 'https://api.linkedin.com/v2/organizationAcls?q=roleAssignee&projection=(elements*(*,organization~(localizedName),organization~(logoV2(original~:playableStreams))))'

resp = requests.get(orgUrl, headers=linkedin_headers)
print(resp.json())
organizationID = ''
for page in resp.json().get('elements', []):
    if page.get('role', False) in ["ADMINISTRATOR", "DIRECT_SPONSORED_CONTENT_POSTER"] and page.get('state', False) == "APPROVED" and page.get('roleAssignee', False) == linkedin_profile_id:
        organizationID = page.get('organization').split(':')[-1]
        organizationName = page.get('organization~').get('localizedName')
        organizationImage = page.get('organization~').get(
            'logoV2')['original~']['elements'][-1]['identifiers'][0]['identifier']
        print(organizationID)
        print(organizationImage)
        print(organizationName)
