from smite_api import SmiteClient
from smite_data import *
import json



devID = "2787";
authKey = "693A2C5633AE4479B35620D485D1FF2E";


test = SmiteClient(devID, authKey)
# gets api info put back later
make_raw_data_json(test)
# makes raw_data.json
make_gods_json()
# makes gods.json
make_icon_json()
