import tweepy
import pandas as pd
from secrets_info import secret

ACCOUNT = {
    "consumer_key": secret.consumer_key,
    "consumer_secret": secret.consumer_secret,
    "access_token": secret.access_token,
    "access_token_secret": secret.access_token_secret
}

SEARCH_TWEETS_URL = 'https://api.twitter.com/1.1/search/tweets.json'
RATE_LIMIT_STATUS_URL = "https://api.twitter.com/1.1/application/rate_limit_status.json"
SEARCH_LIMIT_COUNT = 10


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
    # print(my_twitter.get_tweets("tocho_covid19", 10))
