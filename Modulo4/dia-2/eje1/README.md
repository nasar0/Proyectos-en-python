# Conexión a MongoDB con Python

Este proyecto contiene un script básico para conectarse a una base de datos MongoDB utilizando la librería `pymongo` en Python.

---

## Requisitos

- Python 3.x
- Librería `pymongo`

Puedes instalar `pymongo` con pip:

```bash
pip install pymongo
```
## Uso
Asegúrate de tener una cuenta en MongoDB Atlas o un servidor MongoDB accesible.

Modifica la variable uri con tu cadena de conexión MongoDB.
Ejecuta el script:
```bash
python mongoDB.py
```
El script intentará conectarse a la base de datos y mostrará las bases de datos disponibles en tu servidor MongoDB.