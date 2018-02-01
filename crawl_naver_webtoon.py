# coding: utf8

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webtoon.settings')
import urllib
import requests
from bs4 import BeautifulSoup
from django.core.files import File

import django
django.setup()

from post.models import Webtoon

HOST = "http://comic.naver.com"

is_next = True
page = 1

while is_next:
    params = dict(
        titleId='20853',
        page='1'
    )

    url =  HOST + "/webtoon/list.nhn?titleId=20853&weekday=tue&page={}".format(page)
    res = requests.get(url, params=params)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    for tag_a in soup.select("table.viewList tr td.title a"):
        print(tag_a.text)
        title = tag_a.text

        webtoon = Webtoon(title=title)
        webtoon.save()

        print('saved #{}'.format(webtoon.pk))

    is_next = bool(soup.select('div.paginate a.next'))
    page += 1

