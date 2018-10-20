from god_attributes_class import God_attributes
import json

def make_raw_data_json(elem):
    with open('raw_data.json', "w") as f:
      gods = elem.get_gods()
      json.dump(gods, f)
      # makes json named data.json which contains all the info for all characters

def make_gods_json():
    with open("god_attributes.json", "w") as f:
      json_data = json.loads(open('raw_data.json').read())
      data = []
      gods_json = {}

      for item in json_data:
        data.append(God_attributes(item["Name"]).attributes)

      gods_json = json.dumps(data)
      json.dump(data, f, indent = 1)

def make_icon_json():
    with open("god_icon.json", "w") as f:
      json_data = json.loads(open('raw_data.json').read())
      data = []
      gods_json = {}

      for item in json_data:
        data.append({"name" : item["Name"],
                     "godIcon_URL": item["godIcon_URL"],
                     "godCard_URL": item["godCard_URL"]})
                     
      gods_json = json.dumps(data)
      json.dump(data, f, indent = 1)

#
# make_gods_json()
# make_icon_json()
