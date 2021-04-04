import sqlite3
import datetime
from datetime import datetime
from sqlite3 import Error
from config.globals import DBPATH

class IMC:

    def registrar_imc(self, usuario):
        self.usuario_id = usuario.usuario_id
        self.peso = float(input("Ingresar peso: "))
        self.altura = float(input("Ingresar altura: "))
        self.imc = self.peso / (self.altura * self.altura)
        if usuario.genero == 1:
            self.estado = tabla_masculino(self.imc)
        elif usuario.genero == 2:
            self.estado = tabla_femenino(self.imc)
        else:
            self.estado = "N/A"
        self.fecha =  datetime.today().strftime('%Y-%m-%d')
        con = sqlite3.connect(DBPATH)
        try:
            cursorObj = con.cursor()
            entities = (self.usuario_id,
                        self.peso,
                        self.altura,
                        self.imc,
                        self.estado,
                        self.fecha)
            cursorObj.execute("""INSERT INTO imc(
                                                usuario_id,
                                                peso,
                                                altura,
                                                imc,
                                                estado,
                                                fecha)
                                VALUES(?, ?, ?, ?, ?, ?)""", entities)
            con.commit()
            print("Estado nutricional: " + self.estado)
            print(" ")
        except Error:
            print(Error)
        finally:
            con.close()
    

    def lista(self, usuario):
        con = sqlite3.connect(DBPATH)
        try:
            cursorObj = con.cursor()
            query_select = "SELECT * FROM imc WHERE usuario_id = " + str(usuario.usuario_id)
            cursorObj.execute(query_select)
            rows = cursorObj.fetchall()
            if (len(rows) > 0):
                print("Registros de salud: ")
                for row in rows:
                    print("Fecha: " + row[6])
                    print("Peso: " + str(row[2]))
                    print("Altura: " + str(row[3]))
                    print( "Estado: " + row[5])         
                    print("-------")                    
        except Error:
            print(Error)
        finally:
            con.close()
        return usuario

def tabla_masculino(imc_valor):
    if imc_valor < 20:
        return bcolors.Yellow + "BAJO PESO" + bcolors.ENDC
    elif imc_valor >= 20 and imc_valor < 24.9:
        return bcolors.Green + "NORMAL" + bcolors.ENDC
    elif imc_valor >= 25 and imc_valor < 29.9:
        return bcolors.Orange + "OBESIDAD LEVE" + bcolors.ENDC
    elif imc_valor >= 30 and imc_valor < 40:
        return bcolors.Red + "OBESIDAD SEVERA" + bcolors.ENDC
    elif imc_valor >= 40:
        return bcolors.Red + "OBESIDAD MUY SEVERA" + bcolors.ENDC

def tabla_femenino(imc_valor):
    if imc_valor < 20:
        return bcolors.Yellow + "BAJO PESO" + bcolors.ENDC
    elif imc_valor >= 20 and imc_valor < 23.9:
        return bcolors.Green + "NORMAL" + bcolors.ENDC
    elif imc_valor >= 24 and imc_valor < 28.9:
        return bcolors.Orange + "OBESIDAD LEVE" + bcolors.ENDC
    elif imc_valor >= 29 and imc_valor < 37:
        return bcolors.Red + "OBESIDAD SEVERA" + bcolors.ENDC
    elif imc_valor >= 37:
        return bcolors.Red + "OBESIDAD MUY SEVERA" + bcolors.ENDC

class bcolors:
    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Orange = '\033[33m'
    ENDC = '\033[0m'