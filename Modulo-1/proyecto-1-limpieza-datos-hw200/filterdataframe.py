import pandas as pd

# Leer archivo CSV y renombrar columnas
df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")
df.columns = ['index', 'height_in', 'weight_lb']
df = df.drop(columns=['index'])

# Añadir columna de peso en kilogramos
df["weight_kg"] = (df["weight_lb"] / 2.2046).round(2)

df = df[df["weight_lb"].between(100, 250)]
df = df[df["height_in"].between(50, 80)]

df["imc"] = df['weight_kg']/(df['height_in']*0.0254)**2
print(df)
