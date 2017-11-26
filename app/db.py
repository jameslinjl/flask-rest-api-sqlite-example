import base64
import sqlite3

DB_NAME = 'example.db'

def db_up():
	conn = sqlite3.connect(DB_NAME)

	c = conn.cursor()

	# db setup
	c.execute("CREATE TABLE file (id INTEGER PRIMARY KEY, file_name text, file_content_b64 text, deleted INTEGER)")

	# Insert a row of data
	body = (base64.b64encode('wassup'),)
	c.execute("INSERT INTO file VALUES (null, 'file.txt', ?, 0)", body)

	# Save (commit) the changes
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()

def db_execute(query, tuple_of_values):
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()
	c.execute(query, tuple_of_values)
	last_row_id = c.lastrowid
	conn.commit()
	conn.close()
	return last_row_id

def db_select(query, tuple_of_values, only_one=False):
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()
	if only_one:
		result = c.execute(query, tuple_of_values).fetchone()
	else:
		result = c.execute(query, tuple_of_values).fetchall()
	conn.close()

	return result
	