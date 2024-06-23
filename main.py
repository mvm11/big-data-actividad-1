from pymongo import MongoClient
import pandas as pd

# Conexión a MongoDB
client = MongoClient('mongodb://user:root@localhost:27017/')
db = client['health-care']
collection = db['diagnostics']

# Carga de datos (asumiendo que los datos están en un CSV)
data = pd.read_csv('healthcare_data.csv')
data_dict = data.to_dict("records")
collection.insert_many(data_dict)

# Verificación de la carga de datos
for doc in collection.find().limit(5):  # Muestra los primeros 5 documentos
    print(doc)
