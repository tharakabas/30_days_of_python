# create table in mysql db

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydb")