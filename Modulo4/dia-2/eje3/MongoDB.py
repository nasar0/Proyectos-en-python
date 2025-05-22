from pymongo import MongoClient
from bson.json_util import dumps

uri = "mongodb+srv://<usuario>:<contraseña>@<cluster>.mongodb.net/?retryWrites=true&w=majority"

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

