import pandas as pd

# Datos de enero
df_enero = pd.DataFrame({
    "id": [1, 2],
    "nombre": ["Ana", "Luis"],
    "ventas": [100, 200]
})
df_enero["mes"] = "enero"

# Datos de febrero
df_febrero = pd.DataFrame({
    "id": [3, 4],
    "nombre": ["Sofía", "Carlos"],
    "ventas": [150, 180]
})
df_febrero["mes"] = "febrero"

# Datos de marzo
df_marzo = pd.DataFrame({
    "id": [3, 4],
    "nombre": ["Sofía", "Carlos"],
    "ventas": [100, 110]
})
df_marzo["mes"] = "marzo"

# Unimos todo en uno solo
df_total = pd.concat([df_enero, df_febrero, df_marzo])

print(df_total)