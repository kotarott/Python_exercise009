import threading
import amazon_scraping as scraping
import time


class multiThread(threading.Thread):
    def __init__(self, asin, cycle, status, twitter):
        threading.Thread.__init__(self)
        self.asin = asin
        self.cycle = int(cycle)
        self.check_status = status
        self.twitter = twitter
        self.url = "https://www.amazon.co.jp/dp/" + self.asin

    def run(self):
        while self.check_status:
            result = scraping.get_amazon_stock_status_by_asin(self.asin)
            self.twitter.tweet(self.url + "\n" + result)  # 他のクラスをそのまま引数として使用できるか？
            time.sleep(60 * self.cycle)

