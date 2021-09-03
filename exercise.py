import tweepy
from secrets_info import secret

account = {
    "consumer_key": secret.consumer_key,
    "consumer_secret": secret.consumer_secret,
    "access_token": secret.access_token,
    "access_token_secret": secret.access_token_secret
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

if __name__ == "__main__":
    my_twitter = Twitter_api(account)
    # my_twitter.tweet("お疲れ様です。")