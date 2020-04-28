import sqlite3
import csv

conn = sqlite3.connect('pokemon.sqlite')
cursor = conn.cursor()
#print('aaaaaa')
cursor.execute('DROP TABLE IF EXISTS moves')
#print('bbbbbb')
cursor.execute('PRAGMA foreign_keys = ON')

cursor.execute('''
CREATE TABLE "moves"(
    "move" TEXT,
    "move_type" INTEGER,
    "PP" INTEGER,
    "Power" INTEGER,
    "Accuracy" VarChar,
    FOREIGN KEY (move_type)
        REFERENCES types_table (type_1_id)
    )
    ''')
#print('ccccc')
with open('moves.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        if len(row) > 1:
            move=row[0]
            #print(type(move))
            move_type=row[1]
            type_id = 0
            if move_type =="Grass":
                type_id = 2
            elif move_type =="Fire":
                type_id = 3
            elif move_type =="Water":
                type_id = 4
            elif move_type =="Bug":
                type_id = 5
            elif move_type =="Normal":
                type_id = 6
            elif move_type =="Poison":
                type_id = 7
            elif move_type =="Electric":
                type_id = 8
            elif move_type =="Ground":
                type_id = 9
            elif move_type =="Fairy":
                type_id = 10
            elif move_type =="Fighting":
                type_id = 11
            elif move_type =="Psychic":
                type_id = 12
            elif move_type =="Rock":
                type_id = 13
            elif move_type =="Ghost":
                type_id = 14
            elif move_type =="Flying":
                type_id = 15
            elif move_type =="Dragon":
                type_id = 16
            elif move_type =="Dark":
                type_id = 17
            elif move_type =="Steel":
                type_id = 18
            elif move_type =="Ice":
                type_id = 19
            #print(type(move_type))
            PP=row[2]
            #type(type_1)
            Power=row[3]
            Accuracy=row[4]
            cursor.execute('''INSERT INTO moves(move, move_type,PP,Power,Accuracy)
                VALUES(?,?,?,?,?)''',(move,type_id,PP,Power,Accuracy))
            #
            conn.commit()