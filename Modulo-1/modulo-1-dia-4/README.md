Aquí tienes un `README.md` bien estructurado para tu proyecto de análisis de datos con el dataset `hw_200.csv`:

---

# 📊 Análisis de Datos Antropométricos - Dataset `hw_200.csv`

Este proyecto realiza un análisis básico de un dataset que contiene mediciones de altura y peso, incluyendo transformaciones de unidades, cálculo del IMC, categorización y visualización de datos.

## 📋 Descripción

El script carga datos antropométricos en unidades imperiales (pulgadas y libras), los convierte al sistema métrico, calcula el Índice de Masa Corporal (IMC), categoriza las alturas y genera una visualización de la distribución por categorías.

## 🛠️ Tecnologías utilizadas

- Python 3
- Pandas (para manipulación de datos)
- Matplotlib (para visualización)
- Jupyter Notebook/Google Colab (entorno de ejecución recomendado)

## 📁 Dataset

**Fuente:** [Universidad Estatal de Florida](https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv)  
**Contenido original:**
- Índice (eliminado en el procesamiento)
- Altura en pulgadas (`height_in`)
- Peso en libras (`weight_lb`)

## 🔄 Transformaciones realizadas

1. **Limpieza inicial:**
   - Renombrado de columnas
   - Eliminación de columna de índice

2. **Conversión de unidades:**
   - Peso: libras → kilogramos (`weight_kg`)
   - Altura: pulgadas → centímetros (`height_cm`)

3. **Filtrado de datos:**
   - Altura conservada entre 50-80 pulgadas (127-203 cm)
   - Peso conservado entre 100-250 libras (45-113 kg)

4. **Cálculo de métricas:**
   - Índice de Masa Corporal (IMC) usando la fórmula:
     \[
     \text{IMC} = \frac{\text{peso (kg)}}{(\text{altura (m)})^2}
     \]

5. **Categorización:**
   - Altura en tres categorías:
     - Bajo: < 175 cm
     - Medio: 175-180 cm
     - Alto: > 180 cm

6. **Visualización:**
   - Gráfico de barras mostrando la distribución por categoría de altura

## 📊 Resultados

El análisis genera:
1. Un DataFrame con las columnas transformadas
2. Un gráfico de barras (`personas_por_altura.png`) que muestra:
   - Cantidad de personas en cada categoría de altura
   - Título y ejes descriptivos

## 🚀 Cómo ejecutar

1. Clonar repositorio o descargar script
2. Instalar dependencias:
   ```bash
   pip install pandas matplotlib
   ```
3. Ejecutar el script Python:
   ```bash
   python analisis_antropometrico.py
   ```

## 📝 Notas adicionales

- Todos los cálculos se redondean a 2 decimales excepto la altura en cm que se trunca a entero
- Los filtros aplicados eliminan valores extremos no biológicamente plausibles para adultos

## 👨‍💻 Autor

**Nasaro**  
_Proyecto 1 – Data Engineering Bootcamp_

---

