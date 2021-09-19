import os
from numpy import NaN
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd
import datetime
from webdriver_manager.chrome import ChromeDriverManager


# Chromeを起動する関数
def set_driver(driver_path, headless_flg):
    if "chrome" in driver_path:
        options = ChromeOptions()
    else:
        options = Options()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    if "chrome" in driver_path:
        return Chrome(ChromeDriverManager().install(), options=options)
    else:
        return Firefox(executable_path=os.getcwd()  + "/" + driver_path,options=options)

# 検索ワードから商品リストを作成
def get_amazon_items(keyword, page):
    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)
    
    try:
        url = "https://www.amazon.co.jp/s?k=" + keyword + "&page=" + str(page) + "&__mk_ja_JP=" + "カタカナ" + "&ref=nb_sb_noss_1"
        driver.get(url)
        time.sleep(5)

        search_results = driver.find_elements_by_css_selector(".s-result-item")
        items = get_item_list(search_results)
    finally:
        driver.quit()
        
    return list(items["asin"]), list(items["img"]), list(items["name"]), list(items["url"])

# amazonの商品在庫確認
def get_amazon_stock_status_by_asin(asin_code):
    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)
    
    url = "https://www.amazon.co.jp/dp/" + asin_code
    driver.get(url)
    time.sleep(3)

    # buy-now-button　の有無で確認する
    try:
        buy_button = driver.find_element_by_id("buy-now-button")
        driver.quit()
        return "在庫あり"
    except:
        driver.quit()
        return "在庫なし"

def get_item_list(results):
    df = pd.DataFrame()
    for i, result in enumerate(results):
        result_type = result.get_attribute("data-component-type")
        if result_type == "s-search-result":
            item_asin = result.get_attribute("data-asin")
            item_detail = result.find_element_by_css_selector(".s-image-square-aspect .s-image")
            item_img = item_detail.get_attribute("src")
            item_name = item_detail.get_attribute("alt")
            item_url = "https://www.amazon.co.jp/dp/" + item_asin
            # item_price = result.find_element_by_css_selector("span.a-price-whole")
            # print(item_price)
            # try:
            #     item_price = result.find_element_by_css_selector("span.a-price-whole").text
            # except:
            #     item_price = "なし"
            df = df.append(
                {
                    "asin": item_asin,
                    "img": item_img,
                    "name": item_name,
                    "url": item_url,
                    # "price": item_price
                },
                ignore_index=True
            )
    return df

def get_links(news_titles):
    news_links = []
    for news_title in news_titles:
        a_tag = news_title.find_element_by_tag_name("a")
        link = a_tag.get_attribute("href")
        news_links.append(link)
    return news_links

# CSV作成関数
def create_csv(data, file_name="company_list.csv"):
    num = 0
    while num == 0:
        if os.path.exists(file_name):
            print(f"ファイル名{file_name}は存在します。")
            num = 0
            file_name = input("ファイル名を入力してください >>>")
            file_name += ".csv"
        else:
            data.to_csv(file_name)
            create_log(f'ファイル名:{file_name} を作成しました。')
            return print("ファイルを作成しました。")

def create_folder(folder_name="articles"):
    if os.path.exists(folder_name):
        return
    else:
        os.mkdir(folder_name)

# ログ作成関数
def create_log(comment):
    path = "log.csv"
    now = datetime.datetime.now()
    time_stamp = now.strftime("%Y/%m/%d %H:%M:%S")
    logs = ','.join([time_stamp, comment])

    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(logs)
    else:
        with open(path, 'a', encoding='utf-8') as f:
            f.write('\n' + logs)


if __name__ == "__main__":
    get_amazon_items("PS5", 2)