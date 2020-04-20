from bs4 import BeautifulSoup
import requests
import time
import re
import csv
url = "https://bulbapedia.bulbagarden.net/wiki/List_of_moves"
#url = 'https://www.serebii.net/pokedex-swsh/corviknight/'
#url ='https://www.serebii.net/pokedex-swsh/rapidash/'
#url='https://www.serebii.net/pokedex-sm/053.shtml'

resposne = requests.get(url).text
soup = BeautifulSoup(resposne, 'html.parser')

a = soup.find_all("body", class_="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-List_of_moves rootpage-List_of_moves skin-monobook action-view site-bulbapedia")
b = a[0].find('div', id='globalWrapper')
c = b.find('div', id ='column-content')
d = c.find('div', id='outercontentbox')
e = d.find('div', id='contentbox')
f = e.find('div', id='bodyContent', class_="mw-body-content")
g = f.find('div', id='mw-content-text')
h = g.find_all('table', class_='sortable roundy jquery-tablesorter')#, style='margin:auto; background: #ddf; border: 5px solid #ccf'


z=soup.findAll('table')[0].find_all('tr')
print(z[2].find_all('td')[1].text)
print(z[2].find_all('td')[2].text)
print(z[2].find_all('td')[5].text)
print(z[2].find_all('td')[6].text)
print(z[2].find_all('td')[7].text)

with open("moves.csv", "w+", encoding = "utf-8") as f:
    csv_content = csv.writer(f, delimiter=',')
    for s in z[2:798]:
        out_list = []
        out_list.append(s.find_all('td')[1].text.replace("\n",""))
        out_list.append(s.find_all('td')[2].text.replace("\n",""))
        out_list.append(s.find_all('td')[5].text.replace("\n",""))
        out_list.append(s.find_all('td')[6].text.replace("\n",""))
        out_list.append(s.find_all('td')[7].text.replace("\n",""))
        print(out_list)
        csv_content.writerow(out_list)
