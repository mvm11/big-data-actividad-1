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

# Asegurarse de que 'data' contiene una lista de diccionarios bajo la clave 'rows'
if "rows" in data and isinstance(data["rows"], list) and all(isinstance(item, dict) for item in data["rows"]):
    print("Data is a list of dictionaries under the key 'rows'.")
    # Ingresar datos a MongoDB si la lista no está vacía
    if data["rows"]:
        try:
            result = collection.insert_many(data["rows"])
            print("Data successfully inserted.")
            # Imprimir los primeros cinco documentos de la colección
            print("First five documents in the collection:")
            for doc in collection.find().limit(5):
                print(doc)
        except Exception as e:
            print(f'An error occurred: {e}')
    else:
        print("No data to insert. The list is empty.")
else:
    print("Data format is incorrect or not a list of dictionaries under the key 'rows'.")

# Cerrar la conexión a la base de datos
client.close()
