from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	
	try:
		bsObj = BeautifulSoup(html.read(), "html.parser")
		#title = bsObj.findAll("dt").a
		for title in bsObj.findAll("dt"):
			#if 'title' in title.a:
			print(title.a['title'])
				
	except AttributeError as e:
		return None
	return title

title = getTitle("http://movie.naver.com/movie/preview/index.nhn")
if title == None:
	print("Title could not be found")
else:
	print("That is all")