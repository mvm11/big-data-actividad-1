import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# URL de la API
url = "https://datasets-server.huggingface.co/rows?dataset=Nicolybgs%2Fhealthcare_data&config=default&split=train&offset=0&length=100"

# Conexión a MongoDB
client = MongoClient("mongodb://user:root@localhost:27017/")
db = client["health-care"]
collection = db["diagnoses"]

# Obtener datos de la API
response = requests.get(url)
data = response.json()

# Ingresar datos a MongoDB
try:
    result = collection.insert_many(data)
    print(f'Data inserted with ids: {result.inserted_ids}')
except Exception as e:
    print(f'An error occurred: {e}')
finally:
    client.close()
