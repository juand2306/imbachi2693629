
diccionario_español_ingles = {}
diccionario_ingles_español = {}

def agregar_animal(clave, valor ):

    diccionario_español_ingles[clave] = valor
    diccionario_ingles_español[valor] = clave

    return diccionario_español_ingles, diccionario_ingles_español   


def traducir_español_ingles():
    palabra = input("Ingrese una palabra en español: ")
    if palabra in diccionario_español_ingles:
        traduccion = diccionario_español_ingles[palabra]
        print(f"Traducción al inglés: {traduccion}")
    else:
        print("La palabra no se encuentra en el diccionario.")

def traducir_ingles_español():
    palabra = input("Ingrese una palabra en inglés: ")
    if palabra in diccionario_ingles_español:
        traduccion = diccionario_ingles_español[palabra]
        print(f"Traducción al español: {traduccion}")
    else:
        print("La palabra no se encuentra en el diccionario.")


print('1-Ingresar nuevo animal ')
print('2-Traducir de español a ingles')
print('3-Traducir de ingles a español')
print('4-Salir ')
selector=1
while selector!=0:
    selector=(input('Digite la opcion'))
    match selector:
        case '1':
            suma1=
            print("La suma de la lista 1 es: ",suma1)

            suma2=sumaLista(lista2)
            print("La suma de la lista 2 es: ",suma2)

            if suma1>suma2:
                print("La primera lista tiene la suma mas alta")
            elif suma1==suma2:
                print("Son iguales")
            else:
                print("La segunda lista tiene la suma mas alta")
        case '2':
            mayor1=mayor(lista1)
            print("El mayor de la primera lista es: ",mayor1)

            mayor2=mayor(lista2)
            print("El mayor de la segunda lista es: ",mayor2)

            if mayor1>mayor2:
                print("La primera lista tiene el numero mayor")
            elif mayor1==mayor2:
                print("Son iguales")
            else:
                print("La segunda lista tiene el numero mayor")
        case '3':
            menor1=menor(lista1)
            print("El menor de la primera lista es: ",menor1)

            menor2=menor(lista2)
            print("El menor de la segunda lista es: ",menor2)

            if menor1<menor2:
                print("La primera lista tiene el numero menor")
            elif menor1==menor2:
                print("Son iguales")
            else:
                print("La segunda lista tiene el numero menor")
        case '4':
