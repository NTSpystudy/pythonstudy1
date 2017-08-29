# -*- coding: cp949 -*-

import requests
from bs4 import BeautifulSoup
import urllib


html = urllib.request.urlopen('http://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(html,"lxml")
titles = soup.find_all("a","title")

for title in titles:
	print("제목= {}\n".format(title['title']))