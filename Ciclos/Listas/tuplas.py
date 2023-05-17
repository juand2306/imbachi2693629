#Crear una tuplade tamaño aleatorio de maximo 20
#Llenar la tupla con numeros aleatorios entre 0 y 100 

import random

tam=random.randint(0,20)

#print(tupla)

tupla=()
for i in range(tam):
    num=random.randrange(100)
    tupla=tupla+(num,)

print (tupla)







