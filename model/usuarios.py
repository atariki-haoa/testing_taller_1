import sqlite3
from sqlite3 import Error
from config.globals import DBPATH

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
        self.fecha_nacimiento = input("Fecha de Nacimiento (dd-mm-yyyy): ")
        
        while True:
            if input("¿Es Atleta? (si/no): ") == "si": 
                self.atleta = True
                break
            else:
                self.atleta = False
                break        
        con = sqlite3.connect(DBPATH)
        try:
            cursorObj = con.cursor()
            entities = (self.email, 
                        self.contraseña, 
                        self.nombre, 
                        self.primer_apellido, 
                        self.segundo_apelido,
                        self.genero,
                        self.fecha_nacimiento)
            cursorObj.execute("INSERT INTO usuarios VALUES(?, ?, ?, ?, ?, ?, ?)", entities)
            con.commit()
        except Error:
            print(Error)
            measure = None
        finally:
            con.close()
        return measure

    def login(self, correo, contraseña):
        return True