import requests


def splice_array_with_content(
    array, count): return array[len(array)-count:len(array)]

def facebook_get_all_posts(credential, page=1, content=10):
    url = f"""https://graph.facebook.com/v14.0/{credential['PageId']}/feed"""
    params = {
        "fields": "permalink_url,full_picture,message",
        "access_token": credential['SocialMediaAccessToken'],
        "limit": f'{content}',
        "offset": f'{page-1}'
    }
    posts_response = requests.get(url, params=params)
    all_posts = posts_response.json()['data']
    all_posts = splice_array_with_content(all_posts, content)
    print('--Got Facebook Posts--------')
    return all_posts



def instagram_get_all_posts(credential, page=1, content=10):
    url = f"""https://graph.facebook.com/v14.0/{credential['PageId']}/media"""
    params = {
        "fields": "media_url,caption,timestamp,permalink,like_count,comments_count",
        "access_token": credential['SocialMediaAccessToken'],
        "limit": f'{page*content}',
    }
    posts_response = requests.get(url, params=params)
    all_posts = posts_response.json()['data']
    all_posts = splice_array_with_content(all_posts, content)
    print("---Instagram Posts Found---------")
    return all_posts


def linkedin_get_all_posts(credential, start=1, count=10):
    all_posts = []
    url = f"https://api.linkedin.com/v2/posts?"
    headers = {
        'Authorization': f'Bearer {credential["SocialMediaAccessToken"]}'
    }
    params = {
        "author": f"urn:li:organization:{credential['PageId']}",
        "isDsc": "false",
        "q": "author",
        "count": f"{count}",
        "start": f"{start-1}"
    }
    posts_response = requests.get(url, params=params, headers=headers)
    all_posts = posts_response.json().get('elements', {})
    print('--Got LinkedIn Posts--------')
    return all_posts


def linkedin_get_post_detials(id, token):
    id = f"urn:li:share:{id}"
    url = f"https://api.linkedin.com/v2/posts/{id}"

    header = {
        'Authorization': f'Bearer {token}'
    }
    onePost_Response = requests.get(url, headers=header)
    print('--Got LinkedIn Post Detials--------')
    return onePost_Response.json()


def linkedin_get_post_link(
    post_id): return f'https://www.linkedin.com/feed/update/urn:li:share:{post_id}'


credential = {
    "PageId": "103995469037355",
    "SocialMediaAccessToken": "EAAJQ4liagnQBADuZCXBrYEbI0KBCDryY3bn6cAXJlSRtZBqTEXr2KZCBc6S7QaFmU0wpeDrhH1V8lYQSCWe2PnyFx0FdxwNXDrj215Pugog6ZA0NdtXhn7F1ZAwL2pk82vMFWyaZB73NxJ63b2nzOG5t58jEQx6XLjb7rS7VjygyFEGZB47ixFRyuqaa5OW7ZCcPz2bPmy9sFV58kmK6qD236Js2A8Epb9U3M5jjMYOktKqMrv4cWqHX"
}
print(linkedin_get_post_link('6942490014932967424'))
