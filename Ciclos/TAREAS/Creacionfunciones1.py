def numnat(x):
    suma = 0
    n = 1

    while suma <= maximo:
        suma=suma+n
        n=n+1
        
    return n-1

maximo = int(input("Introduce un número máximo: "))
lista=numnat(-1)

print("El número natural más pequeño necesario para superar el máximo es:",lista)