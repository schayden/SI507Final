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

move_table=soup.findAll('table')[0].find_all('tr')
print(move_table[2].find_all('td')[1].text)
print(move_table[2].find_all('td')[2].text)
print(move_table[2].find_all('td')[5].text)
print(move_table[2].find_all('td')[6].text)
print(move_table[2].find_all('td')[7].text)

with open("moves.csv", "w+", encoding = "utf-8") as f:
    csv_content = csv.writer(f, delimiter=',')
    for s in move_table[2:798]:
        out_list = []
        out_list.append(s.find_all('td')[1].text.replace("\n",""))
        out_list.append(s.find_all('td')[2].text.replace("\n",""))
        out_list.append(s.find_all('td')[5].text.replace("\n",""))
        out_list.append(s.find_all('td')[6].text.replace("\n",""))
        out_list.append(s.find_all('td')[7].text.replace("\n",""))
        print(out_list)
        csv_content.writerow(out_list)
