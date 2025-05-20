# 🚗 Predicción del Consumo de Coches con Regresión Lineal

Este proyecto utiliza regresión lineal múltiple para predecir el consumo de combustible (`mpg`) de automóviles, basado en características técnicas como el número de cilindros, caballos de fuerza (`hp`) y peso del vehículo (`weightlbs`).

---

## 📁 Dataset

El dataset utilizado proviene de [Wild Data](https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv). Contiene datos técnicos de coches de distintas regiones.

### Variables utilizadas:
- `mpg`: millas por galón (target a predecir)
- `cylinders`: número de cilindros
- `hp`: caballos de fuerza
- `weightlbs`: peso del coche en libras

---

## 🧠 Objetivo

Entrenar un modelo de regresión lineal múltiple para predecir el consumo (`mpg`) de un coche dadas sus características técnicas, y evaluar su desempeño.

---

## 🛠️ Tecnologías y Librerías

- Python 3
- Pandas
- Scikit-learn (`LinearRegression`, `train_test_split`, métricas)
- Matplotlib

---

## 📊 Proceso

1. **Carga y limpieza de datos**
2. **Selección de variables predictoras**
3. **División en entrenamiento y test**
4. **Entrenamiento del modelo**
5. **Evaluación con métricas**: MSE y R²
6. **Visualización**:
   - Dispersión de precios reales vs predichos
   - Histograma de errores (residuos)
   - Gráfico de importancia de variables

---

## 📈 Resultados esperados

- MSE: error cuadrático medio del modelo
- R²: porcentaje de varianza explicada por el modelo
- Visualizaciones claras para entender el rendimiento del modelo

---

## ✍️ Autor

**Nasaro**  
📧 nasrallah.elkaboussi@gmail.com  
🔗 GitHub: [nasar0](https://github.com/nasar0)

---