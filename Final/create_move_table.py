import sqlite3
import csv

conn = sqlite3.connect('pokemon.sqlite')
cursor = conn.cursor()
print('aaaaaa')
cursor.execute('DROP TABLE IF EXISTS moves')
print('bbbbbb')

cursor.execute('''
CREATE TABLE "moves"(
    "move" TEXT,
    "move_type" VarChar,
    "PP" INTEGER,
    "Power" INTEGER,
    "Accuracy" VarChar
    )
    ''')
print('ccccc')
with open('moves.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        if len(row) > 1:
            move=row[0]
            print(type(move))
            move_type=row[1]
            print(type(move_type))
            PP=row[2]
            #type(type_1)
            Power=row[3]
            Accuracy=row[4]
            cursor.execute('''INSERT INTO moves(move, move_type,PP,Power,Accuracy)
                VALUES(?,?,?,?,?)''',(move,move_type,PP,Power,Accuracy))
            #
            conn.commit()