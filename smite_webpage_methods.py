from flask import Flask, render_template
from smite_db import *
from smite_json import *
from smite_plot import *
import sqlite3
import json

def make_chart(id):
  stats = get_stats_from_db(id)
  chart = make_radar_chart(id, stats)
  img = "/static/images/tmp/" + str(id) + ".png"
  return img

def icons():
    data = json.loads(open('god_icon.json').read())
    return data
