from collections import OrderedDict
from itertools import count
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

def get_list(title_id):
    list_url = 'http://comic.naver.com/webtoon/list.nhn'
    ep_dict = OrderedDict()
    for page in count(1):
        params = {'titleId': title_id, 'page': page}
        print('try {}'.format(params))

        list_html = requests.get(list_url, params=params).text
        soup = BeautifulSoup(list_html, 'html.parser')

        for tag in soup.select('.viewList tr td.title'):
            tag_a = tag.find('a')
            is_up = bool(tag.find('img'))
            link = urljoin(list_url, tag_a['href'])
            title = tag_a.text
            print(title, is_up, link, img_url)

            if link in ep_dict:
                return ep_dict

            ep = {
                'title': title,
                'is_up': is_up,
                'link': link,
                'img_url': img_url,
            }
            ep_dict[link] = ep
