def divisores(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total=total+i
    return total

def es_perfecto(n):
    return n == divisores(n)

cont = 0
for i in range(1, 1001):
    if es_perfecto(i):
        cont=cont+1
        print(i)

print("Hay", cont, "numeros perfectos entre 1 y 1000.")
