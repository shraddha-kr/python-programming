"""
Normally, the above code snippet would work perfectly fine. But when the database is already being used by another process, it’d have to wait until that process’s query is resolved before executing its own query. If that waiting time crosses the connection timeout value, then that results in a Connection Timeout.
The default value for connection timeout is 5 seconds. But it can be changed in the connect() method itself. It accepts an optional parameter timeout which accepts the value for connection timeout in seconds. 
https://www.geeksforgeeks.org/change-sqlite-connection-timeout-using-python/
"""
# import module
import sqlite3

try:
	# establish connection
	sqliteConnection = sqlite3.connect('test.db', timeout=20)

	# create cursor object
	cursor = sqliteConnection.cursor()
	print('Database Initialization and Connection successful')

	# display version
	query = 'select sqlite_version();'
	cursor.execute(query)

	# get data
	record = cursor.fetchall()
	print(f'SQLite Version - {record}')
	cursor.close()

except sqlite3.Error as error:
	print('Error occurred - ', error)

finally:
	
	# If the connection was established then
	# close it
	if sqliteConnection:
		sqliteConnection.close()
		print('SQLite Connection closed')
