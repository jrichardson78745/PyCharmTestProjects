#!/usr/bin/python

import MySQLdb

username = input("What is the username to connect?")
pwd = input("What is the password to use?")

# Open database connection
db = MySQLdb.connect("localhost",username,pwd,"phpmyadmin" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version: %s " % data)

# disconnect from server
db.close()
