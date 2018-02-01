import requests
from bs4 import BeautifulSoup

list_url = 'http://comic.naver.com/webtoon/list.nhn'
params = {
    'titleId' : 20853,
    'page': 1,
}

html = requests.get(list_url, params=params).text
soup = BeautifulSoup(html, 'html.parser')

print('test')
for tag in soup.select('.viewList tr'):
    try:
        a_tag = tag.select('a[href*=detail.nhn]')[0]
    except IndexError:
        continue
        
    img_tag = a_tag.find('img')
    
    ep_url = a_tag['href']
    ep_name = img_tag['title']
    img_url = img_tag['src']
    
    print(ep_name, img_url, ep_url)