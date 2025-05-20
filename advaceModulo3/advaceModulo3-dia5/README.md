¡Claro! Aquí tienes tu **README** en formato **Markdown** (`README.md`) correctamente formateado:

```markdown
# 🚗 car+++.py – Predicción de Consumo (MPG) con Ridge y Lasso

Este script realiza una regresión multivariable sobre un dataset de automóviles clásicos para predecir el consumo de combustible (millas por galón, *MPG*) usando técnicas de regularización: **Ridge** y **Lasso**.

---

## 📂 Descripción

Se utilizan modelos de regresión lineal regularizada con **búsqueda de hiperparámetros** mediante `GridSearchCV` para optimizar el parámetro `alpha`.  
El dataset se normaliza previamente con `StandardScaler` a través de **pipelines**.

---

## 📈 Dataset

Se carga desde:

```

[https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv](https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv)

````

**Variables utilizadas:**
- `mpg`: millas por galón *(objetivo)*
- `cylinders`: número de cilindros
- `hp`: caballos de fuerza
- `weightlbs`: peso en libras

---

## ⚙️ Tecnologías utilizadas

- `pandas`, `numpy` – manipulación de datos  
- `scikit-learn` – modelado, validación y escalado  
- `matplotlib` – visualización  

---

## ▶️ Cómo ejecutar

1. Asegúrate de tener **Python 3.8+** y las siguientes librerías instaladas:

```bash
pip install pandas numpy matplotlib scikit-learn
````

2. Ejecuta el script:

```bash
python car+++.py
```

---

## 🔍 Qué hace el script

* Carga y limpia los datos
* Separa variables predictoras y objetivo (`mpg`)
* Divide el dataset en entrenamiento y test
* Crea pipelines con escalado + modelo (Ridge y Lasso)
* Realiza búsqueda de hiperparámetros con `GridSearchCV`
* Evalúa los modelos con:

  * Validación cruzada (CV score)
  * MSE y R² en test
* Visualiza los resultados con gráficas de dispersión (valor real vs predicción)

---

## 📊 Ejemplo de salida

```
Mejores parámetros para Ridge: {'ridge__alpha': 0.1}
Mejores parámetros para Lasso: {'lasso__alpha': 0.01}
Score en CV Ridge: 0.70
Score en CV Lasso: 0.68

Resultados en test:
Ridge - MSE: 12.30, R2: 0.74
Lasso - MSE: 13.10, R2: 0.72
```

Se mostrarán también dos gráficos:

* **Ridge**: Predicción vs. Real
* **Lasso**: Predicción vs. Real

---

## 🧠 Aprendizaje

Este ejercicio es ideal para comprender:

* Regularización en regresión lineal
* Comparación entre Ridge y Lasso
* Importancia del escalado previo
* Selección de hiperparámetros con `GridSearchCV`
* Evaluación visual del rendimiento del modelo

## 👤 Autor
Nasaro
📧 nasrallah.elkaboussi@gmail.com
🐙 GitHub: nasar0