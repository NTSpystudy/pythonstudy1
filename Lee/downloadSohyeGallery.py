import random

import urllib
from bs4 import BeautifulSoup as BS

from operator import eq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def download_web_images(url):
    user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"

    name = random.randrange(1,1001)
    full_name = str(name) + ".jpg"

    img_req = urllib.request.Request(url, data=None, headers={'User-Agent': user_agent});
    urllib.request.urlretrieve(img_req, "./img/" + full_name)



def download_web_images_no_extension(url):
    user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"

    name = random.randrange(1, 1001)
    f = open("./img/" + str(name) + ".jpg", "wb");
    img_req = urllib.request.Request(url, data=None, headers={'User-Agent': user_agent});

    f.write(urllib.request.urlopen(img_req).read())
    f.close()

    #
    # f = open( "./img/" + str(name) + '.jpg', 'wb')
    # f.write(urllib.request.urlopen(url).read())
    # f.close()


if __name__ == "__main__":

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("http://gall.dcinside.com/board/lists/?id=kimsohye")
    soup = BS(driver.page_source, 'html5lib')

    f = open("./crawlWebpage.html", "wb")
    f.write(soup.prettify().encode())
    f.close()

    for link in soup.findAll("a"):
        if ('href' in link.attrs and 'class' in link.attrs):
            if(eq(str(link.attrs['class']),'[\'icon_pic_n\']')):
                print(link.attrs['href'])
                driver.find_element_by_xpath("// *[@href = \"" + str(link.attrs['href']) + "\"]").click()

                time.sleep(1)

                soup = BS(driver.page_source, 'html5lib')
                imgs = driver.find_elements_by_xpath(
                    "// *[ @ id = 'dgn_content_de'] / div[2] / div[1] / div / table / tbody / tr / td / div / img")

                for img in imgs:
                    imgurl = img.get_attribute("src")
                    print(imgurl)

                    download_web_images(str(imgurl).encode())


    driver.quit()



