# connect to my sql db
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password"
)

print(mydb)