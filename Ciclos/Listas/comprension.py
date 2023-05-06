import random

num=int(input("Ingrese el numero que quiere buscar entre 0 y 9"))
tam=random.randint(15,20)
cont=0
posicion=[]
lista=[random.randrange(0,9) for i in range (tam)]

for i in lista:
    if i == num:
        cont=cont+1
if num in lista:
    print("Si esta")
else:
    print("No esta")

if cont>=1:
    print("Esta repetido", cont, "veces")

for i in range (len(lista)):
    if num ==lista[i]:
        posicion.append(i)

print("El numero esta en las posiciones", posicion)

print(lista)