import amazon_scraping as ama

def test_get_amazon_items():
    res = ama.get_amazon_items("PS5")
    assert len(res) > 0


if __name__ == "__main__":
    test_get_amazon_items()