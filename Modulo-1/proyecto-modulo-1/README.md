# Perfil Promedio de Salud por Grupo de Edad

## Descripción

Este proyecto analiza un conjunto de datos de altura y peso para calcular el Índice de Masa Corporal (IMC) y agrupar a las personas en categorías de edad: **Joven**, **Adulto** y **Mayor**. Se generan visualizaciones que muestran los promedios de altura, peso e IMC para cada grupo de edad.

El objetivo es practicar la manipulación y análisis de datos usando Python y pandas, así como la creación de gráficos con matplotlib para presentar resultados de manera clara.

---

## Estructura del proyecto

- `perfil_salud_completo.csv` - Dataset final con datos combinados y columnas calculadas  
- `promedio_altura_edad.png` - Gráfico de barras del promedio de altura por grupo de edad  
- `promedio_peso_edad.png` - Gráfico de barras del promedio de peso por grupo de edad  
- `promedio_imc_edad.png` - Gráfico de barras del promedio de IMC por grupo de edad  
- `proyecto_perfil_salud.py` - Script principal con el código para procesar datos y generar gráficos (opcional)  
- `README.md` - Este archivo

---

## Tecnologías y librerías usadas

- Python 3.x  
- pandas  
- matplotlib  

Para instalar las librerías, ejecuta:

```bash
pip install pandas matplotlib
Cómo ejecutar el proyecto
Clona o descarga este repositorio

Instala las dependencias (si no lo has hecho)

Ejecuta el script proyecto_perfil_salud.py o ejecuta el código en un Jupyter Notebook

Los gráficos se guardarán en el directorio como archivos PNG

Detalles del análisis
Se importa un dataset base con alturas y pesos (en pulgadas y libras).

Se calcula el peso en kilogramos y la altura en centímetros.

Se simula un segundo dataset con edades para combinarlo con el primero.

Se calcula el IMC para cada registro.

Se crea una columna de categoría de edad (Joven, Adulto, Mayor).

Se calcula el promedio de altura, peso e IMC por categoría de edad.

Se visualizan estos promedios en gráficos de barras.

Autor
Nasaro