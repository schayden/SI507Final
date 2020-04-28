import sqlite3
import csv

conn = sqlite3.connect('pokemon.sqlite')
cursor = conn.cursor()
cursor.execute('PRAGMA foreign_keys = ON')
cursor.execute('DROP TABLE IF EXISTS pokemon_table')
cursor.execute('''
CREATE TABLE "pokemon_table"(
    "id_number" INTEGER,
    "name" VarChar,
    "type_1_id" INTEGER,
    "type_2" VarChar,
    "ALTERNATIVE_TYPE" VarChar,
    "stat_total" INTEGER,
    "HP" INTEGER,
    "Attack" INTEGER,
    "Defense" INTEGER,
    "Special_Attack" INTEGER,
    "Special_Defense" INTEGER,
    "Speed" INTEGER,
    FOREIGN KEY (type_1_id)
        REFERENCES types_table (id)
    )
    ''')

with open('final_test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        type_1_id = 0
        type_2_id = 0
        alt_type_id = 0
        if len(row) > 1:
            print(row)
            id_number=row[0]
            #print(type(id_number))
            name=row[1]
            #print(type(name))
            type_1=row[2]
            if type_1 =="Grass":
                type_1_id = 2
            elif type_1 =="Fire":
                type_1_id = 3
            elif type_1 =="Water":
                type_1_id = 4
            elif type_1 =="Bug":
                type_1_id = 5
            elif type_1 =="Normal":
                type_1_id = 6
            elif type_1 =="Poison":
                type_1_id = 7
            elif type_1 =="Electric":
                type_1_id = 8
            elif type_1 =="Ground":
                type_1_id = 9
            elif type_1 =="Fairy":
                type_1_id = 10
            elif type_1 =="Fighting":
                type_1_id = 11
            elif type_1 =="Psychic":
                type_1_id = 12
            elif type_1 =="Rock":
                type_1_id = 13
            elif type_1 =="Ghost":
                type_1_id = 14
            elif type_1 =="Flying":
                type_1_id = 15
            elif type_1 =="Dragon":
                type_1_id = 16
            elif type_1 =="Dark":
                type_1_id = 17
            elif type_1 =="Steel":
                type_1_id = 18
            elif type_1 =="Ice":
                type_1_id = 19
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
            cursor.execute('''INSERT INTO pokemon_table(id_number, name,type_1_id,type_2,ALTERNATIVE_TYPE,stat_total,HP,Attack,Defense,Special_Attack,Special_Defense,Speed)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''',(id_number, name,type_1_id,type_2,Alternative_type,stat_total,HP,Attack,Defense,Special_Attack,Special_Defense,Speed))
            #
            conn.commit()