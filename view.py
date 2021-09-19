import eel
import desktop
from common import multi_thread
import common.amazon_scraping as ama
import common.twitter_api as twitter
from dotenv import load_dotenv
import os

app_name = "web"
end_point = "index.html"
size = (600,700)
thread_list = {}

load_dotenv()

ACCOUNT = {
    "consumer_key": os.getenv('CONSUMER_KEY'),
    "consumer_secret": os.getenv('CONSUMER_SECRET'),
    "access_token": os.getenv('ACCESS_TOKEN'),
    "access_token_secret": os.getenv('ACCESS_TOKEN_SECRET'),
}

my_twitter = twitter.Twitter_api(ACCOUNT)

@ eel.expose
def get_item_list(search_keyword):
    return ama.get_amazon_items(search_keyword, 1)

@ eel.expose
def check_and_tweet(items):
    for item in items:
        if item not in thread_list:
            t = multi_thread.multiThread(item, 60, True, my_twitter)
            t.start()
            thread_list[item] = t
        else:
            t_end = thread_list[item]
            t_end.check_status = False
            t_end.join()
            del thread_list[item]

        



desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)

# if __name__ == "__main__":
#     df = get_news_title("ro", "欧州市場サマリー")
