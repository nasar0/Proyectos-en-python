# Limpieza de Datos con Pandas

Este proyecto contiene un script básico para la limpieza de datos en un DataFrame de pandas. Se enfoca en corregir datos sucios o inconsistentes en columnas tanto numéricas como no numéricas.

## Descripción

El código carga un conjunto de datos con valores faltantes, cadenas con espacios y texto en formatos inconsistentes. Luego, mediante la función `clean_data`, realiza los siguientes pasos:

- Para columnas no numéricas:
  - Reemplaza valores `NaN` por `"Desconocido"`.
  - Elimina espacios en blanco al inicio y final.
  - Capitaliza la primera letra de cada valor.
  
- Para columnas numéricas (almacenadas como objetos):
  - Intenta convertirlas a formato numérico.
  - Si existen valores numéricos válidos, reemplaza los valores no convertibles por la media redondeada de la columna.

## Requisitos

- Python 3.x
- pandas
- numpy

Puedes instalar las librerías necesarias con:

```bash
pip install pandas numpy
```
## Autor
Nasaro

