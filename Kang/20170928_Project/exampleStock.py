import pandas as pd
import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup
from pandas import Series, DataFrame
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import sqlite3

font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

def get_financial_data(code):
    url= "http://finance.naver.com/item/coinfo.nhn?code="+code+"&target=finsum_more"


    html = requests.get(url).text
    html = html.replace('  ', '')
    html = html.replace(',', '')
    soup = BeautifulSoup(html, 'lxml')

    date_list = [0,1,2,3,4,5,6,7]
    thead_data = soup.find_all('thead')
    thead_tr_data = thead_data[0].find_all('tr')
    thead_th_data = thead_tr_data[1].find_all('th')
    for i in range(8):
        date_list[i] = thead_th_data[i].text
        date_list[i] = date_list[i].replace('\t', '')
        date_list[i] = date_list[i].replace('\n', '')
        date_list[i] = date_list[i].replace('\r', '')
        date_list[i] = date_list[i].replace('(IFRS연결)', '')

    financial_data = {}
    data_temp_list = [0,1,2,3,4,5,6,7]
    tbody_data = soup.find_all('tbody')
    tbody_tr_data = tbody_data[0].find_all('tr')
    for j in range(32):
        tbody_th_data = tbody_tr_data[j].find_all('th')
        financial_name = tbody_th_data[0].text
        tbody_td_data = tbody_tr_data[j].find_all('td')
        for k in range(8):
            data_text = tbody_td_data[k].text
            r = re.search('.', data_text)
            if r:
                data_num = float(data_text)
            else:
                data_num = ''
            financial_data.setdefault(financial_name, []).append(data_num)
    financial_index = DataFrame(financial_data, columns=list(financial_data.keys()), index=date_list)
    financial_index.index.name = 'Date'
    #financial_index.rename(columns={'매출액':'Sales'}, inplace=True)
    save_data_sql(financial_index, code)
    return financial_index

def save_data_sql(data_frame, code):
    con = sqlite3.connect("D:/Project/Financial_Data.db")
    data_frame.to_sql(code, con, if_exists='replace')

if __name__ == "__main__":
    df = get_financial_data('068270')
    df[['매출액', 'BPS(원)']].plot()
    plt.show()

