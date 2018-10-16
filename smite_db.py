import sqlite3
import json
from god_attributes import God_attributes

conn = sqlite3.connect("god_attributes.db")
c = conn.cursor()
update = False

c.execute(""" CREATE TABLE IF NOT EXISTS god_attributes_table (
                name TEXT,
                siege INT,
                initiation INT,
                crowd_control INT,
                wave_clear INT,
                objective_damage INT,
                PRIMARY KEY (name))""")

def insert_god(id):
    with conn:
        c.execute("INSERT OR REPLACE INTO god_attributes_table VALUES (:name, :siege, :initiation, :crowd_control, :wave_clear, :objective_damage)",
        {'name': id["name"],
         'siege': id["siege"],
         'initiation': id["initiation"],
         'crowd_control': id["crowd_control"],
         'wave_clear': id["wave_clear"],
         'objective_damage': id["objective_damage"]})

def import_json(update):
    if (update == False):
        json_data = json.loads(open('gods.json').read())

        for item in json_data:
            insert_god(item)
        update = True
    else:
        pass

def get_all():
    c.execute("SELECT * FROM god_attributes_table")
    return c.fetchall()

def get_siege(id):
    c.execute("SELECT siege FROM god_attributes_table where name = :god",  {"god" : id})
    return c.fetchall()

def get_initiation(id):
    c.execute("SELECT initiation FROM god_attributes_table where name = :god",  {"god" : id})
    return c.fetchall()

def get_crowd_control(id):
    c.execute("SELECT crowd_control FROM god_attributes_table where name = :god",  {"god" : id})
    return c.fetchall()

def get_wave_clear(id):
    c.execute("SELECT wave_clear FROM god_attributes_table where name = :god",  {"god" : id})
    return c.fetchall()

def get_objective_damage(id):
    c.execute("SELECT objective_damage FROM god_attributes_table where name = :god",  {"god" : id})
    return c.fetchall()

def update_table():
    # updates table if it needs to be updated
    pass

def get_elem(id, elem):
    if elem == "siege":
        return get_siege(id)
    if elem == "initiation":
        return get_initiation(id)
    if elem == "crowd_control":
        return get_crowd_control(id)
    if elem == "wave_clear":
        return get_wave_clear(id)
    if elem == "objective_damage":
        return get_objective_damage(id)
    else:
        print("Element is not in table")
        pass


import_json(update)
update_table() #checks if table needs to be updated then updates
# 
# print(get_all())
# # #
# # conn.close()
