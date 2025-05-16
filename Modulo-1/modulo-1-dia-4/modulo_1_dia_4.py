import pandas as pd
import matplotlib.pyplot as plt
# Leer archivo CSV y renombrar columnas
df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")
df.columns = ['index', 'height_in', 'weight_lb']
df = df.drop(columns=['index'])

# Añadir columna de peso en kilogramos
df["weight_kg"] = (df["weight_lb"] / 2.2046).round(2)
df["height_cm"] = (df["height_in"] * 2.54).astype(int)

df = df[df["weight_lb"].between(100, 250)]
df = df[df["height_in"].between(50, 80)]

df["imc"] = (df['weight_kg']/(df['height_in']*0.0254)**2).round(2)
#INICIO DEL EJERCICIO (PARA QUE NO TENGAS QUE IMPORTAR EL ARCHIVO)
def categoria_alt(altura):
    if altura < 175:
        return 'bajo'
    elif altura < 180:
        return 'medio'
    else:
        return 'alto'

df['categoria_peso'] = df['height_cm'].apply(categoria_alt)


# Contar cuántas personas hay en cada categoría de altura
conteo_categorias = df['categoria_peso'].value_counts().sort_index()

# Crear el gráfico
conteo_categorias.plot(kind='bar', color='skyblue')

# Personalizar
plt.title('Cantidad de personas por categoría de altura')
plt.xlabel('Categoría de altura')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)

# Guardar gráfico (opcional)
plt.savefig('personas_por_altura.png')

# Mostrarlo
plt.show()