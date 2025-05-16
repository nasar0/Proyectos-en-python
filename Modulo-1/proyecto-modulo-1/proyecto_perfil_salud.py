import pandas as pd
import matplotlib.pyplot as plt
# Dataset base (como ya venías trabajando)
df1 = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")
df1.columns = ['index', 'height_in', 'weight_lb']
df1 = df1.drop(columns=['index'])
df1["weight_kg"] = (df1["weight_lb"] / 2.2046).round(2)
df1["height_cm"] = (df1["height_in"] * 2.54).astype(int)

# Simulamos un segundo archivo con edades
# (en la vida real podrías leer esto desde un CSV o Excel)
df2 = pd.DataFrame({
    'id': range(len(df1)),
    'edad': pd.Series([20, 25, 30, 35, 40]*40)[:len(df1)]
})

# Añadimos índice para unir
df1 = df1.reset_index().rename(columns={'index': 'id'})

# Unimos ambos DataFrames por 'id'
df = pd.merge(df1, df2, on='id')

def catgoria_edad(edad):
    if edad >= 18 and edad <= 29:
        return "Joven"
    elif edad >= 30 and edad <= 39:
        return "Adulto"
    else:
        return "Mayor"

df["imc"] = (df['weight_kg']/(df['height_in']*0.0254)**2).round(2)
df["categoria_edad"] = df["edad"].apply(catgoria_edad)

altura = (df.groupby("categoria_edad")["height_cm"].mean()).round()
peso = (df.groupby("categoria_edad")["weight_kg"].mean()).round(2)
imc = (df.groupby("categoria_edad")["imc"].mean()).round(2)


altura.plot(kind='bar', color='green')
plt.title('Promedio de altura por categoría edad')
plt.xlabel('Categoría edad')
plt.ylabel('altura promedio (cm)')
plt.savefig("promedio_altura_edad.png")
plt.xticks(rotation=0)
plt.show()

peso.plot(kind='bar', color='blue')
plt.title('Promedio de peso por categoría edad')
plt.xlabel('Categoría edad')
plt.ylabel('peso promedio (kg)')
plt.savefig("promedio_peso_edad.png")
plt.xticks(rotation=0)
plt.show()

imc.plot(kind='bar', color='orange')
plt.title('Promedio de peso por categoría edad')
plt.xlabel('Categoría edad')
plt.ylabel('imc promedio')
plt.savefig("promedio_imc_edad.png")
plt.xticks(rotation=0)
plt.show()