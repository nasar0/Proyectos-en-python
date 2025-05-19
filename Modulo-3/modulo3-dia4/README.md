# Comparación de Regresión Lineal, Ridge y Lasso

Este proyecto analiza el rendimiento de tres tipos de modelos de regresión aplicados a un dataset de automóviles:

- **Regresión Lineal**
- **Ridge Regression** (regularización L2)
- **Lasso Regression** (regularización L1)

## 📊 Dataset

Se usa el conjunto de datos `cars.csv` de la [Wild Code School](https://github.com/murpi/wilddata/blob/master/quests/cars.csv), que contiene especificaciones técnicas de automóviles antiguos (HP, cilindros, peso, etc.).

## ⚙️ Variables

- `mpg`: millas por galón (target a predecir)
- `cylinders`, `hp`, `weightlbs`: variables predictoras

## 🧠 Modelos usados

Los modelos son entrenados con `scikit-learn`:

- `LinearRegression`
- `Ridge(alpha=1.0)`
- `Lasso(alpha=0.1)`

## 📈 Evaluación

Para cada modelo se presentan:

- Error cuadrático medio (MSE)
- Coeficiente de determinación (R²)
- Gráficas de predicción vs realidad
- Histograma de residuos
- Comparación de coeficientes

## 📦 Librerías necesarias

```bash
pip install pandas numpy matplotlib scikit-learn
```
## Autor
Nasaro
GitHub: nasar0
Email: nasrallah.elkaboussi@gmail.com