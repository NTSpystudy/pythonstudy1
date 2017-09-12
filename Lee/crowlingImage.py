import random

import urllib.request
import re
from bs4 import BeautifulSoup as BS

from selenium import webdriver

# class AppURLopener(urllib.request.FancyURLopener):
#     version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36"

user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"




if __name__ == "__main__":

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("http://gall.dcinside.com/board/lists/?id=kimsohye")
    soup = BS(driver.page_source, 'html.parser')

    print(2)
    for s in soup.find_all("a"):
        print(2)
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

                imgs = soup.findAll("img" , {"src" : re.compile('dcimg.[.]')})
                print(1)

                for img in imgs:
                    name = random.randrange(1, 1001)
                    print(2)
                    imgUrl = img.get("src")
                    print(imgUrl)

                    filename = "./img/" + str(name) + ".jpg"

                    img_req = urllib.request.Request(imgUrl, data=None, headers={'User-Agent': user_agent});
                    # urllib.request.urlretrieve(img_req, filename)

                    f = open(filename, 'wb');
                    f.write(urllib.request.urlopen(img_req).read())
                    f.close()





        except UnicodeEncodeError:
            print("Error")

    driver.quit()