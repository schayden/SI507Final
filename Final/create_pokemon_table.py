import sqlite3
import csv

conn = sqlite3.connect('pokemon.sqlite')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS pokemon')
cursor.execute('''
CREATE TABLE "pokemon"(
    "id_number" INTEGER,
    "name" VarChar,
    "type_1" VarChar,
    "type_2" VarChar,
    "Alternative_type" VarChar,
    "stat_total" VarChar,
    "HP" VarChar,
    "Attack" TEXT,
    "Defense" TEXT,
    "Special_Attack" VarChar,
    "Special_Defense" VarChar,
    "Speed" VarChar
    )
    ''')

with open('final_test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        if len(row) > 1:
            id_number=row[0]
            print(type(id_number))
            name=row[1]
            #print(type(name))
            type_1=row[2]
            #type(type_1)
            type_2=row[3]
            Alternative_type=row[4]
            stat_total=row[5]
            HP=row[6]
            Attack=row[7]
        #print(type(Attack))
            D=row[8]
            Defense = ''.join(str(D))
        #print(type(Defense))
            Special_Attack=row[9]
            Special_Defense=row[10]
            Speed=row[11]
            cursor.execute('''INSERT INTO pokemon(id_number, name,type_1,type_2,Alternative_type,stat_total,HP,Attack,Defense,Special_Attack,Special_Defense,Speed)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''',(id_number, name,type_1,type_2,Alternative_type,stat_total,HP,Attack,Defense,Special_Attack,Special_Defense,Speed))
            #
            conn.commit()