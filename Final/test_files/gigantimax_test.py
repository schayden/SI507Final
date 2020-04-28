from bs4 import BeautifulSoup
import requests
import time
import re
url = "https://www.serebii.net/pokedex-sm/028.shtml"
#url = 'https://www.serebii.net/pokedex-swsh/corviknight/'
#url ='https://www.serebii.net/pokedex-swsh/rapidash/'
#url='https://www.serebii.net/pokedex-sm/053.shtml'

resposne = requests.get(url).text
soup = BeautifulSoup(resposne, 'html.parser')
l=[]
#for image in soup.find_all("img", src=re.compile('.gif')):
 #   print('')

a = soup.find_all("td", align = 'center')
#print(a[-1])
if "Galarian Form" or "Alolan Form" in a[-1]:
    g = soup.find_all("img", src=re.compile('.gif'))
    for t in g[:3]:
        if len(t['alt'])<15:
            print(t['alt'])
else:
    p_type=soup.find_all(class_='typeimg')
    t_list = []
    for t in p_type:
        t_list.append(t.get('alt'))
    if len(t_list) == 1:
        t_list.append("No second type")
    for t in t_list[:3]:
        t = (str(t))
        type_less = t.replace('-type', "")
        #e_list.append(type_less)
        print(type_less)

#g = soup.find_all("img", src=re.compile('.gif'))
#for t in g[:3]:
 #   if len(t['alt'])<15:
  #      print(t['alt'])



''''if "pokedex-sm" in url:
        name_soup = soup.find('font', width = "65%", size="4")
        print(name_soup)
        name = name_soup.find("b").text.strip()
    else:
        name_soup = 


         if soup.find_all('td', class_='fooevo', colspan="4") == []:
        search_index = -1
    for r in group_stat_soup[search_index]:
        c+=1
        if c==5:
            g_list = r.text.split('\n')
            hp = g_list[1]
            attack = g_list[2]
            defense = g_list[3]
            special_attack = g_list[4]
            special_defense = g_list[5]
            speed = g_list[6]'''