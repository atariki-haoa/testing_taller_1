import sqlite3
from config.globals import DBPATH

#Funcion para crear la base de datos la primera vez que se inicie el programa
def sql_table():
    con = sqlite3.connect(DBPATH)
    cursorObj = con.cursor()
    cursorObj.execute("SELECT name from sqlite_master") #Query para verificar si existe o no la db
    tables = cursorObj.fetchall()
    print("Buscando tablas en base de datos...")
    if not tables: #Si no hay valores, significa que no existen tablas en la db
        print("No hay tablas en la base de datos")
        print("Procediendo a crear las tablas")
        cursorObj.execute("""CREATE TABLE IF NOT EXISTS usuarios(
                                        usuario_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                        email TEXT,
                                        contraseña TEXT,
                                        nombnre TEXT,
                                        primer_apellido TEXT,
                                        segundo_apellido TEXT,
                                        genero INTEGER,
                                        fecha_nacimiento FLOAT,
                                        ) """)
        con.commit()
        cursorObj.execute("""CREATE TABLE IF NOT EXISTS imc(
                                        imc_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        usuario_id INTEGER,
                                        peso FLOAT,
                                        altura FLOAT,
                                        imc FLOAT,
                                        estado TEXT,
                                        fecha FLOAT
                                        )""")
        con.commit()
        print("Tablas creadas")
    if tables:
        print("Tablas de datos encontradas!")