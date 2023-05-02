m = int(input("Introduce el primer número: "))
n = int(input("Introduce el segundo número: "))

while n != 0:
    r = m % n
    m = n
    n = r

print("El máximo común divisor es:", m)
