from pymongo import MongoClient

uri = "mongodb+srv://user:pass@cluster0.kiptamo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(uri)
    print(client.list_database_names())  # Muestra las bases de datos disponibles
    print("¡Conexión exitosa!")
except Exception as e:
    print("Error al conectar:", e)
