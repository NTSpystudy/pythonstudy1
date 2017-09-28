# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:01:20 2017

@author: NAVER
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from operator import eq
from bs4 import BeautifulSoup as BS
import urllib.request

import time

receiver = "test_lee3@naver.com"
sender = "test_lee2@naver.com"

receiverId = "test_lee3"
senderId = "test_lee2"

receiverPw = "naver!23"
senderPw = "naver!23"

tmpTime = ""

driver = webdriver.Chrome("chromedriver.exe")

def logIn(Id, Pw):
    driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div[1]/div/a/span").click()
    waitForIsElementPresent("//*[@id='id']")

    driver.find_element_by_xpath("//*[@id='id']").send_keys(Id)
    driver.find_element_by_xpath("//*[@id='pw']").send_keys(Pw)

    driver.find_element_by_xpath("//*[@id='frmNIDLogin']/fieldset/input").click();


def logOut():
    driver.find_element_by_xpath("//*[@id='gnb_name1']").click()
    driver.find_element_by_xpath("//*[@id='gnb_logout_button']/span[3]").click()


def waitForIsElementPresent(xpath):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        print(xpath, "가 존재하지 않습니다.")
        driver.close()


def basicWriting():
    driver.find_element_by_xpath("//*[@id='toInput']").send_keys(receiver)

    time.sleep(1)

    driver.find_element_by_xpath("//*[@id='atcp']/ul/li/div/a").click()
    driver.find_element_by_xpath("//*[@id='subject']").click()

    curTime = time.strftime("%Y%m%d %H%M%S", time.localtime())
    tmpTime = curTime

    driver.find_element_by_xpath("//*[@id='subject']").send_keys(curTime)
    driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='se2_iframe']"))
    driver.find_element_by_xpath("/html/body").send_keys(curTime)

    driver.switch_to_default_content()


# 캡챠 노출하게 하기
def searchCAPTCHA(num):
    driver.find_element_by_xpath("//*[@id='nav_snb']/div[1]/a[1]/strong").click()
    waitForIsElementPresent("//*[@id='toInput']")

    basicWriting()

    driver.find_element_by_xpath("//*[@id='sendBtn']").click()

    isCaptcha = driver.find_element_by_xpath("//*[@id='capchaDiv']/div/div/h4").text
    print(isCaptcha)

    if eq(isCaptcha, "스팸메일 발송 방지 확인"):
        nowtime = time.strftime("%Y%m%d %H%M%S", time.localtime())

        for i in range(1, num+1):
            # CAPTCHA img Url 받아오기
            img = driver.find_element_by_xpath("//*[@id='capchaImg']")
            imgUrl = img.get_attribute("src")

            # CAPTCHA img 저장
            urllib.request.urlretrieve(imgUrl, "./CAPTCHA/" + str(i) + "_" + str(nowtime) + ".png")

            # 이미지 새로고침 클릭
            driver.find_element_by_xpath("//*[@id='capchaDiv']/div/div/div/div[1]/a/span").click()



if __name__ == "__main__":

    driver.get("http://mail.naver.com")
    logIn(senderId, senderPw)
    searchCAPTCHA(1000)
    driver.close()


