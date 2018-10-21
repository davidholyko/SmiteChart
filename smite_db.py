import sqlite3
import json
from god_attributes_class import God_attributes

conn = sqlite3.connect("god_attributes.db")
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS god_attributes_table (
                name TEXT,
                siege INT,
                initiation INT,
                crowd_control INT,
                wave_clear INT,
                objective_damage INT,
                PRIMARY KEY (name))""")

c.execute(""" CREATE TABLE IF NOT EXISTS god_icon_table (
                name TEXT,
                godIcon_URL TEXT,
                godCard_URL TEXT,
                PRIMARY KEY (name))""")

# need to link primary keys name from gods icon table to attributes table_name

def insert_god(id):
    with conn:
        c.execute("INSERT OR IGNORE INTO god_attributes_table VALUES (:name, :siege, :initiation, :crowd_control, :wave_clear, :objective_damage)",
        {'name': id["name"],
         'siege': id["siege"],
         'initiation': id["initiation"],
         'crowd_control': id["crowd_control"],
         'wave_clear': id["wave_clear"],
         'objective_damage': id["objective_damage"]})

def insert_icon(id):
    with conn:
        c.execute("INSERT OR IGNORE INTO god_icon_table VALUES (:name, :godIcon_URL, :godCard_URL)",
        {'name': id,
         'godIcon_URL': id[0],
         'godCard_URL': id[1]})

def import_json(update = False):
    if (update == False):
        json_data = json.loads(open('god_attributes.json').read())

        for item in json_data:
            insert_god(item)

        json_data = json.loads(open('god_icon.json').read())

        for item in json_data:
            insert_icon(item)
        update = True
    else:
        pass

def get_all_by_table_name(table_name):
    c.execute("SELECT * FROM :table",  {"table" : table_name})
    return c.fetchall()

def update_table():
    # updates table if it needs to be updated
    pass

def get_elem(id, elem):

    def get_all(id):
        c.execute("SELECT * FROM god_attributes_table WHERE name = :god",  {"god" : id})
        return c.fetchone()

    def get_siege(id):
        return get_all(id)[1]

    def get_initiation(id):
        return get_all(id)[2]

    def get_crowd_control(id):
        return get_all(id)[3]

    def get_wave_clear(id):
        return get_all(id)[4]

    def get_objective_damage(id):
        return get_all(id)[5]

    methods =  {"siege" : get_siege(id),
                "initiation" : get_initiation(id),
                "crowd_control" : get_crowd_control(id),
                "wave_clear" : get_wave_clear(id),
                "objective_damage" : get_objective_damage(id),
                "all" : get_all(id),

                1 : get_siege(id),
                2 : get_initiation(id),
                3 : get_crowd_control(id),
                4 : get_wave_clear(id),
                5 : get_objective_damage(id),
                6 : get_all(id)}
    error_string = ""
    god_list = []

    json_data = json.loads(open('god_attributes.json').read())
    for item in json_data:
        god_list.append(item["name"])

    if id not in god_list:
        error_string += ('Name: "%s" is not in table' % id)
    if elem not in methods:
        error_string += ('\n%s is not a valid method' % elem)

    if len(error_string) > 1:
        return print(error_string)

    return methods.get(elem)

def get_stats(id):
    # gets all stats by name from db and puts into array
    stats = []
    for item in range(1,6):
        stats.append(get_elem(id,item))
    return stats
