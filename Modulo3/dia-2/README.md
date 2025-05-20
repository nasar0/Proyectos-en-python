# Extracción y Guardado de Tabla de Wikipedia

Este script en Python extrae una tabla de datos de una página web de Wikipedia, la procesa y la guarda en varios formatos (CSV, Excel y JSON).

## Descripción

El código realiza lo siguiente:

- Realiza una petición HTTP a la página de Wikipedia con la lista de países y dependencias por población.
- Extrae la primera tabla con clase `wikitable`.
- Convierte esa tabla HTML en un DataFrame de pandas.
- Limpia y ajusta algunos datos (elimina filas con valores `NaN` y renombra una columna).
- Muestra las primeras filas de la tabla en consola.
- Guarda la tabla en tres formatos diferentes: CSV, Excel y JSON.

## Requisitos

- Python 3.x
- Librerías:
  - `requests`
  - `beautifulsoup4`
  - `pandas`

Puedes instalarlas con:

```bash
pip install requests beautifulsoup4 pandas
```
## Uso
Ejecuta el script directamente:
```bash
python tablas_wiki.py
```
El script generará los archivos:

poblacion_mundial.csv

poblacion_mundial.xlsx

poblacion_mundial.json

en el directorio donde se ejecuta el script.

## Autor
Nasaro