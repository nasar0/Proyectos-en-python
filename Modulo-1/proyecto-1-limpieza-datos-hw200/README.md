# 📊 Limpieza y transformación de datos - Dataset `hw_200.csv`

Este mini proyecto es parte de mi formación en Data Engineering. El objetivo fue cargar, limpiar, transformar y exportar un dataset simple utilizando Python y pandas.

---

## 📁 Dataset original

El archivo proviene de una fuente pública:

- URL: [https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv](https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv)
- Columnas originales: índice, altura en pulgadas, peso en libras

---

## ⚙️ Procesamiento realizado

1. Carga del archivo `.csv` con pandas
2. Renombrado de columnas para mayor claridad
3. Eliminación de la columna innecesaria `index`
4. Conversión del peso de libras (`lb`) a kilogramos (`kg`)
5. Filtros aplicados:
   - Altura entre 50 y 80 pulgadas
   - Peso entre 100 y 250 libras
6. Cálculo del IMC (Índice de Masa Corporal) usando:

   \[
   \text{IMC} = \frac{\text{peso (kg)}}{(\text{altura (m)})^2}
   \]

7. Redondeo de valores
8. Exportación del DataFrame final a un nuevo archivo `datos_finales.csv`

---

## 📦 Archivos generados

- `datos_finales.csv`: archivo limpio y transformado
- `limpieza_hw_200.py`: código completo paso a paso

---

## 🛠️ Tecnologías usadas

- Python 3
- Pandas
- Google Colab

---

## ✍️ Autor

**Nasaro**  
_Proyecto 1 – Data Engineering Bootcamp_

---

