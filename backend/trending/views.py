import requests
import json
from bs4 import BeautifulSoup

from django.http import HttpResponse


def trending_list(request):
    count = int(request.GET.get('count', 0))
    language = request.GET.get('lang', '')

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
    return HttpResponse(json.dumps(trending_list))
