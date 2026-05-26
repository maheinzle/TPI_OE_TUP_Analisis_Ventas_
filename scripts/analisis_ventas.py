
# SCRUM-2: Script de Análisis de Ventas
# Desarrollador: Paco
# Descripción: Script para analizar datos de ventas.

import csv

                   # DEFINICIÓN DE FUNCIONES

#CARGA DE DATOS: Carga el archivo CSV y retorna una lista de diccionarios
def cargar_datos(ruta):
    datos = []                  
    #with garantiza que el archivo se cierre automáticamente cuando termine de usarse, aunque ocurra un error.
    #as le da un nombre al archivo abierto para poder usarlo dentro del bloque. En este caso el nombre es archivo.
    with open(ruta, newline='', encoding='utf-8') as archivo: #newline=' ' evita problemas con saltos de línea y encoding='utf-8'permite leer tildes y caracteres especiales
        lector = csv.DictReader(archivo) #DicReader  es una clase de la librería csv que lee un archivo CSV y convierte cada fila en un diccionario.
        for fila in lector:
            datos.append(fila)
    return datos

#TOTAL DE VENTAS: Calcula el total de ventas sumando todos los montos
def calcular_total_ventas(datos):
    total = 0
    for fila in datos:
        total += float(fila['monto'])
    return total

#PRODUCTO MAS VENDIDO: Retorna el producto con mayor cantidad vendida.
def producto_mas_vendido(datos):
    conteo = {}
    for fila in datos:
        producto = fila['producto']
        cantidad = float(fila['cantidad'])
        if producto in conteo:
            conteo[producto] += cantidad
        else:
            conteo[producto] = cantidad
    
    # Buscamos el producto con mayor cantidad manualmente
    producto_mayor = None
    cantidad_mayor = 0
    for producto, cantidad in conteo.items(): #.items()  permite recorrer el diccionario obteniendo la clave y el valor al mismo tiempo.
        if cantidad > cantidad_mayor:
            cantidad_mayor = cantidad
            producto_mayor = producto
    
    return producto_mayor

#VENTAS POR MES: Agrupa y suma las ventas por mes.
def ventas_por_mes(datos):
    meses = {}
    for fila in datos:
        mes = fila['fecha'][:7]  # Toma los primeros 7 dígitos de la fila fecha (AAAA-MM) en el doc.
        monto = float(fila['monto'])
        if mes in meses:
            meses[mes] += monto
        else:
            meses[mes] = monto
    return meses

#RESULTADOS: Guarda los resultados del análisis en un archivo de texto.
def guardar_resultados(total, producto, meses, ruta): 
    with open(ruta, 'w', encoding='utf-8') as f:      # 'w' es para abrir el archivo en solo escritura, si no existe lo crea y lo llama f.
        f.write("=== RESULTADOS DEL ANÁLISIS DE VENTAS ===\n\n")     # f.write() guarda los resultados en un archivo de texto en el directorio resultados.
        f.write(f"Ventas totales: ${total:,.2f}\n") #,.2f escribe el número con dos decimales y separador por miles(ej: 1.023,01)
        f.write(f"Producto más vendido: {producto}\n\n")
        f.write("Ventas por mes:\n")
        for mes, monto in sorted(meses.items()): #sorted() ordena cronologicamente los meses.
            f.write(f"  {mes}: ${monto:,.2f}\n")
    print(f"Resultados guardados en {ruta}") #el print confirma en pantalla que el archivo fue correctamente guardado.


                    # PROGRAMA PRINCIPAL

#CARGA DE DATOS
def main(): #inicio del programa.
    datos = cargar_datos('../datos/ventas.csv') #guardo las listas con todas las filas en la variable datos.

    # CÁLCULOS
    total = calcular_total_ventas(datos)
    producto = producto_mas_vendido(datos)
    meses = ventas_por_mes(datos)

    #MOSTRAR RESULTADOS
    print("=== ANÁLISIS DE VENTAS ===")
    print(f"Ventas totales: ${total:,.2f}")
    print(f"Producto más vendido: {producto}")
    print("\nVentas por mes:")
    for mes, monto in sorted(meses.items()):
        print(f"  {mes}: ${monto:,.2f}")

    # GUARDAR RESULTADOS
    guardar_resultados(total, producto, meses, '../resultados/resultados_ventas.txt')

main() #ejecuta la función.

# REVISIÓN DE CÓDIGO - P3 (Luis) - SCRUM-3
# Fecha de revisión: 2026-05-26
# - El código es claro y fácil de leer.
# - No hay datos sensibles expuestos.
# - Las rutas son relativas, funciona bien en Colab.
# - El dataset está en CSV, compatible con el script.
