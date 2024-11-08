# install MYSQL on the computer
# pip install mysql
# pip install mysql-connector or mysql-connector-python
# pip install mysql-client

import mysql.connector

database = mysql.connector.connect(
    host ='localhost',
    user ='Ratnesh',
    passwd ='Ratnesh@18',
)

# prepare cursor object

cursorObject = database.cursor()

# create a database

cursorObject.execute("CREATE DATABASE IF NOT EXISTS crm_database")

print("ALL DONE")