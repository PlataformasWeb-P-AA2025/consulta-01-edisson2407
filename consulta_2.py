from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["demo_base"]
coleccion = db["informacion_excel"]

print("2. Partidos donde el favorito (AvgW < 2.0) ganó")

consulta = {"AvgW": {"$lt": 2.0}}

for doc in coleccion.find(consulta):
    print(f"{doc['Winner']} vs {doc['Loser']} | AvgW: {doc['AvgW']}")