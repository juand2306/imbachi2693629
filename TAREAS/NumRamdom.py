import random

numero = random.randint(1, 100)

while True:
    x = int(input("Adivina el número entre 1 y 100: "))
    if x == numero:
        print("Buena mi so, lo adivino")
        break
    elif x < numero:
        print("Uyy muy abajo")
    else:
        print("Uyy muy arriba")