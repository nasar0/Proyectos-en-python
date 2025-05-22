# MongoDB Python Script con PyMongo

Este script en Python permite realizar operaciones básicas sobre una colección en MongoDB utilizando la librería `pymongo`.

## Requisitos

- Python 3.x
- `pymongo`
- `dnspython` (necesario para conexiones con URI tipo `mongodb+srv`)

Puedes instalar los requerimientos con:

```bash
pip install pymongo dnspython
```

## Descripción del Script
### El script realiza las siguientes operaciones:

Conexión a MongoDB usando una URI de conexión con autenticación.

Actualización de un documento: modifica el campo email del cliente con nombre "Ana".

Eliminación de un documento: elimina al cliente con nombre "luis".

Consulta de clientes con más de un pedido: utiliza una expresión $expr con $size y $gt para filtrar documentos.

Creación de un índice en el campo email.