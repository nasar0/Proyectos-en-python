# Ejemplo de concatenación de DataFrames en Pandas

Este proyecto muestra un ejemplo básico de cómo crear múltiples DataFrames en pandas y concatenarlos en uno solo.

## Descripción

Se crean tres DataFrames simulando ventas mensuales (enero, febrero y marzo). Cada DataFrame tiene columnas de `id`, `nombre` y `ventas`, y se añade una columna adicional `mes` para identificar el mes correspondiente. Luego, todos los DataFrames se concatenan en uno solo usando `pd.concat()`.

## Código principal

```python
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
