import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time

def titulosElpais():
    url ="https://elpais.com/"

    respuesta = requests.get(url)

    soup = BeautifulSoup(respuesta.text,"html.parser")

    titulares = soup.find_all("h2")

    # Limpiar y guardar en DataFrame
    titulares_limpios = [titular.get_text(strip=True) for titular in titulares if titular.get_text(strip=True)]

    print(titulares_limpios)

schedule.every(60).seconds.do(titulosElpais)

print("⏳ Iniciando scraping automático... (Ctrl+C para detener)")
while True:
    schedule.run_pending()
    time.sleep(1)