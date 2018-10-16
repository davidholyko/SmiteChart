from god_attributes import God_attributes
import json

def make_raw_data_json(elem):
    with open('raw_data.json', "w") as f:
      gods = elem.get_gods()
      json.dump(gods, f)
      # makes json named data.json which contains all the info for all characters

def make_gods_json():
    with open("gods.json", "w") as f:
      json_data = json.loads(open('raw_data.json').read())
      data = []
      gods_json = {}

      for item in json_data:
        data.append(God_attributes(item["Name"]).attributes)

      gods_json = json.dumps(data)
      json.dump(data, f, indent = 1)

def make_icon_json():
    with open("gods_icon.json", "w") as f:
      json_data = json.loads(open('raw_data.json').read())
      data = []
      gods_json = {}

      for item in json_data:
        data.append({"Name" : item["Name"],
                    "godIcon_URL": item["godIcon_URL"]})

      gods_json = json.dumps(data)
      json.dump(data, f, indent = 1)
