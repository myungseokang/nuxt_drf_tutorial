import json

import requests
from bs4 import BeautifulSoup
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/trendings', methods=['GET'])
def trendings():
    count = int(request.args.get('count'))
    language = request.args.get('lang')
    print(count)
    print(language)
    resposne = requests.get(f'https://github.com/trending/{language}')
    parsed_html = BeautifulSoup(resposne.content, 'html.parser')
    trending_list = []
    link_list = parsed_html.select('.d-inline-block > h3 > a')[:count]

    for index, tag in enumerate(link_list):
        url = tag.get('href')
        trending_list.append({
            'id': int(index + 1),
            'name': url,
            'url': f'https://github.com{url}'
        })

    return json.dumps(trending_list)
