# Conexión a MongoDB e Inserción de Documentos con Python

Este proyecto demuestra cómo conectarse a una base de datos MongoDB usando `pymongo`, insertar múltiples documentos en una colección y realizar consultas específicas.

---

## 🛠 Requisitos

- Python 3.x
- `pymongo`

Instala la librería necesaria con:

```bash
pip install pymongo
```
## 📂 Estructura del Script
El script realiza las siguientes acciones:

Se conecta a una instancia de MongoDB utilizando una URI.

Accede a la base de datos mongoDB y a la colección clientes.

Inserta múltiples documentos que representan clientes y sus pedidos.

Muestra todos los documentos insertados.

Realiza una consulta para encontrar clientes con un pedido específico (pedido_id: 101).

## ▶️ Uso
Asegúrate de tener acceso a una instancia de MongoDB Atlas o local.

Reemplaza la URI con tus credenciales reales (no compartas tus credenciales públicamente).

Ejecuta el script con:

```bash
python script.py
```

## 🔐 Seguridad
No publiques tu URI de MongoDB con usuario y contraseña reales.
Usa variables de entorno para manejar credenciales sensibles.

## 📬 Contacto
¿Tienes alguna duda o sugerencia? Abre un issue o un pull request.