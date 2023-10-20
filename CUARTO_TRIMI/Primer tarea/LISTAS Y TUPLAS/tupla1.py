import random

def CuboCuadrado():
    tupla = (random.randrange(1, 10) for _ in range(10))

    print("Numero Cuadrado  Cubo")
    for i in tupla:
        cuadrado = i ** 2
        cubo = i ** 3
        print(f"{i}        {cuadrado}        {cubo}")

CuboCuadrado()