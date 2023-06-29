#sumar, promedio, max,min
import random


lista=[]
suma=0
promedio=0
max=0
min=10000
tam=int(random.randint(10,20))
print(tam)
for i in range (tam):
    num=int(random.randrange(100))
    lista.append(num)
    suma+=num
    promedio=suma/tam
    if num>max:
        max=num
    if num<min and num!=0:
        min=num

    

print(lista)

print("La suma de los datos es: ",suma)
print("El promedio de los numeros es: ",promedio)
print("El numero mas grande es: ", max)
print("El numero mas pequeño es: ", min)

