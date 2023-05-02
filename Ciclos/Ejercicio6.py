maximo = 0
num = 1

while num > 0:
    num = int(input("Introduce un número positivo: "))
    if num > maximo:
        maximo = num

print("El máximo número introducido es:", maximo)
