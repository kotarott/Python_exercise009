import tweepy
import pandas as pd
from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv
import os

load_dotenv()

ACCOUNT = {
    "consumer_key": os.getenv('CONSUMER_KEY'),
    "consumer_secret": os.getenv('CONSUMER_SECRET'),
    "access_token": os.getenv('ACCESS_TOKEN'),
    "access_token_secret": os.getenv('ACCESS_TOKEN_SECRET'),
}


class Twitter_api:
    def __init__(self, account):
        self.consumer_key = account["consumer_key"]
        self.consumer_secret = account["consumer_secret"]
        self.access_token = account["access_token"]
        self.access_token_secret = account["access_token_secret"]
        self.auth_account()

    def auth_account(self):
        # Twitterオブジェクトの生成
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, text):
        # tweetする
        self.api.update_status(text)

    def get_tweets(self, account, count):
        # 特定のユーザーのツイートを取得する
        tweets = self.api.user_timeline(account, count=count, page=1)
        df = pd.DataFrame(columns=[
            "tweetId",
            "tweetUser",
            "tweetDate",
            "contents",
            "favo",
            "retw"
        ])
        for tweet in tweets:
            data = {
                "tweetId": tweet.id,
                "tweetUser": tweet.user.screen_name,
                "tweetDate": tweet.created_at,
                "contents": tweet.text,
                "favo": tweet.favorite_count,
                "retw": tweet.retweet_count
            }
            df = df.append(data, ignore_index=True)
        return df


if __name__ == "__main__":
    my_twitter = Twitter_api(ACCOUNT)
    # my_twitter.tweet("お疲れ様です。")
    print(my_twitter.get_tweets("tocho_covid19", 10))
