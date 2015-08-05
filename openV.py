#!/usr/bin/python

# sudo apt-get install python-mysqldb
# ./mysql-db-create.sh openVdev openVuser openVpw
# ./mysql-db-create.sh testDBname testDBuser testDBpass
# mysql -u openVuser -popenVpw openVdev
# http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python
import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="openVuser", # your username
                      passwd="openVpw", # your password
                      db="openVdev") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM bible")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]	