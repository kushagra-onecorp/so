import requests

# Access Token from LinkedIn API
linkedin_access_token = """AQXbW07y2PlQM1hYF_5_E5mGf0Xk88JPoLhxcPyfOwkVACXpmc_gvj88VDaf2MH0jJDLhWxZB87cpBf4fqZv-baQgst0QvMmt9ZH-Fe931AsVFa1dJPGc-ttAiR6CzDbxYlmfdxBOjoR6cIQ5uizypXSJRegJmZURB9xtOk0KjNXlJ5QNq-MYkIKTKZ9z7pvehyvu1Y9TmefZxyO6-B4sBx51ZNT-NF32R2olgOmdjg7qksJjfrehrXBEe6Xhb0_EPwE0kvzE6cbDEbx2R7rqABiExIulCcsZ5q17n8gcompX6s-_SRK2R1wtyMeLJ8voslqoOTKhSn8PalUybN9y9py74oyAw"""


# Post Description
post_text = 'Post Description'
# LinkedIn Profile ID
linkedin_profile_id = 'gXaSyTq5Tm'
# linkedin post url
linkedin_url = "https://api.linkedin.com/v2/ugcPosts"
linkedin_headers = {
    'Authorization': f'Bearer {linkedin_access_token}'
}

linkedin_post_data = {
    "author": f"urn:li:person:{linkedin_profile_id}",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": post_text
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

linkedin_post_response = requests.post(
    linkedin_url, headers=linkedin_headers, json=linkedin_post_data)

print(linkedin_post_response.json())
