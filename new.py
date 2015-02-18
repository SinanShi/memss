# A minimal SQLite shell for experiments
# -*- coding: utf-8 -*-  
import sqlite3
import os, sys

def call_sqlite():
	con = sqlite3.connect(":memory:")
	con.isolation_level = None
	cur = con.cursor()

	buffer = ""

	print "Enter your SQL commands to execute in sqlite3."
	print "Enter a blank line to exit."

	while True:
		line = raw_input()
		if line == "":
			break
		buffer += line
		if sqlite3.complete_statement(buffer):
			try:
				buffer = buffer.strip()
				cur.execute(buffer)
	
				if buffer.lstrip().upper().startswith("SELECT"):
					print cur.fetchall()
			except sqlite3.Error as e:
				print "An error occurred:", e.args[0]
				buffer = ""

	con.close()



def create_memtable():
	conn = sqlite3.connect("DataBase/my_memory")
	c = conn.cursor()
    # Create table
	c.execute('''CREATE TABLE english_words(word text, translation text, usage text, origintxt text, origin text, time real)''')


def add_mem(loc_db,table_name):
	conn = sqlite3.connect(loc_db)
	c = conn.cursor()
	line="INSERT INTO %s VALUES('abdfgoidfg ','sdfsdfyy','sdfsdfa','速度','大放送',3)" % table_name
	c.execute(line)
	# Save (commit) the changes
	conn.commit()
	conn.close()

def display_all(loc_db,table_name,order):
	conn = sqlite3.connect(loc_db)
	c = conn.cursor()
	line = "SELECT * FROM %s ORDER BY %s" % (table_name,order)
	#c.execute('SELECT * FROM table_name ORDER BY word')
	c.execute(line)
	rows = c.fetchall()
	print len(rows)
	for row in rows:
		print "%2s| %-10s| %-10s| %-10s| %-10s| %-10d|" % row
	conn.close()


location="DataBase/my_memory"
table="english_words"
order="word"
#create_memtable()
#add_mem(location,table)
display_all(location,table,"word")



#git test
