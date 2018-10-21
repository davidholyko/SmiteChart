from flask import Flask, render_template
from smite_db import *
from smite_json import *
from smite_plot import *
from smite_webpage_methods import *
import sqlite3

app = Flask(__name__)


@app.route("/test/")
def test():
    data = icons()
    return render_template("test.html",  data = data)


@app.route("/test/gods/<string:id>")
def char_test_page(id):
    conn = sqlite3.connect("god_attributes.db")
    c = conn.cursor()
    attributes = ["Name", "Siege", "Initiation", "Crowd Control", "Wave Clear", "Objective Damage"]

    c.execute("SELECT * FROM god_attributes_table WHERE name = :god", {"god" : id})
    god_name = c.fetchone()

    c.execute("SELECT * FROM god_icon_table WHERE name = :god", {"god" : id})
    all = c.fetchone()

    img = make_chart(id)

    return render_template('char_test_page.html', name = god_name, attr = attributes, all = all, img = img)


@app.route("/")
@app.route("/gods/")
def data():
    data = icons()
    return render_template('home.html', data = data)

@app.route('/gods/<string:id>/')
def char_page(id):
    conn = sqlite3.connect("god_attributes.db")
    c = conn.cursor()
    attributes = ["Name", "Siege", "Initiation", "Crowd Control", "Wave Clear", "Objective Damage"]

    c.execute("SELECT * FROM god_attributes_table WHERE name = :god", {"god" : id})
    god_name = c.fetchone()

    c.execute("SELECT * FROM god_icon_table WHERE name = :god", {"god" : id})
    all = c.fetchone()

    img = make_chart(id)

    return render_template('char_page.html', name = god_name, attr = attributes, all = all, img = img)

if __name__ == '__main__':
  app.run(debug = True)
