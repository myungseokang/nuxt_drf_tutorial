import requests
import json
from bs4 import BeautifulSoup

from django.http import HttpResponse


def trending_list(request):
    count = int(request.GET.get('count', 5))
    language = request.GET.get('lang', '')

    resposne = requests.get(f'https://github.com/trending/{language}')
    parsed_html = BeautifulSoup(resposne.content, 'html.parser')

    trending_list = []
    star_list = parsed_html.select('.muted-link.mr-3')
    today_star_list = parsed_html.select('span.float-right')
    link_list = parsed_html.select('.d-inline-block > h3 > a')[:count]

    for index, tag in enumerate(link_list):
        star_idx = index * 2
        star_cnt = star_list[star_idx].text.strip('\n ')
        today_star = today_star_list[index].text.strip('\n ')
        url = tag.get('href')

        trending_list.append({
            'id': int(index + 1),
            'name': url[1:],
            'url': f'https://github.com{url}',
            'star_cnt': star_cnt,
            'today_star': today_star,
        })
    return HttpResponse(json.dumps(trending_list))
