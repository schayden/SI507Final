from bs4 import BeautifulSoup
import requests
import time
import re

#url = "https://www.serebii.net/pokedex-swsh/bulbasaur/"
#url = 'https://www.serebii.net/pokedex-swsh/corviknight/'
url = 'https://www.serebii.net/pokedex-sm/001.shtml'
#url='https://www.serebii.net/pokedex-sm/806.shtml'
#url = 'https://www.serebii.net/pokedex-sm/028.shtml'
#url ='https://www.serebii.net/pokedex-sm/808.shtml'
import csv

count = 1
with open("final_test.csv", "w+", encoding = "utf-8") as f:
    csv_content = csv.writer(f, delimiter = ',')
    csv_content.writerow(['id_number', 'name', 'type_1', 'type_2', 'alternative_types','stat_total', 'HP', 'Attack', 'Defense', 'Special Attack', 'Special Defense', 'Speed'])

    while count < 891: #when count <5, stops at #4
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'html.parser')
        e_list = []
    #get pokemon name
        if "pokedex-sm" in url:
            name_soup = soup.find('font', size="4")
        #print(name_soup)
            name = name_soup.find("b").text
        else:
            name_soup = soup.find('td', width = "65%")
            name = name_soup.find("h1").text.strip()
        n_list = name.split(" ")
        n_1 = n_list[0].replace('#', '')
        n_2 = int(n_1)
        if len(n_list) == 3:
            split_name = n_list[1]+n_list[2]
        else:
            split_name = n_list[1]
        print("Count is ", (str(count)))
        print("Number", str(n_2))
        e_list.append(n_2)
        print(split_name)
        e_list.append(split_name)


#get pokemon type
        center_aligned = soup.find_all("td", align = 'center')
        if "Galarian Form" or "Alolan Form" in center_aligned[-1]:
            t_list = []
            g = soup.find_all("img", src=re.compile('.gif'))
            for t in g[:3]:
                if len(t['alt'])<15:
                    typ = (t['alt'])
                    type_less = typ.replace('-type','')
                    t_list.append(type_less)
            if len(t_list) == 1:
                    t_list.append("No second type")
                    t_list.append("No alternate type")
            elif len(t_list) == 2:
                    t_list.append("No alternate type")
            for t in t_list[:3]:
                    t = (str(t))
                    e_list.append(t)
                    print(t)
        else:
            p_type=soup.find_all(class_='typeimg')
            t_list = []
            for t in p_type:
                t_list.append(t.get('alt'))
            if len(t_list) == 1:
                t_list.append("No second type")
            elif len(t_list) == 2:
                t_list.append("No alternate type")
            for t in t_list[:2]:
                t = (str(t))
                type_less = t.replace('-type', "")
                e_list.append(type_less)
                print(type_less)

#gets base stat total
        try:
            base_stat_soup = soup.find('td', colspan="2", width='14%', class_='fooinfo')
            base_stat = base_stat_soup.text.strip()
        except:
            base_stat_soup = soup.find('td', colspan="3", width='14%', class_='fooinfo')
            base_stat = base_stat_soup.text.strip()
        str_total = (str(base_stat))
        stripped_total = str_total.replace("Base Stats - Total: ", "")
        total = int(stripped_total)
        e_list.append(total)
        print(total)

#individual stats

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
            if n_2 == 6 or n_2 ==150: #charizard has two mega forms
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
        e_list.append(hp)
        e_list.append(attack)
        e_list.append(defense)
        e_list.append(special_attack)
        e_list.append(special_defense)
        e_list.append(speed)


    
        csv_content.writerow(e_list)
#get link to next page
        if count == 809:
            url = 'https://www.serebii.net/pokedex-swsh/grookey/'
        else:
            link = soup.find(width = "50%", align = "right")
            center = link.find('td', align="center")
            a = center.find('a')['href']
            url = 'https://www.serebii.net'+a
        print(url)
        time.sleep(2)
        count +=1
        print('''
    
    ''')


#print(name)
#for t in t_list:
#    print(t)
#print(next_url)