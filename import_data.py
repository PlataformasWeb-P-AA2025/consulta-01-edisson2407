import pandas as pd
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["demo_base"]
coleccion = db["informacion_excel"]

# Leer y guardar los archivos Excel
archivos = ["data/2022.xlsx", "data/2023.xlsx"]

for archivo in archivos:
    df = pd.read_excel(archivo)
    datos = df.to_dict(orient="records")
    coleccion.insert_many(datos)

print("Datos insertados correctamente desde archivos Excel.")
