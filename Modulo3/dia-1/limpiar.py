import pandas as pd

# 1. Leer archivo CSV
df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

# 2. Mostrar las primeras filas para ver qué tiene
print(df.head())

# 3. Limpiar datos: quitar filas con valores faltantes
df_clean = df.dropna()

# 4. Crear una nueva columna: peso_hp_ratio
df_clean['peso_hp_ratio'] = df_clean['weightlbs'] / df_clean['hp']

# 5. Guardar a CSV localmente
df_clean.to_csv('cars_clean.csv', index=False)

print("Archivo guardado como 'cars_clean.csv'")
