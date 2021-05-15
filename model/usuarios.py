import sqlite3
from sqlite3 import Error
from typing_extensions import runtime
from config.globals import DBPATH
import model.usuarios
import re
from itertools import cycle

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
    def registrarPersona(self):
        print("Ingrese datos de autentificacion")
        self.email = input("Email: ")
        
        print("Ingrese los datos personales:")
        self.rut = input("Rut:")
        self.nombre = input("Nombre: ")
        self.primer_apellido = input("Primer apellido: ")
        self.segundo_apelido = input("Segundo apellido: ")
        self.genero = input("Genero (1: Masculino, 2: Femenino): ")

        self.fecha_nacimiento = input("Fecha de Nacimiento (yyyy-mm-dd): ")
        self.atleta = True if input("¿Es Atleta? (si/no): ") == "si" else False
        
        self.contraseña = self.calcularContraseña()
        if(self.validarCorreo() and self.validarRut()):
            self.saveData()
        else:
            print("Correo invalido")


    def saveData(self):
        con = sqlite3.connect(DBPATH)
        try:
            cursorObj = con.cursor()
            entities = (self.email, 
                        self.contraseña, 
                        self.nombre, 
                        self.primer_apellido, 
                        self.segundo_apelido,
                        self.genero,
                        self.fecha_nacimiento,
                        self.atleta)
            cursorObj.execute("""INSERT INTO usuarios(
                                                email,
                                                contraseña,
                                                nombre,
                                                primer_apellido,
                                                segundo_apellido,
                                                genero,
                                                fecha_nacimiento,
                                                atleta)
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", entities)
            con.commit()
        except Error:
            print(Error)
        finally:
            con.close()

    #funcion de login, verifica autentificacion y crea un objeto usuario a partir
    #de los datos de ingreso
    def login(self, email_ingreso, contraseña):
        con = sqlite3.connect(DBPATH)
        usuario = model.usuarios.Usuario()
        try:
            cursorObj = con.cursor()
            query_select = """SELECT * FROM usuarios 
                              WHERE email = """ + "'" + email_ingreso + "';"
            cursorObj.execute(query_select)
            rows = cursorObj.fetchall()
            if (len(rows) <= 0):
                usuario = None
            else:
                data = rows[0]
                if data[2] == contraseña:
                    usuario.usuario_id = data[0]
                    usuario.email = data[1]
                    usuario.nombre = data[3]
                    usuario.primer_apellido = data[4]
                    usuario.segundo_apellido = data[5]
                    usuario.genero = data[6]
                    usuario.fecha_nacimiento = data[7]
                    usuario.atleta = data[8]
        except Error:
            print(Error)
        finally:
            con.close()
        return usuario
    
    def validarCorreo(self):
            regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
            if(re.search(regex, self.email)):
                return True
            else:
                return False
    
    def calcularContraseña(self):
        return self.email.split("@")[0] + self.rut[1:4]
    
    def validarRut(self):
        rut = self.rut
    	rut = rut.upper();
        rut = rut.replace("-","")
        rut = rut.replace(".","")
        aux = rut[:-1]
        dv = rut[-1:]
    
        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido,factors))
        res = (-s)%11
    
        if str(res) == dv:
            return True
        elif dv=="K" and res==10:
            return True
        else:
            return False
         