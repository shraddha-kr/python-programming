# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('test.db')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()


# Display columns
print('\nColumns in GEEKS table:')
data=cursor.execute('''SELECT * FROM GEEKS''')
for column in data.description:
	print(column[0])
	
# Display data
print('\nData in EMPLOYEE table:')
data=cursor.execute('''SELECT * FROM GEEKS''')
for row in data:
	print(row)
	
# Commit your changes in the database	
conn.commit()

# Closing the connection
conn.close()
