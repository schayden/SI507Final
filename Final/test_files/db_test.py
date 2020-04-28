import sqlite3
typ = input("what pokemon ")
typ2 =typ.capitalize()
connection = sqlite3.connect("pokemon.sqlite")
cursor = connection.cursor()
q = f'''
        SELECT  name, Attack, Speed
        FROM pokemon_table
        WHERE type_1 OR type_2 = '{typ}'
        '''
result = cursor.execute(q).fetchall()
connection.close()
print(result)