import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('test.db')

# cursor object
cursor_obj = connection_obj.cursor()

print("Count of Rows")
cursor_obj.execute("SELECT * FROM GEEKS")
print(len(cursor_obj.fetchall()))

connection_obj.commit()

# Close the connection
connection_obj.close()
