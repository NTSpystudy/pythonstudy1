import random

import urllib
import urllib.request
from bs4 import BeautifulSoup as BS

from operator import eq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def download_web_images(url):
    name = random.randrange(1,1001)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, "./img/" + full_name)

def download_web_images_noExtension(url):


    name = random.randrange(1, 1001)
    f = open( "./img/" + str(name) + '.jpg', 'wb')
    f.write(urllib.request.urlopen(url).read())
    f.close()

if __name__ == "__main__":

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("http://gall.dcinside.com/board/lists/?id=kimsohye")
    soup = BS(driver.page_source, 'html5lib')

    # f = open("./crawlWebpage.html", "wb")
    # f.write(soup.prettify().encode())
    # f.close()

    for link in soup.findAll("a"):
        if ('href' in link.attrs and 'class' in link.attrs):
            if(eq(str(link.attrs['class']),'[\'icon_pic_n\']')):
                print(link.attrs['href'])
                driver.find_element_by_xpath("// *[@href = \"" + link.attrs['href'] + "\"]").click()

                time.sleep(1)

                soup = BS(driver.page_source, 'html5lib')
                imgs = driver.find_elements_by_xpath("// *[ @ id = 'dgn_content_de'] / div[2] / div[1] / div / table / tbody / tr / td / div / img")

                for img in imgs:
                    imgurl = img.get_attribute("src")
                    print(imgurl)

                    download_web_images_noExtension(imgurl)



    driver.quit()




