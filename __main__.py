import os
from model.usuarios import registro, login

def __init__():
    while True:
        respuesta = input("Usuario nuevo (si/no): ") 
        if respuesta == "si":
            registro()
            break
        elif respuesta == "no":
            print("Identifiquese")
            correo =  input("Correo: ")
            contraseña = input("Contraseña: ")
            login(correo, contraseña)
            break

__init__()