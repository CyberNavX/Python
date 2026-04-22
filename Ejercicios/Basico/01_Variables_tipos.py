#=======================================
    #01 Variables y tipos de datos
#=======================================

'''Descripcion del problema:

Un sistema de registro necesita procesar informacion basica de un usuario,
pero los datos vienen en formatos distintos. Se debe demostrar que puedes 
identificar la naturaleza de cada dato y transformarlo segun la necesidad 
del programa

Que se pide:
    1. Declaracion: Crear 3 variables que contengan Nombre, edad, estatura.
    2. Identificacion: Imprime en consola el tipo de dato de cada una de las variables
        original usando la funcion propia de Python para identificar tipos.
    3. Transformacion (Casting): Convierte la variable de tu edad a un numero decimal
        y convertir la variable de estatura a un numero entero.'''
        
        
print("-- Sistema de registros de datos basicos --\n")

#El usuario ingresa los datos para declarar las variables
Nombre = "Gerber Garcia Salas"
Edad = 21
Estatura = 1.70

#Comprobacion de tipos
print(f"La Variable Nombre es de tipo: {type(Nombre)}")

#Casting (Conversion) de int a floar y floar a int
tipoEdad = float(Edad)
tipoEstatura = int(Estatura)

print(f"Las personas con el nombre: {Nombre} tiene la edad de: {tipoEdad} y tiene las estatura de: {tipoEstatura} mts")


