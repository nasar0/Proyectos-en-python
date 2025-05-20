import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de ejemplo con una tabla real (Wikipedia - autos)
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

# Realizar la petición a la página
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Buscar la primera tabla de la página
tabla = soup.find("table", {"class": "wikitable"})

# Convertir la tabla HTML en un DataFrame de pandas
df = pd.read_html(str(tabla))[0]

df = df.dropna()
df = df.fillna("Null")

df = df.rename( columns={'% of world' : "world %"})
# Mostrar los primeros registros
print("Tabla extraída:")
print(df.head())

# Guardar como CSV
df.to_csv("poblacion_mundial.csv", index=False)
print("CSV guardado.")

# Guardar como Excel
df.to_excel("poblacion_mundial.xlsx", index=False)
print("Excel guardado.")

# Guardar como JSON
df.to_json("poblacion_mundial.json", orient="records", indent=2)
print("JSON guardado.")