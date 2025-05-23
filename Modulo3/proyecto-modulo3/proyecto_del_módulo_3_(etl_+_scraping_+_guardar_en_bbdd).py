import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
import sqlite3

def guardar():
    try:
        with sqlite3.connect("titularesELpais.db") as conn:
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS titulares ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "fecha_scrap TEXT, "
                "titular TEXT UNIQUE)"
            )

            url = "https://elpais.com/"
            respuesta = requests.get(url)
            soup = BeautifulSoup(respuesta.text, "html.parser")

            titulares = soup.find_all("h2")
            titulares_limpios = [t.get_text(strip=True) for t in titulares if t.get_text(strip=True)]

            for titular in titulares_limpios:
                try:
                    cur.execute(
                        "INSERT INTO titulares (fecha_scrap, titular) VALUES (CURRENT_TIMESTAMP, ?)",
                        (titular,)
                    )
                    print(f"✅ Titular guardado: {titular}")
                except sqlite3.IntegrityError:
                    print(f"⏩ Titular duplicado (ignorado): {titular}")
    except Exception as e:
        print(f"Error en guardar(): {e}")


def titulosElpais():
    try:
        guardar()
    except Exception as e:
        print(f"Error en titulosElpais(): {e}")


schedule.every(60).seconds.do(titulosElpais)

n = input("Pulsa 0 para bucle automático o 1 para guardar CSV: ")

if n == "0":
    print("⏳ Iniciando scraping automático... (Ctrl+C para detener)")
    while True:
        schedule.run_pending()
        time.sleep(1)
elif n == "1":
    with sqlite3.connect("titularesELpais.db") as conn:
        df = pd.read_sql_query("SELECT * FROM titulares", conn)

    df.to_csv("titulares_elpais.csv", index=False, encoding="utf-8")
    print("Titulares exportados a 'titulares_elpais.csv'")
else:
    print("Opción no válida.")
