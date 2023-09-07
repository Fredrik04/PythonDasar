#import library
import mysql.connector

#membuat koneksi ke database
mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="database"
)

#melakukan operasi pada database
mycursor = mydb.cursor()
mycursor.execute(SELECT * FROM customers)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#menutup koneksi database
mydb.close()

