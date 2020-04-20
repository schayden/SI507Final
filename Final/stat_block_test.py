from bs4 import BeautifulSoup
import requests
import time
import re
url = "https://www.serebii.net/pokedex-sm/807.shtml"
#url = 'https://www.serebii.net/pokedex-swsh/corviknight/'
#url ='https://www.serebii.net/pokedex-swsh/rapidash/'
#url='https://www.serebii.net/pokedex-sm/053.shtml'

resposne = requests.get(url).text
soup = BeautifulSoup(resposne, 'html.parser')
l=[]
count = 807

group_stat_soup = soup.find_all(class_="dextable")
g_stats = {}
g_list = []
c = 1
hp = 0
attack = 0
defense = 0
special_attack = 0
special_defense = 0
speed = 0
#print(group_stat_soup[-13])
if "pokedex-sm" in url:
    search_index = -8 #for pokemon with mega evolutions
    if count == 6 or count ==150: #charizard has two mega forms
        search_index = -13
    elif count > 151 and count < 808: #for all pokemon not available in Let's Go Pikachu/Eevee
        search_index = -1
    elif soup.find_all('td', class_='fooevo', colspan='6') ==[]:
        search_index = -3 #for standard pokemon out of the sun and moon pokedex
    else:
        search_index = -2 #for gigantimaxing pokemon
        if soup.find_all('td', class_='fooevo', colspan="4") == []:
                search_index = -1 #for standard pokemon out of the SwSh dex
    #print(group_stat_soup[-3])
for r in group_stat_soup[search_index]:
    c+=1
    if c==5:
        g_list = r.text.split('\n')
        hp = g_list[1]
        attack = g_list[2]
        defense = g_list[3]
        special_attack = g_list[4]
        special_defense = g_list[5]
        speed = g_list[6]
print(f'HP = {hp}')
print(f'Attack = {attack}')
print(f'Defense = {defense}')
print(f'Special Attack = {special_attack}')
print(f'Special Defense = {special_defense}')
print(f'Speed = {speed}')