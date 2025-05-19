# Predicción del Precio de Bicicletas con Regresión Lineal Múltiple

Este proyecto implementa un modelo de regresión lineal múltiple para predecir el precio de bicicletas basado en características como el tamaño de la rueda, el peso y si la marca es premium o no.

---

## Descripción

Se genera un dataset simulado con las siguientes características:
- **tamaño_rueda**: tamaño de la rueda en pulgadas (valores posibles: 26, 27.5, 29).
- **peso**: peso de la bicicleta en kilogramos (simulado con una distribución normal).
- **marca_premium**: indicador binario (0 = no premium, 1 = premium).
- **precio**: variable objetivo que depende linealmente de las características anteriores, con algo de ruido añadido.

El modelo usa regresión lineal múltiple para aprender la relación entre las variables y predecir el precio.

---

## Tecnologías utilizadas

- Python 3.x  
- pandas  
- numpy  
- scikit-learn  
- matplotlib (opcional para gráficos)

---

## Cómo ejecutar

1. Clona el repositorio:
   ```bash
      git clone https://github.com/nasar0/Proyectos-en-python
      cd Proyectos-en-python/Modulo-3/modulo3-dia2
   ```
Instala las dependencias:

   ```bash
   pip install pandas numpy scikit-learn matplotlib
   ```
Ejecuta el script principal:

```bash
python bicicleta_regresion.py
```
## Resultados
El modelo reporta métricas de evaluación como:

Mean Squared Error (MSE)

Coeficiente de determinación (R²)

Estas métricas indican qué tan bien el modelo predice los precios en el conjunto de prueba.

## Autor
Nasaro
Contacto: nasrallah.elkaboussi@gmail.com
GitHub: nasar0