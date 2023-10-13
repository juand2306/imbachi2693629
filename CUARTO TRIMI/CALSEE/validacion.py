diccionario1={"juan":"1212",
             "dylan":"1111",
             "diego":"5555"
             }

def validar(usuario, contraseña):
    return usuario in diccionario1 and diccionario1[usuario] == contraseña

def validar_autenticacion(*args, **kwargs):
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if validar(usuario, contrasena):
        print("Bienvenido al sistema <3")
    else:
        print(" Usuario o contraseña incorrectos :( )")
        
validar_autenticacion()

