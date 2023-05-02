def sum_divisores(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    return suma

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

suma_a = sum_divisores(a)
suma_b = sum_divisores(b)

if suma_a == b and suma_b == a:
    print("Los números", a, "y", b, "son números amigos")
else:
    print("Los números", a, "y", b, "no son números amigos")
