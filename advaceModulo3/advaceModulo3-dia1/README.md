# 📈 Predicción de Peso en función de la Altura (Regresión Lineal)

Este proyecto utiliza un modelo de **regresión lineal simple** para predecir el peso (en kilogramos) de una persona a partir de su altura (en centímetros). Se basa en un dataset real de altura y peso, y aplica técnicas básicas de Machine Learning con `scikit-learn`.

---

## 🧪 Tecnologías usadas

- Python 3
- Pandas
- Matplotlib
- scikit-learn

---

## 📊 Descripción del proyecto

1. **Carga de datos:**  
   Se utiliza un dataset disponible públicamente de altura/peso en pulgadas y libras.

2. **Preprocesamiento:**  
   - Se renombran las columnas.  
   - Se convierten las unidades a centímetros y kilogramos.  
   - Se eliminan columnas innecesarias.

3. **Entrenamiento del modelo:**  
   - Se entrena un modelo de regresión lineal simple (`LinearRegression`) para predecir el peso en kg a partir de la altura en cm.

4. **Predicciones:**  
   - El modelo predice el peso estimado para alturas de ejemplo (170, 180, 190 cm).
   - Los resultados se imprimen en pantalla.

---

## 📌 Requisitos

Instala las librerías necesarias con:

```bash
pip install pandas matplotlib scikit-learn
```

## ▶️ Ejecución
Simplemente corre el script:
```bash
python prediccion_peso.py
```
## 📤 Ejemplo de salida
Altura: 176 cm -> Peso estimado: 72.41 kg  
Altura: 180 cm -> Peso estimado: 76.41 kg  
Altura: 190 cm -> Peso estimado: 86.40 kg  

## 📁 Fuente de datos
https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv

 
