import os
import usuario

def __init__():
    usuario_input = usuario.Usuario()
    while True:
        respuesta = input("Usuario nuevo (si/no): ") 
        if respuesta == "si":
            usuario_input.registro()
            break
        elif respuesta == "no":
            print("Identifiquese")
            correo =  input("Correo: ")
            contraseña = input("Contraseña: ")
            usuario_input.login(correo, contraseña)
            break

__init__()