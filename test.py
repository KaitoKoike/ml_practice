#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json
import re

#Consumer Key
CK = "KF9FB8laqgKBxwdDi3jYjoqNQ"
#ConsumerSecret Key
CS = "HCk4TbAyUceNOoKekR1JrDnTA5GPw40iy2xAjgwcWVTry37XHG"
#Access Token
AT = "472864471-1viPEeSMNheFb3VK3aCQ0MzgQh883DrFFnPDc44O"
#Access Token Secret
AS = "jjj2ksiZpTOCD4TU03uips2YkYVIm0vgii0xFERVYmbMl"
# ツイート投稿用のURL
url_tweet = "https://api.twitter.com/1.1/statuses/update.json"
#タイムライン取得用URL
url_timeline = "https://api.twitter.com/1.1/statuses/home_timeline.json"
# ツイート本文
params_tweet = {"status": "Hello, World!"}

twitter = OAuth1Session(CK, CS, AT, AS)


# OAuth認証で POST method で投稿
#req_post = twitter.post(url_tweet, params = params_tweet)

# OAuth認証で GET method でタイムラインの取得
req_timeline = twitter.get(url_timeline,params = {})

# レスポンスを確認
if req_timeline.status_code == 200:
    timeline = json.loads(req_timeline.text)
    for tweet in timeline:
        text = tweet["text"]
        text = re.sub("RT","",text)
        text = re.sub("#","",text)
        text = re.sub("\n","",text)
        text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
        text = re.sub(r'@[\w…]+',"",text)
        text = re.sub(r':',"",text)
        text = re.sub(" ","",text)
        print("text = ",text)
else:
    print ("Error: %d" % req_timeline.status_code)
