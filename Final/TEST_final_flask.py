
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_results(sort_by, sort_order, filter_type, in_name, num, move_name, table_select):
    conn = sqlite3.connect('pokemon.sqlite')
    cur = conn.cursor()
    where_clause = ''
    num = str(num)
    select_clause = ''
    from_clause = ''
    join_clause=''
    if table_select=='pokemon':
        select_clause=
    if in_name != "":
        name = in_name.capitalize()
        where_clause = f'WHERE name = "{name}"'
        q = f'''
        SELECT id_number, name, type_name, type_2, Alternative_type, stat_total, HP, Attack, Defense, Special_Attack,Special_Defense,Speed
        FROM pokemon_table
        JOIN types_table
            ON pokemon_table.type_1_id = types_table.id
        {where_clause}
        '''
    elif num != '':
        num = int(num)
        where_clause =f"WHERE id_number = '{num}'"
        q = f'''
        SELECT id_number, name, type_name, type_2, Alternative_type, stat_total, HP, Attack, Defense, Special_Attack,Special_Defense,Speed
        FROM pokemon_table
        JOIN types_table
            ON pokemon_table.type_1_id = types_table.id
        {where_clause}
        '''
    elif num =='' and in_name =='':
        if (filter_type != 'All'):
            where_clause = f'WHERE type_2 = "{filter_type}" OR type_name = "{filter_type}"'
        q = f'''
        SELECT id_number, name, type_name, type_2, Alternative_type, stat_total, HP, Attack, Defense, Special_Attack,Special_Defense,Speed
        FROM pokemon_table
        JOIN types_table
            ON pokemon_table.type_1_id = types_table.id
        {where_clause}
        ORDER BY {sort_by} {sort_order}
        LIMIT 10
        '''
    results = cur.execute(q).fetchall()
    conn.close()
    #print(q, "aaa")
    return results
#ORDER BY {sort_by} {sort_order}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    sort_by = request.form['sort']
    print(sort_by)
    sort_order = request.form['dir']
    print(sort_order)
    filter_type = request.form['region']
    print(filter_type)
    name = request.form['name']
    print(name)
    num = request.form['num']
    print(num)
    table_select = request.form['table_select']
    results = get_results(sort_by, sort_order, filter_type, name, num)
    print(results)
    return render_template('results.html',
        sort=sort_by, results=results)

if __name__ == '__main__':
    app.run(debug=True)