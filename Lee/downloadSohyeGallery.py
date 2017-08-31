import random

import html
import urllib.request
import lxml
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

def download_web_images_noExtension(url):

    name = random.randrange(1, 1001)
    f = open( "./img/" + str(name) + '.jpg', 'wb')
    f.write(urllib.request.urlopen(url).read())
    f.close()

def find_by_xpath(element_source,xpath_expression):
    root = html.fromstring(element_source)
    return root.xpath(xpath_expression)



if __name__ == "__main__":

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("http://gall.dcinside.com/board/lists/?id=kimsohye")
    soup = BS(driver.page_source, 'html.parser')

    # f = open("./crawlWebpage.html", "wb")
    # f.write(soup.prettify().encode())
    # f.close()

    idx = 0

    for s in soup.find_all("a"):

        try:
            prop = s.get('class')
            if prop != None and prop[0] == "icon_pic_n":
                print(s.get('href') + " : " + s.get_text())
                url_info = s.get('href')

                if url_info[:4] != "http":
                    url_info = "http://gall.dcinside.com" + url_info

                print(url_info)

                driver.get(url_info)
                soup = BS(driver.page_source, 'html.parser')

                li = soup.find_all("li")
                print(1)

                for ele in li:
                    print(2)
                    val = ele.get('class')
                    if val != None and val[0] == 'icon_pic':
                        print(3)
                        base_url = ele.a.get("href")
                        rp_from = "http://image.dcinside.com/download.php"
                        rp_to = "http://dcimg7.dcinside.com/viewimage.php"
                        base_url = base_url.replace(rp_from, rp_to);
                        print(base_url)
                        f = open("./img/" + ele.a.contents[0], "wb");
                        img_req = urllib.request.Request(base_url);
                        f.write(urllib.request.urlopen(img_req).read())
                        f.close()

        except UnicodeEncodeError:
            print("Error : " + str(idx))
        finally:
            idx += 1




        # if ('href' in link.attrs and 'class' in link.attrs):
        #     if(eq(str(link.attrs['class']),'[\'icon_pic_n\']')):
        #         print(link.attrs['href'])
        #
        #         driver.find_element_by_xpath("// *[@href = \"" + link.attrs['href'] + "\"]").click()
        #
        #         time.sleep(1)
        #
        #         soup = BS(driver.page_source, 'html5lib')
        #
        #         imgs = soup.findAll("div", "app_editorno")
        #         "// *[ @ id = 'dgn_content_de'] / div[2] / div[1] / div / table / tbody / tr / td / div[2] / img"
        #
        #         for img in imgs:
        #
        #             imgurl = img.get_attribute("app_editorno")
        #             print(imgurl)




    driver.quit()




