# Análisis de Ventas - TP2 - Organización Empresarial - UTN

## Descripción del Proyecto
Este proyecto forma parte del Trabajo Práctico de la cátedra de Organización Empresarial
de la Tecnicatura Universitaria en Programación (UTN - Modalidad a Distancia).

El objetivo es analizar un conjunto de datos de ventas de una tienda de ropa para generar
indicadores básicos que permitan interpretar el desempeño comercial, aplicando control de
versiones con Git y GitHub, gestión de tareas con Jira y desarrollo colaborativo.

## Escenario
Escenario B - Análisis de Ventas de una Pequeña Empresa

## Integrantes
- Hugo: Líder y Organizador
- Paco: Desarrollador Técnico
- Luis:Revisor y QA
*(Los integrantes son ficticios ya que el tp lo hice sola, utilicé diferentes mails para cada usuario.)

## Dataset
Dataset de ventas simuladas de una tienda de ropa con registros de:
- Fecha de venta
- Producto (Campera, Remera, Pantalon, Vestido, Zapatillas)
- Cantidad vendida
- Monto de venta
El dataset está organizado por n°de fila, por si se quiere modificar el script para contar cuántos productos diferentes está manejando la tienda. En este caso no lo utilize.

Período: Enero a Diciembre 2024.

## Instrucciones para ejecutar el script
1. Clonar el repositorio
2. Abrir Google Colab
3. Posicionarse en la carpeta scripts:
   import os
   os.chdir('/content/TPI_OE_TUP_Analisis_Ventas_/scripts')
4. Ejecutar el script:
   !python analisis_ventas.py
5. Los resultados se guardan en /resultados/resultados_ventas.txt

## Estructura del Repositorio
- /datos — Dataset de ventas en formato CSV
- /scripts — Script de análisis en Python
- /resultados — Resultados generados por el análisis
- README.md — Documentación del proyecto
- .gitignore — Archivos excluidos del repositorio
