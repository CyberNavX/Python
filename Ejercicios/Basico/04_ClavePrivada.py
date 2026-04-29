#=======================================
    #04 clave para acceso 
#=======================================

'''
Descripcion del problema:

    Realizar un programa donde se le pida una clave al usuario y
    que sea igual a la clave y asi dar acceso o denegar.
'''

print("\n---- Control de acceso ---\n")
clave = input("Ingrese la contraseña de acceso: ")

if clave == "123@Charlie":
    print("La clave es aceptada, acceso concedido.")
else:
    print("La contraseña no es correcta, acceso denegado")