import eel
import desktop
# import multi_thread
import common.amazon_scraping as ama

app_name = "web"
end_point = "index.html"
size = (600,700)

@ eel.expose
def get_item_list(search_keyword):
    return ama.get_amazon_items(search_keyword, 1)




desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)

# if __name__ == "__main__":
#     df = get_news_title("ro", "欧州市場サマリー")
