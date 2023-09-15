import mysql.connector

DataBase= mysql.connector.connect(
    host = ' localhost',
    user = 'root',
    passwd= 'passiton'
)

cursorObject= DataBase.cursor()

cursorObject.execute("CREATE DATABASE JDCO")

