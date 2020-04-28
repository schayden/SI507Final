
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_results(sort_by, sort_order, filter_type, in_name, num, table_select, return_limit):
    conn = sqlite3.connect('pokemon.sqlite')
    cur = conn.cursor()
    where_clause = ''
    num = str(num)
    select_clause = ''
    from_clause = ''
    join_clause=''
    limit_clause = f"LIMIT {return_limit}"
    if table_select=='pokemon':
        select_clause='SELECT id_number, name, type_name, type_2, Alternative_type, stat_total, HP, Attack, Defense, Special_Attack,Special_Defense,Speed'
        from_clause='FROM pokemon_table'
        join_clause='''JOIN types_table
            ON pokemon_table.type_1_id = types_table.id'''
    else:
        select_clause = "SELECT move, type_name, PP, Power, Accuracy"
        from_clause = "FROM moves"
        join_clause='''JOIN types_table
                        ON moves.move_type = types_table.id
        '''
    if in_name != "":
        name = in_name
        if " " in name:
            name = name.replace(" ","_")
        name = name.capitalize()
        if table_select == 'pokemon':
            where_clause = f'WHERE name = "{name}"'
        else:
            where_clause = f'WHERE move = "{name}"'
        q = f'''
        {select_clause}
        {from_clause}
        {join_clause}
        {where_clause}
        '''
    elif num != '':
        num = int(num)
        where_clause =f"WHERE id_number = '{num}'"
        q = f'''
        {select_clause}
        {from_clause}
        {join_clause}
        {where_clause}
        '''
    elif num =='' and in_name =='':
        if table_select=='pokemon':
            order_clause = f''
            if (filter_type != 'All'):
                where_clause = f'WHERE type_2 = "{filter_type}" OR type_name = "{filter_type}"'
        else:
            if (filter_type != 'All'):
                where_clause=f'WHERE type_name = "{filter_type}"'
        q = f'''
        {select_clause}
        {from_clause}
        {join_clause}
        {where_clause}
        ORDER BY {sort_by} {sort_order}
        {limit_clause}
        '''
    results = cur.execute(q).fetchall()
    conn.close()
    print(q, "aaa")
    print(results)
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
    filter_type = request.form['filter_type']
    print(filter_type)
    name = request.form['name']
    print(name)
    num = request.form['num']
    print(num)
    table_select = request.form['table_select']
    return_limit = request.form['limit']
    results = get_results(sort_by, sort_order, filter_type, name, num, table_select, return_limit)
    print(results)
    return render_template('results.html',
        sort=sort_by, results=results, table_select=table_select)

if __name__ == '__main__':
    app.run(debug=True)