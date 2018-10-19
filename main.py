from smite_api import *
from smite_json import *
from smite_db import *
import json

API_call = SmiteClient()
# gets api info put back later
make_raw_data_json(API_call)
# makes raw_data.json
make_gods_json()
# makes god_attributes.json
make_icon_json()
#makes god_icon.json
import_json()
# updates table by converting json to table
update_table()
# doesnt do anything right now
