import amazon_scraping as ama

def test_get_amazon_items():
    res = ama.get_amazon_items("PS5")
    assert len(res) > 0

def test_get_amazon_stock_status_by_asin():
    res = ama.get_amazon_stock_status_by_asin("B08GGGBKRQ")
    assert res == "在庫なし"

if __name__ == "__main__":
    test_get_amazon_items()
    # test_get_amazon_stock_status_by_asin()