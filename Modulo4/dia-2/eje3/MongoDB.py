from pymongo import MongoClient
from bson.json_util import dumps

uri = "mongodb+srv://nasarzzz:cI7iTlm4xyq5OnlN@cluster0.kiptamo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(uri)
    db = client["mongoDB"]
    collection = db['clientes']
    result = collection.update_one(
        {"nombre":"Ana"},
        {"$set":{"email":"anaActualizada@gmail.com"}}
    )
    if result :
        print(collection.find_one({"nombre":"Ana"}))
    
    result = collection.delete_one({"nombre":"luis"})
    if result :
        print(result)
    

    clientes_con_varios_pedidos = collection.find({
        "$expr": {"$gt": [{"$size": "$pedidos"}, 1]}
    })

    print("\nClientes con más de un pedido:")
    for doc in clientes_con_varios_pedidos:
        print(dumps(doc, indent=2)) 
    
    collection.create_index("email")
    print("\Índice creado en el campo 'email'")

except Exception as e:
    print("Error al conectar a MongoDB:", e)

# db = client["mongoDB"]
# coleccion = db["clientes"]

# clientes = [
#     {
#         "nombre": "Ana",
#         "email": "ana@email.com",
#         "pedidos": [
#             {"pedido_id": 101, "fecha": "2025-05-20"},
#             {"pedido_id": 102, "fecha": "2025-05-22"}
#         ]
#     },
#     {
#         "nombre": "Luis",
#         "email": "luis@email.com",
#         "pedidos": [
#             {"pedido_id": 103, "fecha": "2025-05-21"}
#         ]
#     }
# ]

# try:
#     coleccion.insert_many(clientes)
#     print("Documentos insertados.")
# except Exception as e:
#     print("Error al insertar documentos:", e)