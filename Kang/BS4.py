import requests
from bs4 import BeautifulSoup
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# HTTP GET Requeset
req = requests.get('http://fifaonline3.nexon.com/datacenter/player/list.aspx?ps=10&n4pageno=1')

# HTML
html = req.text

# HTML Header (200:success)
status = req.status_code

# HTTP ok ?
is_ok = req.ok

print(is_ok)

soup = BeautifulSoup(html, 'html.parser')

players = soup.select('#currentContent > main > div.datacenterContent > div.datacenterListWrapper > table > tbody tr')

data = []
for player in players:

    row= {}
    info = player.find('td',{'class':'info'})
    ability = player.find('td',{'class':'ability'})
    ovrs = ability.find('span',{'class':'ovr'})
    body = ability.find('span',{'class':'body'})


    row['name'] = info.a.strong.span.text
    row['price'] = info.find('span', {'class':'value'}).text
    row['pic'] = info.find('span',{'class','thumb'}).img['src']


    row['ability'] = {}
    row['ability']['overall'] = ability.find('span',{'class':'ovr'}).text
    row['ability']['body'] = {}
    row['ability']['body']["height"] =  body.find('span',{'class':'height'}).text
    row['ability']['body']["weight"] =  body.find('span',{'class':'weight'}).text
    row['ability']['body']["foot"] =  body.find('span',{'class':'foot'}).text
    row['ability']['body']["skill"] =  body.find('span',{'class':'skill'}).text

    row['stat'] = []
    row['stat'].append(player.find('td',{'class':'stat1'}).text)
    row['stat'].append(player.find('td',{'class':'stat2'}).text)
    row['stat'].append(player.find('td',{'class':'stat3'}).text)
    row['stat'].append(player.find('td',{'class':'stat4'}).text)
    row['stat'].append(player.find('td',{'class':'stat5'}).text)
    row['rating'] = player.find('td',{'class':'rating'}).text

    data.append(row)

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)