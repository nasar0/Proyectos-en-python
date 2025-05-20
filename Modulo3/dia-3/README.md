# Scraper de Titulares de El País

Este proyecto es un scraper simple en Python que extrae los titulares de noticias desde la página principal de [El País](https://elpais.com/) y los imprime en consola. Además, ejecuta esta tarea de manera automática cada 60 segundos usando la librería `schedule`.

---

## Tecnologías usadas

- Python 3.x
- Requests
- BeautifulSoup (bs4)
- Pandas (para manejo de datos)
- Schedule (para ejecución periódica)

---

## Instalación

Primero, clona este repositorio o copia el código en tu máquina local.

Luego, instala las dependencias con pip:

```bash
pip install requests beautifulsoup4 pandas schedule
```

## Uso
Ejecuta el script para iniciar el scraper automático:

```bash
python webscrapingpais.py
```

El script imprimirá los titulares extraídos cada 60 segundos.

## Funcionamiento
Hace una petición HTTP a la página principal de El País.

Analiza el HTML recibido para extraer todos los textos dentro de etiquetas <h2>.

Limpia los textos para eliminar espacios y etiquetas vacías.

Imprime la lista de titulares en consola.

Repite esta tarea cada 60 segundos automáticamente.

## Autor
Nasaro