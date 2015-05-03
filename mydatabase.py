__author__ = 'Database'


#!/usr/bin/python
import pymysql
import sys
try:
 db = pymysql.connect(host="local", # your host, usually localhost
                      port=3306,
                      user="root", # your username
                      passwd=" ", # your password
                      db="python") # name of the data base

except Exception as e:
          sys.exit('we can not get database')

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT host, User FROM user")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print (row[0])

