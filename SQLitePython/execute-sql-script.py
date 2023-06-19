# import sqlite3 module
import sqlite3

# create con object to connect
# the database geeks_db.db
con = sqlite3.connect("test.db")

# create the cursor object
cur = con.cursor()

# execute the script by creating the table
# named geeks1 and insert the data
cur.executescript("""
        create table geeks1(
        geek_id,
        geek_name,
        address
    );
insert into geeks values ( '7058', 'sravan kumar','hyd' );
insert into geeks values ( '7059', 'Jyothika' ,'ponnur' );
insert into geeks values ( '7072', 'Harsha','chebrolu' );
insert into geeks values ( '7075', 'Deepika','tenali' );
	
	""")

# display the data in the table by
# executing the cursor object
cur.execute("SELECT * from geeks")

# fetch all the data
print(cur.fetchall())
