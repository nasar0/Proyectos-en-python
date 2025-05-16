import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Dataset de altura/peso
df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")
df.columns = ['index', 'height_in', 'weight_lb']
df = df.drop(columns=['index'])

# Convertimos a sistema métrico
df["height_cm"] = (df["height_in"] * 2.54).round(1)
df["weight_kg"] = (df["weight_lb"] / 2.2046).round(1)

# Variables
X = df[["height_cm"]]  # variable independiente
y = df["weight_kg"]    # variable a predecir



modelo = LinearRegression()
modelo.fit(X, y)
alturas = [[170], [180], [190]]
predicciones = modelo.predict(alturas)

# Mostrar resultados
for altura, peso in zip([176, 180, 190], predicciones):
    print(f"Altura: {altura} cm -> Peso estimado: {peso:.2f} kg")