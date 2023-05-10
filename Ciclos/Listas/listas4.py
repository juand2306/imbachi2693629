""" Llenar un arreglo de n elementos con números generados con la función random. No
puede haber números repetidos. Si intenta ingresar al arreglo un número que ya existe,
imprimirlo para anunciar que ese número ya está en el arreglo"""


import random

tam=random.randint(10,15)

lista=[]
contador=0
print(tam)
for i in range(tam):
    while contador!=tam:
        num=int(random.randrange(20))
        if num not in lista:
            lista.append(num)
            contador=contador+1
        else:
            print(f"El numero {num} ya esta en la lista")

print(lista)