import pandas as pd
import matplotlib.pyplot as plt
# Leer archivo CSV y renombrar columnas
df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")
df.columns = ['index', 'height_in', 'weight_lb']
df = df.drop(columns=['index'])

# Añadir columna de peso en kilogramos
df["weight_kg"] = (df["weight_lb"] / 2.2046).round(2)

df = df[df["weight_lb"].between(100, 250)]
df = df[df["height_in"].between(50, 80)]

df["imc"] = (df['weight_kg']/(df['height_in']*0.0254)**2).round(2)
#INICIO DEL EJERCICIO (PARA QUE NO TENGAS QUE IMPORTAR EL ARCHIVO)
# Agrupar por categoría IMC
bins = [0, 18.5, 25, 30, 100]
labels = ['Bajo peso', 'Normal', 'Sobrepeso', 'Obesidad']
df['categoria_imc'] = pd.cut(df['imc'], bins=bins, labels=labels)

promedio_lb = (df.groupby("categoria_imc")["weight_lb"].mean()).round(2)

print(promedio_lb)
promedio_lb.plot(kind='bar', color='orange')
plt.title('Promedio de peso por categoría IMC')
plt.xlabel('Categoría IMC')
plt.ylabel('Peso promedio (libras)')
plt.savefig("promedio_peso_imc.png")
plt.show()