# Install mysql on your computer 
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '2002'
)

# Prepare a cursor 
cursorObject = dataBase.cursor()

# Create a data base
cursorObject.execute("CREATE DATABASE elderco")
print("All done...")
