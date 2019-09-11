from requests_oauthlib import OAuth1Session
import json,config
import janome

"""
・検索語を入力して、対応するtweetを取得する
    ・ANDとかOR検索にも対応させる
・形態素解析する
・共起ネットワークで可視化する
・PNGとかで出力
"""

ck=config.CONSUMER_KEY
cs=config.CONSUMER_SECCRET
at=config.ACCESS_TOKEN
ats=config.ACCESS_TOKEN_SECRET
twitter=OAuth1Session(ck,cs,at,ats)

url="https://api.twitter.com/1.1/statuses/user_timeline.json"

params={"count":5}
res=twitter.get(url,params=params)
json.loads(res.text)
type(res)
json.loads(res[0].text)


url="https://api.twitter.com/1.1/search/tweets.json"
#reference...https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
params={"q":"最果てのバベル 詫び","count":5,"result_type":"recent"}
res=twitter.get(url,params=params)
json.loads(res.text)

