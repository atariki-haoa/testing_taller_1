import model.usuarios
import config.db_configuration
import model.imc

def __init__():
    print("Iniciando programa...")
    config.db_configuration.sql_table()
    menu()
    
def menu():
    usuario = model.usuarios.Usuario()
    respuesta = input("""
    Bienvenido al programa de calculo de IMC
    Seleccione una opcion:
    1- Registrar usuario
    2- Ingresar, calcular y registrar IMC
    3- Salir

    """) 
    if respuesta == "1":
        if usuario.ingresarDatos():
            print("Usuario ingresado correctamente")
        else:
            print("Error al ingresar el usuario")
        menu()
    elif respuesta == "2":
        auth(usuario)
    elif respuesta == "3":
        print("Hasta luego!")

def auth(usuario):
    print("Identifiquese")
    correo =  input("Correo: ")
    contraseña = input("Contraseña: ")
    usuario = usuario.login(correo, contraseña)
    if not usuario:
        print("usuario no encontrado o contraseña mal ingresada")
        menu()
    else:
        submenu(usuario)

def submenu(usuario):
    imc = model.imc.IMC()
    print("Informacion del usuario")
    print("Nombre: " + 
           usuario.nombre + " " +
           usuario.primer_apellido + " " + 
           usuario.segundo_apellido)
    genero = ""
    if usuario.genero == 1:
        genero = "Masculino"
    elif usuario.genero == 2:
        genero = "Femenino"
    else:
        genero = "No valido"
    print("Genero: " + genero)
    print("Fecha nacimiento: " + usuario.fecha_nacimiento)
    print("Atleta:" + "si" if usuario.atleta else "no" )
    print("Correo: " + usuario.email)
    print("Seleccione opcion: ")
    respuesta = input("""
                        1- Registrar nueva medicion IMC
                        2- Mostrar lista
                        3- Volver
                        """)
    if respuesta == "1":
        if (imc.calcularIMC(usuario)):
            print('IMC calculado correctamente')
        else:
            print('Error al calcular IMC')
        submenu(usuario)
    elif respuesta == "2":
        imc.mostrarListadoDeRegistros(usuario)
        submenu(usuario)
    elif respuesta == "3":
        menu()
        
__init__()