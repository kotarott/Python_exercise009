import tweepy
from secrets_info import secret

consumer_key = secret.consumer_key
consumer_secret = secret.consumer_secret
access_token = secret.access_token
access_token_secret = secret.access_token_secret

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# tweetを投稿
api.update_status("APIツイートのテスト")
