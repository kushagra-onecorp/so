import tweepy

# ! Client Credentials
twitter_client_id = "cXFQbG1nQWkybmhrRkFzM25MTzg6MTpjaQ"
twitter_client_secret = "jMkuH3RssjI_KUVRDKRWK2gA2gEmDK_ALmP_NTtarYQXSqZmtR"

# ! Consumer Credentials
twitter_consumer_key = 'ie0yFTgq4XwLSBAFOWdBoBIAR'
twitter_consumer_secret = 'cOicl85MHBFBWGVNVrZWn87RPJs0Fq1OBLsXPO1cgcSxeNyUXO'

# ! Others
redirect_url = 'https://onepost.sasone.in/linked-accounts/twitter/'
twitter_scope = 'tweet.read,tweet.write,users.read,offline.access'

# ! User Access Token
twitter_access_token=""
twitter_access_secret=""


# auth = tweepy.OAuth1UserHandler(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret)

# auth.set_access_token(
#     key=twitter_access_token, secret=twitter_access_secret)

# print(auth.access_token)

# api = tweepy.API(auth)

# client = tweepy.Client(twitter_access_token)

# media_ids=[]

# client.media_upload()

auth = tweepy.OAuth1UserHandler(consumer_key=twitter_consumer_key,consumer_secret=twitter_consumer_secret,callback=redirect_url)

print(auth.get_authorization_url(signin_with_twitter=True))
oauth_verifier = input("Enter OAuth Verifier: ")

twitter_access_token,twitter_access_secret = auth.get_access_token(oauth_verifier)

api = tweepy.API(auth)

print(api.update_status_with_media(status='Hello Tweepy',filename='post_image.jpg',file='./images/post_image.jpg'))

# print(client.create_tweet(text='hello tweepy',media_ids=media_ids,user_auth=False))
