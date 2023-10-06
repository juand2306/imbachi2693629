def Tuplas():
    
    tupla1 = ()
    tupla2 = ()
    tupla3 = ()

    print("Ingrese valores para la primera tupla: ")
    for i in range(5):
        valor = int(input(f"Ingrese el valor {i + 1}: "))
        tupla1 += (valor,)

    print("Ingrese valores para la segunda tupla: ")
    for i in range(5):
        valor = int(input(f"Ingrese el valor {i + 1}: "))
        tupla2 += (valor,)

    for i in range(5):
        suma = tupla1[i] + tupla2[i]
        tupla3 += (suma,)

    print("Tupla1:", tupla1)
    print("Tupla2:", tupla2)
    print("Tupla3:", tupla3)

Tuplas()