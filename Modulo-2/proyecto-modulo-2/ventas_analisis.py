import pandas as pd
import matplotlib.pyplot as plt
# Ventas tienda A
tienda_a = pd.DataFrame({
    "id_cliente": [1, 2, 3],
    "venta": [100, 150, 200],
    "tienda": "A"
})

# Ventas tienda B
tienda_b = pd.DataFrame({
    "id_cliente": [2, 3, 4],
    "venta": [120, 180, 250],
    "tienda": "B"
})

clientes = pd.DataFrame({
    "id_cliente": [1, 2, 3, 4],
    "nombre": ["Ana", "Luis", "Sofía", "Carlos"],
    "ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"],
    "edad": [25, 30, 28, 35]
})


ventas = pd.concat([tienda_a,tienda_b])
total = pd.merge(ventas, clientes, on="id_cliente")

# Clasificar por edad
def grupo_edad(edad):
    if edad < 30:
        return 'Joven'
    elif edad <= 50:
        return 'Adulto'
    else:
        return 'Senior'

total["grupo_edad"] = total["edad"].apply(grupo_edad)

# Agregaciones y guardado
ventas_por_ciudad = total.groupby('ciudad')['venta'].sum()
ventas_por_grupo_edad = total.groupby('grupo_edad')['venta'].sum()
ventas_por_tienda = total.groupby('tienda')['venta'].sum()

ventas_por_ciudad.to_csv('ventas_por_ciudad.csv', index=True)
ventas_por_grupo_edad.to_csv('ventas_por_edad.csv')
ventas_por_tienda.to_csv('ventas_por_tienda.csv')

# Cargar CSVs
ventas_ciudad = pd.read_csv('ventas_por_ciudad.csv', index_col=0)
ventas_edad = pd.read_csv('ventas_por_edad.csv', index_col=0)
ventas_tienda = pd.read_csv('ventas_por_tienda.csv', index_col=0)

# Mostrar totales por categoría
print("Ventas por Ciudad:")
print(ventas_ciudad, "\n")

print("Ventas por Grupo de Edad:")
print(ventas_edad, "\n")

print("Ventas por Tienda:")
print(ventas_tienda, "\n")

# Datos destacados
print(f"Ciudad con más ventas: {ventas_ciudad['venta'].idxmax()} ({ventas_ciudad['venta'].max()})")
print(f"Grupo de edad con más ventas: {ventas_edad['venta'].idxmax()} ({ventas_edad['venta'].max()})")
print(f"Tienda con más ventas: {ventas_tienda['venta'].idxmax()} ({ventas_tienda['venta'].max()})")


# Graficar resultados
ventas_por_ciudad.plot(kind='bar')
plt.xticks(rotation=0)
plt.show()

ventas_por_grupo_edad.plot(kind='bar')
plt.xticks(rotation=0)
plt.show()