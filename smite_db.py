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
        {'name': id["name"],
         'godIcon_URL': id["godIcon_URL"],
         'godCard_URL': id["godCard_URL"]})

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

def get_all():
    c.execute("SELECT * FROM god_icon_table")
    return c.fetchall()

def get_all_by_table_name(table_name):
    #gets all by records by table name
    pass

def update_table():
    # updates table if it needs to be updated
    pass

def get_elem(id, elem):
    # returns item in form "(x,)"

    def get_siege(id):
        c.execute("SELECT siege FROM god_attributes_table WHERE name = :god",  {"god" : id})
        return c.fetchone()

    def get_initiation(id):
        c.execute("SELECT initiation FROM god_attributes_table WHERE name = :god",  {"god" : id})
        return c.fetchone()

    def get_crowd_control(id):
        c.execute("SELECT crowd_control FROM god_attributes_table WHERE name = :god",  {"god" : id})
        return c.fetchone()

    def get_wave_clear(id):
        c.execute("SELECT wave_clear FROM god_attributes_table WHERE name = :god",  {"god" : id})
        return c.fetchone()

    def get_objective_damage(id):
        c.execute("SELECT objective_damage FROM god_attributes_table WHERE name = :god",  {"god" : id})
        return c.fetchone()

    methods = {"siege" : get_siege(id), "initiation" : get_initiation(id), "crowd_control" : get_crowd_control(id), "wave_clear" : get_wave_clear(id), "objective_damage" : get_objective_damage(id)}
    error_string = ""
    god_list = []

    json_data = json.loads(open('god_attributes.json').read())
    for item in json_data:
        god_list.append(item["name"])

    if id not in god_list:
        error_string += ('Name: "%s" is not in table' % id)
    if elem not in methods:
        error_string += ('\n "elem": %s is not a valid method' % elem)

    if len(error_string) >= 1:
        print(error_string)

    return methods.get(elem)

def get_stats(id):
    # gets all stats by name from db and puts into array
    pass


#
# print(get_all())
