# from smite_db import *
from smite_webpage_methods import *

# conn = sqlite3.connect("gods.db")
# c = conn.cursor()


# c.execute("SELECT * FROM gods")
# # data = c.fetchall()
#
# data = get_all()
#
# print(data)
# print(type(data))
# # print(data)
# conn.close()

# error_string = "444"
#
# if len(error_string) > 1:
#     raise error_string

#
# dict = {"thing" : {
#         "one": 3,
#         "33" : 4}}
#
# print(dict["thing"])

data = icons()

print(data["Agni"]["godCard_URL"])
