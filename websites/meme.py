from flask import Flask, render_template
import requests
from flask import request
from flask import jsonify

import json
app = Flask(__name__)


def get_mem():
    #sr = "wholesomememes"
    #url = "https://www.reddit.com/r/" + sr + "/hot.json"
    url = "https://meme-api.herokuapp.com/gimme/50"
    response = json.loads(requests.request("GET",url).text)
    #response1 = json.dumps(requests.get("https://meme-api.herokuapp.com/gimme").json())
    #response1 = json.dumps({  "count": 2,  "memes": [    {      "postLink": "https://redd.it/ji1riw",      "subreddit": "wholesomememes",      "title": "It makes me feel good.",      "url": "https://i.redd.it/xuzd77yl8bv51.png",      "nsfw": "true",      "spoiler": "true",      "author": "polyesterairpods",      "ups": 306,      "preview": [        "https://preview.redd.it/xuzd77yl8bv51.png?width=108&crop=smart&auto=webp&s=9a0376741fbda988ceeb7d96fdec3982f102313e",        "https://preview.redd.it/xuzd77yl8bv51.png?width=216&crop=smart&auto=webp&s=ee2f287bf3f215da9c1cd88c865692b91512476d",        "https://preview.redd.it/xuzd77yl8bv51.png?width=320&crop=smart&auto=webp&s=88850d9155d51f568fdb0ad527c94d556cd8bd70",        "https://preview.redd.it/xuzd77yl8bv51.png?width=640&crop=smart&auto=webp&s=b7418b023b2f09cdc189a55ff1c57d531028bc3e"      ]    },    {      "postLink": "https://redd.it/jibifc",      "subreddit": "wholesomememes",      "title": "It really feels like that",      "url": "https://i.redd.it/vvpbl29prv51.jpg",      "nsfw": "true",      "spoiler": "true",      "author": "lolthebest",      "ups": 188,      "preview": [        "https://preview.redd.it/vvpbl29prev51.jpg?width=108&crop=smart&auto=webp&s=cf64f01dfaca5f41c2e87651e4b0e321e28fa47c",        "https://preview.redd.it/vvpbl29prev51.jpg?width=216&crop=smart&auto=webp&s=33acdf7ed7d943e1438039aa71fe9295ee2ff5a0",        "https://preview.redd.it/vvpbl29prev51.jpg?width=320&crop=smart&auto=webp&s=6a0497b998bd9364cdb97876aa54c147089270da",        "https://preview.redd.it/vvpbl29prev51.jpg?width=640&crop=smart&auto=webp&s=e68fbe686e92acb5977bcfc24dd57febd552afaf",        "https://preview.redd.it/vvpbl29prev51.jpg?width=960&crop=smart&auto=webp&s=1ba690cfe8d49480fdd55c6daee6f2692e9292e7",        "https://preview.redd.it/vvpbl29prev51.jpg?width=1080&crop=smart&auto=webp&s=44852004dba921a17ee4ade108980baab242805e"      ]    }  ]})
    #response = json.loads(response1)
    meme_pic = response["memes"][1]["preview"][-1]
    subriddit = response["memes"][0]['subreddit']
    return meme_pic, subriddit
def get_ip():
    #return jsonify({'ip': request.remote_addr}), 200
    #return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
    #return request.environ['REMOTE_ADDR']
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    else:
        return (request.environ['HTTP_X_FORWARDED_FOR'])

@app.route('/')
def index():
    ip = get_ip()
    meme_pic, subriddit = get_mem()
    return render_template('meme_index.html', meme_pic=meme_pic, subriddit=subriddit, ip=ip)
    #
app.run(host="0.0.0.0", port=80)
