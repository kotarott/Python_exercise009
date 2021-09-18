# Python_exercise009
Twitter連携  
amazonの在庫状況を確認してツイートするアプリケーション  
  
## 参考
[参考サイト](https://tech-blog.rakus.co.jp/entry/20201106/api)  
  

## インストール
以下のライブラリのインストールを行う。  
>pip install tweepy  
>pip install python-dotenv  
>pip install eel  
>pip install selenium  
>pip install webdriver_manager  
>pip install pandas  
  

## ファイルの準備
.envファイルをトップに作成  
以下の情報を記載する。  
>CONSUMER_KEY = [自分のキー]  
>CONSUMER_SECRET = [自分のキー]  
>ACCESS_TOKEN = [自分のキー]  
>ACCESS_TOKEN_SECRET = [自分のキー]  
  

### memo
処理の起動・更新・停止機能を入れる。  
複数商品の在庫状況を決まった時間ごとに監視（マルチスレッド）  
↑クラスにしたスレッドにインスタンス変数が変わらなければ、同じ処理を繰り返し続けるようにする。  
