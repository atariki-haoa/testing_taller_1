import sqlite3
import datetime
from sqlite3 import Error
from config.globals import DBPATH

class IMC:
    
    def tabla_masculino(imc_valor):
        if imc_valor < 20:
            return "BAJO PESO"
        elif imc_valor >= 20 and imc_valor < 24.9:
            return "NORMAL"
        elif imc_valor >= 25 and imc_valor < 29.9:
            return "OBESIDAD LEVE"
        elif imc_valor >= 30 and imc_valor < 40:
            return "OBESIDAD SEVERA"
        elif imc_valor >= 40:
            return "OBESIDAD MUY SEVERA"
    
    def tabla_femenino(imc_valor):
        if imc_valor < 20:
            return "BAJO PESO"
        elif imc_valor >= 20 and imc_valor < 23.9:
            return "NORMAL"
        elif imc_valor >= 24 and imc_valor < 28.9:
            return "OBESIDAD LEVE"
        elif imc_valor >= 29 and imc_valor < 37:
            return "OBESIDAD SEVERA"
        elif imc_valor >= 37:
            return "OBESIDAD MUY SEVERA"

    
    def registrar_imc(self, usuario):
        self.usuario_id = usuario.usuario_id
        self.peso = input("Ingresar peso: ")
        self.altura = input("Ingresar altura: ")
        self.imc = self.peso / (self.altura * self.altura)
        if usuario.genero == 1:
            self.estado = self.tabla_masculino(self.imc)
        elif usuario.genero == 2:
            self.estado = self.tabla_femenino(self.imc)
        else:
            self.estado = "N/A"
        self.fecha = datetime.datetime.strptime(datetime.datetime.now()).strftime('%d/%m/%Y')
        con = sqlite3.connect(DBPATH)
        try:
            cursorObj = con.cursor()
            entities = (self.usuario_id,
                        self.peso,
                        self.altura,
                        self.imc,
                        self.estado,
                        self.fecha)
            cursorObj.execute("""INSERT INTO usuarios(
                                                usuario_id,
                                                peso,
                                                altura,
                                                imc,
                                                estado,
                                                fecha)
                                VALUES(?, ?, ?, ?, ?, ?)""", entities)
            con.commit()
        except Error:
            print(Error)
        finally:
            con.close()
    

    def lista(usuario):
        con = sqlite3.connect(DBPATH)
        try:
            cursorObj = con.cursor()
            query_select = """SELECT state FROM imc 
                              WHERE usuario_id = {id} """.format(usuario.usuario_id)
            cursorObj.execute(query_select)
            rows = cursorObj.fetchall()
            if (len(rows) > 0):
                for row in rows:
                    print("""Registros de salud:
                             Fecha: {fecha}
                             Peso: {peso}
                             Altura: {altura}
                             Estado: {estado}
                             
                             """.format(row.fecha, row.peso, row.altura, row.estado))
        except Error:
            print(Error)
        finally:
            con.close()
        return usuario