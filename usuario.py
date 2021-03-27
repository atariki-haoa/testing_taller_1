import datetime
import json
from typing import cast

class Usuario: 

    def registro(self):
        print("Ingrese datos de autentificacion")
        self.email = input("Email: ")
        self.contraseña = input("Contraseña: ")
        
        print("Ingrese los datos personales:")
        self.nombre = input("Nombre: ")
        self.primer_apellido = input("Primer apellido: ")
        self.segundo_apelido = input("Segundo apellido: ")
        self.genero = input("Genero: ")
        self.fecha_nacimiento = input("Fecha de Nacimiento: ")
        
        while True:
            if input("¿Es Atleta? (si/no): ") == "si": 
                self.atleta = True
                break
            else:
                self.atleta = False
                break        
        try:
            with open('usuarios.json', "r+") as file:
                data = json.load(file)
                data.update(self)
                json.dump(data, file)
            print("Usuario nuevo registrado exitosamente")
            return True
                
        except:
            print("Error al registrar el nuevo usuario")
            return False

    def login(self, correo, contraseña):
        file = csv.reader(open('usuarios.csv', "r"), delimiter=",")
        for row in file:
            if correo == row[0]:
                print (row)
        return True