inicio= int(input("Ingrese el valor de inicio: "))
fin = int(input("Ingrese el valor final: "))
incremento = int(input("Ingrese el incremento o decremento: "))

print("La serie es:")
if inicio < fin:
    for i in range(inicio, fin+1, incremento):
        print(i)
else:
    for i in range(inicio, fin-1, -incremento):
        print(i)

n = int(input("Ingrese un número positivo: "))
while n < 0:
    n = int(input("El número debe ser positivo. Ingrese otro: "))

multiples = []
for i in range(n, fin+1, n):
    multiples.append(i)

print(f"Hay {len(multiples)} múltiplos de {n} entre 0 y {fin}: {multiples}")