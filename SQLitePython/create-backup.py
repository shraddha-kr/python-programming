import sqlite3
import io
conn = sqlite3.connect('test.db')

# Open() function
with io.open('testdb_dump.sql', 'w') as p:
		
	# iterdump() function
	for line in conn.iterdump():
		
		p.write('%s\n' % line)
	
print(' Backup performed successfully!')
print(' Data Saved as testdb_dump.sql')

conn.close()
