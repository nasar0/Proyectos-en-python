# Merge de DataFrames con pandas 🐼

Este script de Python muestra cómo combinar dos `DataFrames` usando la función `merge()` de la biblioteca `pandas`. Se utilizan distintos tipos de unión: `inner`, `outer`, `left` y `right`.

## 📄 Descripción

- Se crean dos DataFrames:
  - `df_a`: contiene un ID y un nombre.
  - `df_b`: contiene un ID y una edad.
- Se demuestra cómo combinar ambos usando diferentes tipos de `merge`.

## 🔧 Tipos de uniones demostradas

| Tipo de unión | Descripción |
|---------------|-------------|
| `inner`       | Solo los IDs que existen en ambos DataFrames |
| `outer`       | Todos los IDs, rellenando con `NaN` si no hay coincidencia |
| `left`        | Todos los datos de `df_a`, más los coincidentes de `df_b` |
| `right`       | Todos los datos de `df_b`, más los coincidentes de `df_a` |

## ▶️ Ejecución

```bash
python merge_ejemplo.py