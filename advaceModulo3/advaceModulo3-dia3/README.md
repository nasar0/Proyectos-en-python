# Análisis de Regresión Lineal para Predicción de Consumo de Combustible (MPG)

Este proyecto utiliza un conjunto de datos de autos para construir un modelo de regresión lineal que predice el consumo de combustible (millas por galón, MPG) basado en características del vehículo.

---

## Descripción

Se utiliza el dataset disponible en:  
[https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv](https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv)

Características empleadas:  
- Número de cilindros (`cylinders`)  
- Caballos de fuerza (`hp`)  
- Peso del vehículo en libras (`weightlbs`)  
- Ratio peso/caballos de fuerza normalizado (`peso_hp_ratio`)  
- Logaritmo de caballos de fuerza (`potencia_log`)

El objetivo es predecir `mpg` (millas por galón).

---

## Pasos realizados

1. Carga y limpieza de datos: selección de columnas relevantes y eliminación de filas con valores faltantes.  
2. Creación de variables derivadas:  
   - `peso_hp_ratio` (peso dividido por caballos de fuerza)  
   - `potencia_log` (logaritmo natural de los caballos de fuerza)  
3. Normalización de `peso_hp_ratio` para mejorar la escala y rendimiento del modelo.  
4. División de los datos en conjunto de entrenamiento y prueba (80/20).  
5. Entrenamiento de un modelo de regresión lineal.  
6. Evaluación del modelo con métricas:  
   - Mean Squared Error (MSE)  
   - Coeficiente de determinación (R²)  
7. Visualización:  
   - Scatter plot de valores reales vs. predichos  
   - Histograma de errores (residuos)  
   - Gráfico de barras horizontales con la importancia (coeficientes) de cada variable.

---

## Resultados

- El scatter plot permite visualizar qué tan bien el modelo ajusta las predicciones a los datos reales.  
- El histograma muestra la distribución de los errores de predicción.  
- El gráfico de coeficientes indica el peso que cada variable tiene en la predicción del consumo.

---

## Requisitos

- Python 3.x  
- Librerías: `pandas`, `numpy`, `scikit-learn`, `matplotlib`

---

## Cómo ejecutar

1. Clonar el repositorio o copiar el script.  
2. Instalar las dependencias (si no están instaladas):  
```bash
   pip install pandas numpy scikit-learn matplotlib
```
Ejecutar el script en un entorno Python.

## Autor
Nasaro
GitHub: nasar0
Email: nasrallah.elkaboussi@gmail.com