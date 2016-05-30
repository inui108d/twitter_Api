#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from requests_oauthlib import OAuth1Session

with open("secret.json") as f:
    secretjson = json.load(f)

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
params = {"status": "Hello, World!"}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(secretjson["CK"], secretjson["CS"], secretjson["AT"], secretjson["AS"])
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
