import threading
from common import amazon_scraping
import time
import datetime


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
            result = amazon_scraping.get_amazon_stock_status_by_asin(self.asin)
            now = datetime.datetime.now()
            time_stamp = now.strftime("%Y/%m/%d %H:%M:%S")
            self.twitter.tweet(self.url + "\n" + result + "\n" + str(time_stamp))
            time.sleep(60 * self.cycle)
            print(result)

        # test用↓
        # while self.check_status:
        #     print(self.asin + " processing...")
        #     result = amazon_scraping.get_amazon_stock_status_by_asin(self.asin)
        #     time.sleep(30)
        # print("finished!!")

if __name__ == "__main__":
    # test = multiThread("B08GGGBKRQ", 60, True, "ok")
    # test.start()
    # test.join()
    # print("ok")
    pass
