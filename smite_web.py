from flask import Flask, render_template
from smite_db import *
from smite_json import *
from smite_plot import *
import sqlite3

app = Flask(__name__)


@app.route("/test/")
def test():
    conn = sqlite3.connect("god_attributes.db")
    c = conn.cursor()

    c.execute("SELECT * FROM god_icon_table")
    all = c.fetchall()

    return render_template("test.html", all = all)


@app.route("/test/gods/<string:id>")
def char_test_page(id):
    conn = sqlite3.connect("god_attributes.db")
    c = conn.cursor()
    attributes = ["Name", "Siege", "Initiation", "Crowd Control", "Wave Clear", "Objective Damage"]

    c.execute("SELECT * FROM god_attributes_table WHERE name = :god", {"god" : id})
    god_name = c.fetchone()

    c.execute("SELECT * FROM god_icon_table WHERE name = :god", {"god" : id})
    all = c.fetchone()

    stats = get_stats_from_db(id)
    chart = make_radar_chart(id, stats)

    img = "/static/images/" + str(id) + ".png"

    return render_template('char_test_page.html', name = god_name, attr = attributes, all = all, stats = stats, img = img)


@app.route("/")
@app.route("/gods/")
def data():
    conn = sqlite3.connect("god_attributes.db")
    c = conn.cursor()

    c.execute("SELECT * FROM god_icon_table")
    all = c.fetchall()

    return render_template('home.html', all = all)

@app.route('/gods/<string:id>/')
def char_page(id):
    conn = sqlite3.connect("god_attributes.db")
    c = conn.cursor()
    attributes = ["Name", "Siege", "Initiation", "Crowd Control", "Wave Clear", "Objective Damage"]

    c.execute("SELECT * FROM god_attributes_table WHERE name = :god", {"god" : id})
    god_name = c.fetchone()

    c.execute("SELECT * FROM god_icon_table WHERE name = :god", {"god" : id})
    all = c.fetchone()

    stats = get_stats_from_db(id)

    return render_template('char_page.html', name = god_name, attr = attributes, all = all, stats = stats)

if __name__ == '__main__':
  app.run(debug = True)
