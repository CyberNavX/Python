#=======================================
    #03 Analizador de paquetes 
#=======================================

'''
Descripcion del problema:

    En este programa se implementara una calculadora de tamaño de archivos,
    el programa decide si el archivo es apto o no para enviar un archivo con limite.
'''

print("--- Calculadora para tamaño de archivos ---\n")

nombre_Archivo = input("Nombre del archivo: ")
tamaño_mb = float(input("Ingrese el tamaño del archivo en MB: "))

tamaño_kb = tamaño_mb * 1024
tamaño_Aceptado = tamaño_mb > 0 and tamaño_mb < 100

print(f"\n--- Archivo {nombre_Archivo} ---")
print(f"Tamaño del archivo en KB: {tamaño_kb} kB")
print(f"¿Tamaño aceptado del archivo?: {tamaño_Aceptado}")
