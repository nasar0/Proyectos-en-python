# Scraper de Titulares de El País

Este proyecto es un scraper que extrae titulares de noticias del sitio web [El País](https://elpais.com/), los guarda en una base de datos SQLite y permite exportarlos a un archivo CSV.

---

## Funcionalidades

- Extrae titulares (`<h2>`) de la página principal de El País.
- Guarda los titulares en una base de datos SQLite (`titularesELpais.db`) con marca de tiempo.
- Evita duplicados al insertar titulares.
- Permite ejecutar un bucle automático que realiza scraping cada 60 segundos.
- Exporta los titulares guardados a un archivo CSV (`titulares_elpais.csv`).

---

## Requisitos

- Python 3.x
- Librerías:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `schedule`

Puedes instalar las dependencias con:

```bash
pip install requests beautifulsoup4 pandas schedule
```

## Uso
Al ejecutar el script, se te preguntará:
```bash
Pulsa 0 para bucle automático o 1 para guardar CSV:
```
0: Inicia el scraping automático cada 60 segundos.
Detén el proceso con Ctrl+C.
1: Exporta los titulares guardados en la base de datos a un archivo CSV (titulares_elpais.csv).

## Estructura de la base de datos
La tabla titulares contiene:

Campo	Tipo	Descripción
id	INTEGER	Clave primaria autoincrementable
fecha_scrap	TEXT	Fecha y hora en que se guardó el titular
titular	TEXT	Texto del titular (único)

Ejemplo de ejecución
```bash
python proyecto_del_módulo_3_(etl_+_scraping_+_guardar_en_bbdd).py
```
Luego, ingresa la opción deseada (0 o 1).

## Notas
El script maneja errores básicos, como titulares duplicados o problemas al guardar datos.

Puedes modificar el intervalo de scraping cambiando schedule.every(60).seconds en el código.