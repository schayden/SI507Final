import sqlite3
import csv

conn = sqlite3.connect('pokemon.sqlite')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS types_table')
cursor.execute('''
CREATE TABLE "types_table"(
    "id" INTEGER,
    "type_name" VarChar,
    PRIMARY KEY (id)
    )
    ''')

with open('pokemon_list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 1
    t_list = []
    for row in csv_reader:
        if len(row) > 1:
            print(row)
            id_number=count
            #print(type(id_number))
            name=row[1]
            #print(type(name))
            type_1=row[2]
            if type_1 not in t_list:
                t_list.append(type_1)
                count +=1
            cursor.execute('''INSERT or IGNORE INTO types_table(id,type_name)
                VALUES(?,?)''',(id_number, type_1))
            #
            conn.commit()
        