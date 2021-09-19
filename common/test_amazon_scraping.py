import amazon_scraping as ama

thread_list = ["A"]

def test_get_amazon_items():
    res = ama.get_amazon_items("PS5", 1)
    assert len(res) > 0

def test_get_amazon_stock_status_by_asin():
    res = ama.get_amazon_stock_status_by_asin("B08GGGBKRQ")
    assert res == "在庫なし"

def test_thread():
    thread_list.append("B")
    print(thread_list)

if __name__ == "__main__":
    test_get_amazon_items()
    # test_get_amazon_stock_status_by_asin()
    # test_thread()
    # print(thread_list)