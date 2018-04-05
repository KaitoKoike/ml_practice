#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json
import re,sys,MeCab

#Consumer Key
CK = "*******************"
#ConsumerSecret Key
CS = "**********************"
#Access Token
AT = "*****************"
#Access Token Secret
AS = "**********************"
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


# 取得ツイートからノイズを削除
def arrangement_timeline(req_timeline):
    if req_timeline.status_code == 200:
        timeline = json.loads(req_timeline.text)
        timeline_texts = []
        for tweet in timeline:
            text = tweet["text"]
            text = re.sub("RT","",text)
            text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
            text = re.sub(r'@[\w…]+',"",text)
            text = re.sub("#","",text)
            text = re.sub("\n","",text)
            text = re.sub("\u3000","",text)
            text = re.sub(r':',"",text)
            text = re.sub(" ","",text)
            timeline_texts.append(text)
        print(timeline_texts)
        return timeline_texts
    else:
        print ("Error: %d" % req_timeline.status_code)

def wakati_text(texts):
    m = MeCab.Tagger("-Owakati")
    word_box = []
    text_box = []
    for i in range(len(texts)):
        text = m.parse(texts[i])
        words = text.split(" ")
        text_box.append(words)

    print(text_box)
    return text_box


if __name__ == "__main__":
    timeline_texts = arrangement_timeline(req_timeline)
    wakati_text(timeline_texts)
