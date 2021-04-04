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
        usuario.registro()
    elif respuesta == "2":
        submenu(usuario)
    elif respuesta == "3":
        print("Hasta luego!")

def submenu(usuario):
    imc = model.imc.IMC()
    print("Identifiquese")
    correo =  input("Correo: ")
    contraseña = input("Contraseña: ")
    usuario = usuario.login(correo, contraseña)
    if usuario:
        print("""
        Informacion del usuario
        Nombre: {nombre} {primer_apellido} {segundo_apellido},
        Genero: {genero}
        Fecha nacimiento: {fecha_nacimiento} 
        Atleta: {atleta}
        Correo: {correo}

        Seleccione opcion: 
        """.format(usuario.nombre,
                   usuario.primer_apellido, 
                   usuario.segundo_apellido,
                   usuario.genero,
                   usuario.fecha_nacimiento,
                   usuario.atleta,
                   usuario.correo ))
        respuesta = input("""
                            1- Registrar nueva medicion IMC
                            2- Mostrar lista
                            3- Volver
                            """)
        if respuesta == "1":
            imc.registrar_imc(usuario)
        elif respuesta == "2":
            imc.lista(usuario)
        elif respuesta == "3":
            menu()
    else:
        print("usuario no encontrado")
        menu()


__init__()