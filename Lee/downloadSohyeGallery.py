import random
import urllib.request as url
from bs4 import BeautifulSoup as BS
import base64

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download_web_images(url):
    name = random.randrange(1,1001)
    full_name = str(name) + ".jpg"
    url.urlretrieve(url, "./img/" + full_name)


if __name__ == "__main__":

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("http://gall.dcinside.com/board/lists/?id=kimsohye")
    soup = BS(driver.page_source, 'html5lib')

    f = open("./crawlWebpage.html", "wb")
    f.write(soup.prettify().encode())
    f.close()

    for link in soup.findAll("a"):
        if ('href' in link.attrs & 'class' in link.attrs):

            print(link.attrs['href'])


    driver.quit()



