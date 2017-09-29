import requests
from bs4 import BeautifulSoup
import re
import sys


code = "068270"
url = "http://finance.naver.com/item/coinfo.nhn?code="+code+"&target=finsum_more"

url_ = requests.get(url)
plain_text = url_.text


soup = BeautifulSoup(plain_text, "lxml")
ranks = soup.find("dl", {"class": "cBk"})

if ranks == None:
    print("Unknown code(%s)" % code)
    exit(255)

print(ranks.get_text())
exit(0)
