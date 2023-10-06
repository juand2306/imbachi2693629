maximo = int(input("Introduce un número máximo: "))
suma = 0
n = 1

while suma <= maximo:
    suma=suma+n
    n=n+1

print("El número natural más pequeño necesario para superar el máximo es:", n-1)
