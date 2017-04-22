import json

import requests
from bs4 import BeautifulSoup
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/trendings')
def trendings():
    resposne = requests.get('https://github.com/trending')
    parsed_html = BeautifulSoup(resposne.content, 'html.parser')
    trending_list = []

    for index, tag in enumerate(parsed_html.select('.d-inline-block > h3 > a')):
        url = tag.get('href')
        trending_list.append({
            'id': int(index + 1),
            'name': url,
            'url': f'https://github.com{url}'
        })

    return json.dumps(trending_list)

'''
[
  {
    "id": 1,
    "name": "Leanne Graham",
    "url": ""
  },
'''