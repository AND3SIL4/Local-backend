from pymongo import MongoClient
import pymongo
from pprint import pprint
import os

try:
    # Conexión con la base de datos
    client = MongoClient("mongodb://localhost:27017/")

    # Seleccionar la base de datos
    db = client["covid19"]

    # Seleccionar la colección
    collection = db["casos"]

    print("All done...")

    consulta1 = {"Ciudad de ubicación": "Bogotá D.C."}
    consulta2 = {"Ciudad de ubicación": "Bogotá D.C.", "atención": "Recuperado"}
    consulta3 = [
        {"$match": {"atención": "Recuperado"}},
        {"$group": {"_id": "$Ciudad de ubicación", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 1},
    ]
    consulta4 = [
        {"$match": {"atención": "Recuperado", "Sexo": "F"}},
        {"$group": {"_id": "$Ciudad de ubicación", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 1},
    ]

    consulta5 = {"Sexo": "F", "Edad": {"$gt": 50}, "atención": "Fallecido"}
    consulta6 = {"Sexo": "M", "Edad": {"$lt": 50}, "atención": "Fallecido"}
    consulta7 = {"País de procedencia": {"$ne": None, "$exists": True}}
    consulta8 = {
        "Edad": {"$lt": 30},
        "País de procedencia": {"$ne": None, "$exists": True},
        "Departamento o Distrito ": "Antioquia",
    }
    consulta9 = {"País de procedencia": "ESPAÑA"}
    consulta10 = {"Edad": {"$gte": 20, "$lte": 50}}

    def menu():
        while True:
            print()
            print("Welcome to de menu of mongo db.")
            print("1 | Cuantos casos se registraron en Bogotá.")
            print("2 | Cuantos casos se recuperaron en Bogotá.")
            print("3 | Cual fue la ciudad en la que más se recuperaron.")
            print("4 | Cual fue la ciudad que más se recuperaron siendo mujeres.")
            print("5 | Cuantos fallecidos que fueron mujeres y mayores de 50 años.")
            print("6 | Cuantos fallecidos que fueron hombres y menores de 50 años.")
            print("7 | Cuantos casos fueron por personas del extranjero.")
            print(
                "8 | Cuantos casos registraron en Antioquía, menores de 30 años y por persona extranjeras."
            )
            print(
                "9 | Cuantos casos se registraron por personas de edad entre 20 y 50 años."
            )
            print("10 | Cuantos casos se registraron en Bogotá")
            print("0 | Para salir")
            enter = input("Chosee an option: ")
            if enter == "1":
                count = collection.count_documents(consulta1)
                print("Total casos: ", count)
                x = input("Quieres volver al menu? y/n ").upper()
                if x == "Y":
                    os.system("cls")
                    return menu()
                else:
                    os.system("cls")
                    break
            if enter == "2":
                count = collection.count_documents(consulta2)
                print("Total de casos: ", count)
                x = input("Quieres volver al menu? y/n ").upper()
                if x == "Y":
                    os.system("cls")
                    return menu()
                else:
                    os.system("cls")
                    break
            if enter == "3":
                result = collection.aggregate(consulta3)
                for doc in result:
                    pprint(doc)
                x = input("Quieres volver al menu? y/n ").upper()
                if x == "Y":
                    os.system("cls")
                    return menu()
                else:
                    os.system("cls")
                    break
            if enter == "4":
                result = collection.aggregate(consulta4)
                for doc in result:
                    pprint(doc)
                x = input("Quieres volver al menu? y/n ").upper()
                if x == "Y":
                    os.system("cls")
                    return menu()
                else:
                    os.system("cls")
                    break
            if enter == "5":
                count = collection.count_documents(consulta5)
                print("Total casos: ", count)
                x = input("Quieres volver al menu? y/n ").upper()
                if x == "Y":
                    os.system("cls")
                    return menu()
                else:
                    os.system("cls")
                    break
            if enter == "6":
                count = collection.count_documents(consulta6)
                print("Total casos: ", count)
                x = input("Quieres volver al menu? y/n ").upper()
                if x == "Y":
                    os.system("cls")
                    return menu()
                else:
                    os.system("cls")
                    break
            if enter == "7":
                count = collection.count_documents(consulta7)
                print("Total casos: ", count)
                x = input("Quieres volver al menu? y/n ").upper()
                if x == "Y":
                    os.system("cls")
                    return menu()
                else:
                    os.system("cls")
                    break
            if enter == "8":
                count = collection.count_documents(consulta8)
                print("Total casos: ", count)
                x = input("Quieres volver al menu? y/n ").upper()
                x = input("Quieres volver al menu? y/n ").upper()
                if x == "Y":
                    os.system("cls")
                    return menu()
                else:
                    os.system("cls")
                    break
            if enter == "9":
                count = collection.count_documents(consulta9)
                print("Total casos: ", count)
                x = input("Quieres volver al menu? y/n ").upper()
                x = input("Quieres volver al menu? y/n ").upper()
                if x == "Y":
                    os.system("cls")
                    return menu()
                else:
                    os.system("cls")
                    break
            if enter == "10":
                count = collection.count_documents(consulta10)
                print("Total casos", count)
                x = input("Quieres volver al menu? y/n ").upper()
                x = input("Quieres volver al menu? y/n ").upper()
                if x == "Y":
                    os.system("cls")
                    return menu()
                else:
                    os.system("cls")
                    break
            if enter == "0":
                print("Hasta la proxima bye...")
                os.system("cls")
                break
            else: 
                print("Opcion no valida, adios...")
                os.system("cls")
                break
    menu()

    # Cerrar la conexión
    client.close()
    print(f"Conexion a base de datos {db} cerrada con exito")

except pymongo.errors.PyMongoError as e:
    print("Error:", str(e))
