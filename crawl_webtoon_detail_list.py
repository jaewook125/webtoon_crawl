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
titleId = 650305

while is_next: #페이지의끝 = False이면 멈춤
    params = dict(
        titleId=titleId, #웹툰 아이디
        page=page, #페이지네이션
    )

    url =  HOST + "/webtoon/list.nhn?titleId={}&page={}".format(titleId,page)
    res = requests.get(url, params=params)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    for tag_a in soup.select("table.viewList tr > td:nth-of-type(1)"):
        #뷰리스트 tr보다 하위인것
        tag_img = tag_a.find('img')
        #img태그를 찾는다
        if tag_img:
            #img태그일때
            title = tag_img['title']
            #img-title만 찾아서 출력
            image = tag_img['src']
            #img-src만 찾아서 출력
            img_name = os.path.basename(image.split('?')[0])
            #문자열을 ?로 나눈다음 이미지파일을 열어준다
            img_res = requests.get(image, stream=True)
            #이미지 src를 얻어온다
            print(title, image)
            
            # webtoon = Webtoon(title=title)
            # #모델 대입
            # webtoon.image.save(img_name, File(img_res.raw))
            # #문자열로 이미지src url을 받아와서 webtoon-image에 저장
            # webtoon.save()

            # print('saved #{}'.format(webtoon.pk))

    is_next = bool(soup.select('div.paginate a.next')) #NEXT = True
    page += 1

#마음의 소리의 배너에 title이 없기때문에 크롤링 아직 못함