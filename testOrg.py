import requests


linkedin_access_token = """AQWzYto687fM0l2nv8AxJA82d9GXCegbvv7H5c-6ONkFSoYVhu6WoXPfUVIKeoRc0mgYDa7kv6TzizKwPTHq1TnNpvUXUV2q863M422UCCdM-vkI2zlfaREMGjmVuU_jznVJuSpwB5L5xUMaCIwTKBRgTfETZitQg_Fu_kqbBQlM6Zgas9sU7BdNArmoEDfPp6Gba8U4M5ucnIS1fAH9-W7z5_3JiWHQ3pnDa2ChkuB518iMGg9B8muYq-akM-6JL4ZEnmA5jUh_S0PPdApAE-O62---daiWRmq_nr36ek_55ClZ0sDAeU-nM82PIywbwXYXFaboK81k3n9E-s7Ko-HWsVVMHA"""


linkedin_headers = {
    "Authorization": f"Bearer {linkedin_access_token}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0"
}

linkedin_me_url = "https://api.linkedin.com/v2/me"
linkedin_me_response = requests.get(linkedin_me_url, headers=linkedin_headers)
linkedin_profile_id = f"urn:li:person:{linkedin_me_response.json()['id']}"
print(linkedin_profile_id)


orgUrl = 'https://api.linkedin.com/v2/organizationAcls?q=roleAssignee&role=ADMINISTRATOR&projection=(elements*(*,organization~(localizedName)))'

resp = requests.get(orgUrl, headers=linkedin_headers)
print(resp.json())
organizationID=''
for page in resp.json().get('elements', []):
    if page.get('role', False) in ["ADMINISTRATOR","DIRECT_SPONSORED_CONTENT_POSTER"] and page.get('state', False) == "APPROVED" and page.get('roleAssignee', False) == linkedin_profile_id:
        organizationID=page.get('organization').split(':')[-1]
        organizationName=page.get('organization~').get('localizedName')
        print(organizationID)
        print(organizationName)
