from flask import Flask, render_template
from smite_db import *
import sqlite3

app = Flask(__name__)

@app.route("/test/")
def test():
    conn = sqlite3.connect("god_attributes.db")
    c = conn.cursor()

    c.execute("SELECT * FROM god_icon_table")
    all = c.fetchall()

    return render_template("home.html", all = all)

@app.route("/")
@app.route("/gods/")
def data():
    conn = sqlite3.connect("god_attributes.db")
    c = conn.cursor()
    c.execute("SELECT * FROM god_attributes_table")
    gods_list = c.fetchall()

    return render_template('data.html', data = gods_list)

@app.route('/gods/<string:id>/')
def char_page(id):
    conn = sqlite3.connect("god_attributes.db")
    c = conn.cursor()
    c.execute("SELECT * FROM god_attributes_table WHERE name = :god", {"god" : id})
    god_name = c.fetchone()

    c.execute("SELECT godIcon_URL FROM god_icon_table WHERE name = :god", {"god" : id})
    god_icon = c.fetchone()

    c.execute("SELECT godCard_URL FROM god_icon_table WHERE name = :god", {"god" : id})
    god_card = c.fetchone()

    c.execute("SELECT * FROM god_icon_table WHERE name = :god", {"god" : id})
    all = c.fetchone()

    attributes = ["Name", "Siege", "Initiation", "Crowd Control", "Wave Clear", "Objective Damage"]

    return render_template('char_page.html', name = god_name, attr = attributes, icon = god_icon, card = god_card, all = all)

if __name__ == '__main__':
  app.run(debug = True)
