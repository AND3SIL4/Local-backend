# print("HOLA MI PERRO\n")

# nombre=input("Ingrese su nombre mi perro: ")
# edad=int(input("Ingrese su edad mi perro: "))

# print (f"Usted se llama", nombre, "y tiene", edad, "años")

# print ("HOLA")

import mysql.connector

db = mysql.connector.connect(
    user = 'root',
    password = '2002',
    host ='localhost',
    database='laboratorio_sql',
    port='3306',
)

cursor = db.cursor()
cursor.execute('SHOW TABLES')
# print(cursor)
db.close()