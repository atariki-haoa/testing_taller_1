import sqlite3
import datetime
from sqlite3 import Error
from config.globals import DBPATH

# En la clase, se guardan en "self" los atributos del usuario, siendo estos:
# email,
# contraseña,
# nombnre,
# primer_apellido,
# segundo_apellido,
# genero,
# fecha_nacimiento

class Usuario: 
    # funcion de registro, crea y guarda usuario en la base de datos
    def registro(self):
        print("Ingrese datos de autentificacion")
        self.email = input("Email: ")
        self.contraseña = input("Contraseña: ")
        
        print("Ingrese los datos personales:")
        self.nombre = input("Nombre: ")
        self.primer_apellido = input("Primer apellido: ")
        self.segundo_apelido = input("Segundo apellido: ")
        self.genero = input("Genero (1: Masculino, 2: Femenino")

        self.fecha_nacimiento = input("Fecha de Nacimiento (dd/mm/yyyy): ")
        self.atleta = True if input("¿Es Atleta? (si/no): ") == "si" else False
           
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
            cursorObj.execute("""INSERT INTO usuarios(
                                                email,
                                                contraseña,
                                                nombre,
                                                primer_apellido,
                                                segundo_apellido,
                                                genero,
                                                fecha_nacimiento)
                                VALUES(?, ?, ?, ?, ?, ?, ?)""", entities)
            con.commit()
        except Error:
            print(Error)
        finally:
            con.close()

    #funcion de login, verifica autentificacion y crea un objeto usuario a partir
    #de los datos de ingreso
    def login(self, email_ingreso, contraseña):
        con = sqlite3.connect(DBPATH)
        usuario = {}
        try:
            cursorObj = con.cursor()
            query_select = """SELECT * FROM usuarios 
                              WHERE email = """ + "'" + email_ingreso + "';"
            cursorObj.execute(query_select)
            rows = cursorObj.fetchall()
            if (len(rows) > 0):
                temp_usuario = rows[0]
                if temp_usuario[1] == contraseña:
                    usuario = temp_usuario
        except Error:
            print(Error)
        finally:
            con.close()
        return usuario
