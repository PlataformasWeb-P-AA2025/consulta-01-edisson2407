from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["demo_base"]
coleccion = db["informacion_excel"]

print("1. Ganadores que perdieron al menos un set")

consulta = {"Lsets": {"$gt": 0}}

for doc in coleccion.find(consulta):
    print(f"{doc['Winner']} vs {doc['Loser']} | Sets ganados/perdidos: {doc['Wsets']}-{doc['Lsets']}")
