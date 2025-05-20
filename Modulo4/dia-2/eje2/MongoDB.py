from pymongo import MongoClient

uri = "mongodb+srv://user:pass@cluster0.kiptamo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(uri)
    print(client.list_database_names())  # Muestra las bases de datos disponibles
    print("¡Conexión exitosa!")

    db = client["mongoDB"]
    coleccion = db["clientes"]

    clientes = [
        {
            "nombre": "Ana",
            "email": "ana@email.com",
            "pedidos": [
                {"pedido_id": 101, "fecha": "2025-05-20"},
                {"pedido_id": 102, "fecha": "2025-05-22"}
            ]
        },
        {
            "nombre": "Luis",
            "email": "luis@email.com",
            "pedidos": [
                {"pedido_id": 103, "fecha": "2025-05-21"}
            ]
        }
    ]

    try:
        coleccion.insert_many(clientes)
        print("Documentos insertados.")
    except Exception as e:
        print("Error al insertar documentos:", e)

    print("\nTodos los documentos en la colección:")
    for doc in coleccion.find():
        print(doc)

    resultado = coleccion.find({"pedidos.pedido_id": 101})
    print("\nClientes con pedido 101:")
    for doc in resultado:
        print(doc)

except Exception as e:
    print("Error al conectar a MongoDB:", e)
