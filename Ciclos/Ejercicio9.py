x= float(input("Introduce la base: "))
n = int(input("Introduce el exponente: "))

if n == 0:
    resultado = 1
else:
    resultado = 1
    for i in range(1, abs(n)+1):
        resultado *= x
    if n < 0:
        resultado = 1 / resultado

print("El resultado es:", resultado)
