import requests
from bs4 import BeautifulSoup

list_url = 'http://comic.naver.com/webtoon/list.nhn'
params = {
	'titleId': 650305, #호랑이형님
	'page': 1,
}
html = requests.get(list_url, params=params).text
soup = BeautifulSoup(html, 'html.parser')

for tag in soup.select('.viewList tr'):
	try:
		a_tag = tag.select('a[href*=detail.nhn')[0]
	except IndexError:
		continue

	print(a_tag)