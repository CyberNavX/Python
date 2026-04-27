#=======================================
    #02 Operadores 
#=======================================

'''
Descripcion del problema:

    Este programa consiste en un contro de gastos con respecto a el ingreso 
    que tiene el usuario
    
    1. Pedir nombre, presupuesto, gastos
    2. Operaciones de gasto en el mes, dinero restante, procentaje del gasto
    3. Mostrar los resultados
'''

print("Calculadora de gastos y presupuesto\n")

nombre = input("Ingrese su nombre: ")
presupuesto = float(input("Ingrese su presupuesto: "))
gastos_diario = float(input("Ingrese sus gastos: "))

gasto_mensual = gastos_diario * 30
dinero_restante = presupuesto - gasto_mensual
porcentaje_Gastos = (gasto_mensual / presupuesto) * 100

print(f"\n--- Resumen para {nombre} ---")

print(f"Gasto proyectado al mes: Q{gasto_mensual:.2f}")
print(f"Dinero restante: Q{dinero_restante :.2f}")
print(f"Has consumido el {porcentaje_Gastos:.1f}% de tu presupuesto.")
