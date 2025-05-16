````markdown
# Análisis de Peso Promedio por Categoría de IMC

Este proyecto realiza un análisis sencillo de datos de altura y peso para calcular y visualizar el promedio de peso (en libras) según la categoría del Índice de Masa Corporal (IMC).

---

## Descripción

El script realiza las siguientes tareas:

1. **Carga de datos**: Lee un archivo CSV público con datos de altura y peso.
2. **Limpieza de datos**: Renombra columnas y elimina columnas innecesarias.
3. **Filtrado**: Mantiene solo las filas con peso entre 100 y 250 libras, y altura entre 50 y 80 pulgadas.
4. **Cálculo del IMC**: Calcula el Índice de Masa Corporal para cada individuo.
5. **Clasificación**: Asigna a cada persona una categoría de IMC:
   - Bajo peso (IMC < 18.5)
   - Normal (18.5 ≤ IMC < 25)
   - Sobrepeso (25 ≤ IMC < 30)
   - Obesidad (IMC ≥ 30)
6. **Agrupación y resumen**: Calcula el peso promedio para cada categoría de IMC.
7. **Visualización**: Genera y guarda un gráfico de barras mostrando el peso promedio por categoría.

---

## Cómo ejecutar

1. Clona o descarga este repositorio.
2. Asegúrate de tener Python 3.7 o superior instalado.
3. Instala las librerías necesarias:

```bash
pip install pandas matplotlib
````

4. Ejecuta el script:

```bash
python groupby.py
```

5. El resultado se imprimirá en consola y se generará un archivo `promedio_peso_imc.png` con el gráfico.

---

## Datos usados

Datos tomados del archivo público:
[https://people.sc.fsu.edu/\~jburkardt/data/csv/hw\_200.csv](https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv)

---

## Autor

Tu Nombre - \[[nasrallah.elkaboussi@ejemplo.com](mailto:nasrallah.elkaboussi@ejemplo.com)]

---