from smite_db import *

# conn = sqlite3.connect("gods.db")
# c = conn.cursor()


# c.execute("SELECT * FROM gods")
# data = c.fetchall()

data = get_all()

print(data)
print(type(data))
# print(data)
conn.close()
