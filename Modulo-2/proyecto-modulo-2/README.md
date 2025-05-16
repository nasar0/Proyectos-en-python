# Análisis de Ventas por Ciudad, Edad y Tienda

Este proyecto en Python utiliza **pandas** y **matplotlib** para analizar ventas realizadas en dos tiendas diferentes y su relación con la información de los clientes. El objetivo es practicar la manipulación de DataFrames, combinación de datos, agrupaciones, guardado y lectura de CSVs, y visualización gráfica.

---

## Descripción

* Se crean dos DataFrames simulando ventas en dos tiendas diferentes (`tienda_a` y `tienda_b`).
* Se tiene otro DataFrame con datos de clientes, incluyendo su ciudad y edad.
* Se combinan los datos de ventas y clientes usando merge.
* Se clasifica a los clientes en grupos de edad (`Joven`, `Adulto`, `Senior`).
* Se realizan agrupaciones para obtener la suma de ventas por ciudad, grupo de edad y tienda.
* Los resultados se guardan en archivos CSV.
* Se vuelven a cargar esos CSV para generar un informe de consola con totales y datos destacados.
* Se generan gráficos de barras para visualizar las ventas por ciudad y grupo de edad.

---

## Requisitos

* Python 3.x
* pandas
* matplotlib

Puedes instalar las librerías con:

```bash
pip install pandas matplotlib
```

---

## Uso

Ejecuta el script principal:

```bash
python ventas_analisis.py
```

El script mostrará en consola los totales de ventas por ciudad, grupo de edad y tienda, además de los datos destacados:

* Ciudad con más ventas
* Grupo de edad con más ventas
* Tienda con más ventas

También mostrará gráficos con las ventas agrupadas.

---

## Archivos generados

* `ventas_por_ciudad.csv`
* `ventas_por_edad.csv`
* `ventas_por_tienda.csv`

---

## Ejemplo de salida

```
Ventas por Ciudad:
         venta
ciudad        
Barcelona   270
Madrid      100
Sevilla     250
Valencia    280 

Ventas por Grupo de Edad:
         venta
grupo_edad      
Adulto       430
Joven        480

Ventas por Tienda:
        venta
tienda       
A         450
B         550 

Ciudad con más ventas: Valencia (280)
Grupo de edad con más ventas: Joven (480)
Tienda con más ventas: B (550)
```